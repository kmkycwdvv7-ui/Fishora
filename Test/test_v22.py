from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime, timedelta
import re
root=Path(__file__).resolve().parent
if not (root/'index.html').exists():root=root.parent
html=(root/'index.html').read_text().replace('<link rel="stylesheet" href="styles.css">','').replace('<script defer src="data.js"></script>','').replace('<script defer src="app.js"></script>','')
html=re.sub(r'<(?:script|link)\b[^>]*unpkg\.com[^>]*>(?:</script>)?', '', html)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':900},accept_downloads=True);page.set_default_timeout(5000)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.on('dialog',lambda dialog:dialog.accept())
 page.set_content(html,wait_until='domcontentloaded')
 page.add_style_tag(content=(root/'styles.css').read_text())
 page.evaluate("""() => {const mem=new Map();Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>mem.has(k)?mem.get(k):null,setItem:(k,v)=>mem.set(k,String(v)),removeItem:k=>mem.delete(k),clear:()=>mem.clear(),key:i=>Array.from(mem.keys())[i]||null,get length(){return mem.size}}})}""")
 page.evaluate('''() => { window.fetch = async (u) => {
 if(String(u).includes('species_counts'))return {ok:true,json:async()=>({results:[{count:4,taxon:{name:'Dicentrarchus labrax',preferred_common_name:'Bar'}}]})};
 if(String(u).includes('overpass'))return {ok:true,json:async()=>({elements:[{type:'way',id:781,tags:{name:'Río Test OSM',waterway:'river'},center:{lat:38.35,lon:-0.49}}]})};
 if(String(u).includes('/v1/search?'))return {ok:true,json:async()=>({results:[{name:'Alicante',admin1:'Valencia',country:'Espagne',latitude:38.345,longitude:-0.481}]})};
 let day=new Date(); let days=[],times=[],temp=[],winds=[],prec=[],pressure=[],rises=[],sets=[];
 for(let d=0;d<16;d++){let dt=new Date(day.getFullYear(),day.getMonth(),day.getDate()+d).toISOString().slice(0,10);days.push(dt);rises.push(dt+'T07:00');sets.push(dt+'T19:00');for(let h=0;h<24;h++){times.push(dt+'T'+String(h).padStart(2,'0')+':00');temp.push(17);winds.push(7+d);prec.push(12+d);pressure.push(1018)}}
 if(String(u).includes('/api/interpreter?'))return {ok:true,json:async()=>({elements:[{type:'way',id:123,center:{lat:38.35,lon:-0.49},tags:{name:'Plage tests',natural:'beach'}}]})};
 if(String(u).includes('marine'))return {ok:true,json:async()=>({current:{wave_height:1,sea_surface_temperature:18,ocean_current_velocity:0.5},hourly:{time:times,wave_height:times.map(()=>1)}})};
 return {ok:true,json:async()=>({timezone:'Europe/Madrid',current:{temperature_2m:17,wind_speed_10m:14,pressure_msl:1018,precipitation:0},hourly:{time:times,temperature_2m:temp,wind_speed_10m:winds,precipitation_probability:prec,pressure_msl:pressure},daily:{time:days,sunrise:rises,sunset:sets}})};
 };}''')
 page.add_script_tag(content=(root/'data.js').read_text());page.add_script_tag(content=(root/'app.js').read_text());page.wait_for_timeout(550)
 print('PAGE',page.locator('h1').first.inner_text())
 page.locator('.modal .close').click()
 # source French gear -> external inventory
 print('CHECKPOINT gear',flush=True)
 page.locator('.side-nav [data-page=gear]').click()
 for name, typ, inv, qty in [('Canne mer','Canne','es',1),('Moulinet mer','Moulinet','es',1),('Leurre France','Leurre','fr',3)]:
  page.locator('[data-action=add-gear]').click();m=page.locator('.modal');m.locator('[name=name]').fill(name);m.locator('[name=type]').select_option(label=typ);m.locator('[name=inventoryId]').select_option(inv);m.locator('[name=qty]').fill(str(qty));m.locator('[type=submit]').click();page.wait_for_timeout(80)
 print('CHECKPOINT plan',flush=True)
 page.locator('.side-nav [data-page=plan]').click()
 assert page.locator('#planForm input[name=lat]').get_attribute('type')=='hidden'
 assert page.locator('#planForm input[name=lon]').get_attribute('type')=='hidden'
 # A new plan must not silently inherit the global reference coordinates.
 assert page.locator('#planForm [name=locationConfirmed]').input_value()=='0'
 assert page.locator('#planForm [name=lat]').input_value()==''
 assert page.locator('#planForm [name=lon]').input_value()==''
 assert page.locator('[data-action=plan-geolocate]').count()==1
 
 page.locator('#planForm [name=name]').fill('Voyage Alicante')
 page.locator('#planForm [name=city]').fill('Alicante')
 page.locator('#planForm [name=country]').fill('Espagne')
 page.locator('[data-action=search-plan-destination]').click();page.wait_for_timeout(150)
 assert page.locator('[data-action=pick-plan-destination]').count()>0
 page.locator('[data-action=pick-plan-destination]').first.click()
 assert page.locator('#planForm [name=lat]').input_value()=='38.345'
 assert page.locator('#planForm [name=place]').input_value().startswith('Alicante')
 assert not page.locator('#planForm [name=lat]').is_visible()
 assert not page.locator('#planForm [name=lon]').is_visible()
 page.locator('#planForm [name=env]').select_option('sea')
 page.locator('#planForm [name=technique]').select_option('leurres')
 page.locator('#planForm [name=access]').select_option('bord')
 page.locator('#planForm [name=invIds][value=fr]').uncheck()
 page.locator('#planForm [name=invIds][value=es]').check()
 page.locator('#planForm [type=submit]').click();page.wait_for_timeout(650)
 data=page.evaluate('FishoraTest.getData()');assert len(data['plans'])==1,data
 assert data['plans'][0]['city']=='Alicante'
 assert data['plans'][0]['country']=='Espagne'
 assert data['plans'][0]['locationSource']=='city'
 plan=data['plans'][0]
 assert plan['access']=='bord' and plan['invIds']==['es']
 assert page.locator('[data-action=retain-slot]').count()>4, page.locator('body').inner_text()[-1500:]
 # Automatic water-place discovery must be based on OSM names, not imaginary fish populations.
 assert page.locator('[data-action=save-plan-water]').count()>0, 'Automatic nearby water discovery not presented'
 page.locator('[data-action=find-plan-water]').click();page.wait_for_timeout(250)
 assert 'Río Test OSM' in page.locator('main').inner_text()
 page.locator('[data-action=save-plan-water]').first.click();page.wait_for_timeout(100)
 assert any(x['name']=='Río Test OSM' for x in page.evaluate('FishoraTest.getData().spots'))
 page.locator('[data-action=retain-slot]').first.click();page.wait_for_timeout(80)
 page.locator('[data-action=retain-slot]').nth(1).click();page.wait_for_timeout(80)
 assert len(page.evaluate('FishoraTest.getData().plans[0].confirmedSlots'))==2
 # update saved first slot
 page.locator('[data-action=edit-slot]').first.click();m=page.locator('.modal');m.locator('[name=startHour]').fill('08:00');m.locator('[name=endHour]').fill('10:00');m.locator('[name=spotId]').select_option(page.evaluate('FishoraTest.getData().spots[0].id'));m.locator('[type=submit]').click();page.wait_for_timeout(100)
 assert page.evaluate('FishoraTest.getData().plans[0].confirmedSlots[0].startHour')=='08:00'
 assert page.evaluate('FishoraTest.getData().plans[0].confirmedSlots[0].place')=='Río Test OSM'
 # inventory status and technique strategy
 statuses=page.evaluate('FishoraTest.materialPlan(FishoraTest.getData().plans[0])')
 assert next(x for x in statuses if x['type']=='Canne')['status']=='available',statuses
 assert next(x for x in statuses if x['type']=='Leurre / Appât')['status']=='bring',statuses
 print('CHECKPOINT OSM sites',flush=True)
 page.locator('[data-action=find-plan-species]').click();page.wait_for_timeout(120)
 assert 'Dicentrarchus labrax' in page.locator('main').inner_text(),page.locator('main').inner_text()[-2500:]
 print('CHECKPOINT local biology',flush=True)
 print('CHECKPOINT calendar',flush=True)
 with page.expect_download() as d: page.locator('[data-action=calendar]').first.click()
 ics=Path(d.value.path()).read_text()
 assert ics.count('BEGIN:VEVENT')==2,ics
 assert 'T080000' in ics
 print('CHECKPOINT technique',flush=True)
 # technique incompatibility flag
 page.locator('#planForm [name=species]').select_option('bar')
 page.locator('#planForm [name=technique]').select_option('mouche')
 page.locator('#planForm [type=submit]').click();page.wait_for_timeout(200)
 assert 'à reconsidérer' in page.locator('body').inner_text().lower()
 print('CHECKPOINT forecast',flush=True)
 # forecast fish grading selector change
 page.locator('.side-nav [data-page=forecast]').click();page.wait_for_timeout(180)
 assert page.locator('.fish-rating').count()>10
 assert page.locator('.forecast-day').count()==16
 first=page.locator('.forecast-day .fish-rating').first.get_attribute('aria-label')
 page.locator('select[name=forecastTechnique]').select_option('mouche');page.wait_for_timeout(110)
 assert page.locator('select[name=forecastTechnique]').input_value()=='mouche'
 assert page.locator('.forecast-day .fish-rating').first.get_attribute('aria-label')
 print('forecast fish:',first,'| upgraded:',page.locator('.forecast-day .fish-rating').first.get_attribute('aria-label'))
 print('CHECKPOINT GPS and anti-stale-location',flush=True)
 page.locator('.side-nav [data-page=plan]').click()
 page.locator('[data-action=new-plan]').click()
 assert page.locator('#planForm [name=locationConfirmed]').input_value()=='0'
 page.evaluate('''() => Object.defineProperty(navigator,'geolocation',{configurable:true,value:{getCurrentPosition:(yes,no,options)=>yes({coords:{latitude:43.5512,longitude:7.0134,accuracy:16}}),watchPosition:()=>1,clearWatch:()=>{}}})''')
 page.locator('[data-action=plan-geolocate]').click();page.wait_for_timeout(120)
 assert page.locator('#planForm [name=locationConfirmed]').input_value()=='1'
 assert page.locator('#planForm [name=lat]').input_value()=='43.5512'
 assert page.locator('#planForm [name=lon]').input_value()=='7.0134'
 page.locator('#planForm [name=city]').fill('Lyon')
 assert page.locator('#planForm [name=locationConfirmed]').input_value()=='0', 'Stale coordinates accepted after city edit'
 page.locator('#planForm [name=name]').fill('GPS voyage')
 page.locator('#planForm [type=submit]').click();page.wait_for_timeout(120)
 assert len(page.evaluate('FishoraTest.getData().plans'))==1, 'Unresolved location must not be saved'
 page.locator('[data-action=plan-geolocate]').click();page.wait_for_timeout(100)
 page.locator('#planForm [type=submit]').click();page.wait_for_timeout(240)
 assert len(page.evaluate('FishoraTest.getData().plans'))==2
 assert next(x for x in page.evaluate('FishoraTest.getData().plans') if x['name']=='GPS voyage')['locationSource']=='gps'
 print('CHECKPOINT manual',flush=True)
 page.locator('[data-action=open-plan]').filter(visible=True).first.click();page.wait_for_timeout(60)
 # manual selection when no weather
 page.locator('.side-nav [data-page=plan]').click();page.locator('[data-action=manual-slot]').click();m=page.locator('.modal');m.locator('[type=submit]').click();page.wait_for_timeout(80)
 assert max(len(x['confirmedSlots']) for x in page.evaluate('FishoraTest.getData().plans'))>=3
 print('CHECKPOINT mobile',flush=True)
 # mobile UI
 mob=b.new_page(viewport={'width':390,'height':844},is_mobile=True,device_scale_factor=2)
 moberr=[];mob.on('pageerror',lambda e:moberr.append(str(e)))
 mob.set_content(html,wait_until='domcontentloaded');mob.add_style_tag(content=(root/'styles.css').read_text())
 mob.evaluate("() => {window.fetch=async()=>{throw Error('offline')}}")
 mob.add_script_tag(content=(root/'data.js').read_text());mob.add_script_tag(content=(root/'app.js').read_text());mob.wait_for_timeout(450)
 if mob.locator('.modal .close').count():mob.locator('.modal .close').click()
 mob.locator('.bottom-nav [data-page=plan]').click();mob.wait_for_timeout(100)
 assert mob.locator('#planForm').count()==1
 assert mob.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 3'),(mob.evaluate('document.documentElement.scrollWidth'),mob.evaluate('window.innerWidth'))
 print('CHECKPOINT screenshot',flush=True)
 page.locator('.side-nav [data-page=plan]').click();page.screenshot(path=str(root/'FISHORA_V2_2_APERCU_DESKTOP.png'),full_page=True)
 mob.screenshot(path=str(root/'FISHORA_V2_2_APERCU_MOBILE.png'),full_page=True)
 assert not errors,errors
 assert not moberr,moberr
 print('ALL TESTS PASSED | errors:',errors,'mobile:',moberr)
 b.close()
