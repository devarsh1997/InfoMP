from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

mp_data_unified = [{
   "full_name": "Nalin Kumar Kateel",
   "constituency": "Dakshina Kannada",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "No. 201, Ashoka Apartment, Near Daiwajna Kalyana Mantapa,Hoigebail Road, Ashok Nagar, Mangalore - 575006 Karnataka(0824) 2444319, 2455215, 09448549445 (M)",
   "present_address": "142, South Avenue,New Delhi - 110 011Tels. 9654229367 (M), 9013180145 (M)",
   "email_id": "nalinkumar.kateel@sansad.nic.in"
  },
  {
   "full_name": "Mallikarjun Kharge",
   "constituency": "Gulbarga",
   "party": "Indian National Congress",
   "state": "Karnataka",
   "permanent_address": "Lumbini Aiwan-e-Shahi Area, Gulbarga, Karnataka09980035555 (M)",
   "present_address": "9, Safdarjang Road,New Delhi- 110 011Tels. (011) 23386645, 23381213(O), 09971300079 (M) Telefax: (011) 23793068, 23793082 (R) Fax: (011) 23387333 (O)",
   "email_id": "m.kharge@sansad.nic.in mallikarjunkharge@yahoo.in",
   "countries_visited": "Australia,Brazil,China, Czech Republic,France,Germany,Italy, New Zealand, Sweden,Thailand, U.K."
  },
  {
   "full_name": "Kamlesh Paswan",
   "constituency": "Bansgaon",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Paswan Niwas, Opposite BRD Medical College, North Gate,Gorakhpur, Uttar PradeshMob : 09013180277, 09415086756",
   "present_address": "25, Ferozshah Road,New DelhiTel : (011) 23795191, 23782550, 23782551 Mob : 09013180277",
   "email_id": "kamlesh.paswan@sansad.nic.in kamleshpassi67@gmail.com",
   "countries_visited": "China, Dubai, Germany, Hong Kong (Special Administrative Region of the People`s Republic of China), Malaysia, Singapore, Switzerland, Thailand and U.S.A."
  },
  {
   "full_name": "Virender Kashyap",
   "constituency": "Shimla",
   "party": "Bharatiya Janata Party",
   "state": "Himachal Pradesh",
   "permanent_address": "Daulat Niwas, Gupta Lodge, The Mall, Solan - 173 212,Himachal Pradesh(01792) 222998, 09816274646 (M) Fax. (01792) 222998",
   "present_address": "152 - 154, North Avenue, New Delhi -110 001Tels. (011) 23093228 9013180063 (M) Fax. (011) 23093912",
   "email_id": "(i) virenderkashyapbjp@yahoo.co.in (ii) virendra.kashyap@sansad.nic.in",
   "countries_visited": "Egypt, Germany, Greece, Holland, Israel, Spain and Turkey"
  },
  {
   "full_name": "Jagdambika Pal",
   "constituency": "Domariyaganj",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "3/249, Vinay Khand, Gomti Nagar,Lucknow,Uttar Pradesh09013180217,09335283287,0941503781(M)",
   "present_address": "12, Teen Murti Marg,New DelhiTel.(011) 23795370 9013180217, 09335283287, 09415037381 (M) Fax.(011) 23795377",
   "email_id": "1. mp.jpal@yahoo.com 2. jagdambika.pal@sansad.nic.in",
   "countries_visited": "Australia, Cuba, China, France, Germany, Northen Ireland, Newzealand, Sri Lanka, U.S.A., England and Malanya."
  },
  {
   "full_name": "Feroze Varun Gandhi",
   "constituency": "Sultanpur",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "14, Ashoka RoadNew Delhi - 110 001Tele:(011) 23357088,0 99155006(M) Fax: (011) 23354321",
   "present_address": "14, Ashoka Road,New Delhi - 110 001Tels. (011) 23357088 099155006(M) Fax. (011) 23354321",
   "email_id": "ferozevarun.gandhi@sansad.nic.in 14ashokaroad@gmail.com",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Prof. Ram Shankar",
   "constituency": "Agra",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "1, Teachers` Home University CampusKhandari, Agra-282002, Uttar PradeshTels. (0562) 2527933, 09412750008 (M)",
   "present_address": "43, North Avenue,New Delhi - 110 001Tels. 09013180116 (M)",
   "email_id": "1. office.mpagra@gmail.com 2. rs.katheria@sansad.nic.in"
  },
  {
   "full_name": "Rajnath Singh",
   "constituency": "Lucknow",
   "party": "Bharatiya Janata Party",
   "state": "04, Kalidas Marg,Lucknow, Uttar PradeshTel. (0522) 2236338",
   "permanent_address": "17, Akbar RoadNew Delhi - 110 011Tel. (011) 23793881 Telefax. (011) 23014184",
   "present_address": "38ashokroad@gmail.com",
   "email_id": "Education Qualifications: M.Sc. (Physics) Educated at Gorakhpur University,Gorakhpur, Uttar Pradesh"
  },
  {
   "full_name": "Rajendra Agrawal",
   "constituency": "Meerut",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "135,Chanakyapuri,Shastri Nagar,PradeshMeerut - 250005, Uttar PradeshTelefax. (0121) 2769955, 09412202623(M),",
   "present_address": "201, Narmada Apartment, Dr. B.D. MargNew Delhi - 110 001Tels. 09013180336 (M)",
   "email_id": "1. rajendra.agrawal51@gmail.com 2. rajendra.agrawal@sansad.nic.in",
   "countries_visited": "Nepal, South Africa and Vietnam"
  },
  {
   "full_name": "Anurag Singh Thakur",
   "constituency": "Hamirpur",
   "party": "Bharatiya Janata Party",
   "state": "Himachal Pradesh",
   "permanent_address": "Vill. & P.O. Samirpur, Distt. Hamirpur,Himachal Pradesh(01972) 275060 Fax. (01972) 275265",
   "present_address": "14, JanpathNew Delhi -110 001Tels. (011) 23782365 Fax. (011) 23782368",
   "email_id": "(i) hpcapresident@yahoo.com (ii) mphamirpur @gmail.com",
   "countries_visited": "Australia, German Democratic Republic,Hong Kong,Japan, Malaysia, New Zealand, Pakistan, South Africa, Spain, Sweden, Switzerland, Thailand, U.A.E, U.S.A.,and U.K."
  },
  {
   "full_name": "Abu Hasem Khan Choudhury",
   "constituency": "Maldaha Dakshin",
   "party": "Indian National Congress",
   "state": "Vill. - Sah Jalalpur, P.O - Kotwali, P.S. - English Bazar,Distt. - Malda, West Bengal(03512) 283593, 09868180995 (M)",
   "permanent_address": "22, Gurdwara Rakab Ganj Road,New Delhi - 110 001Tels. (011) 23712727, 23712828, 23061016, 23061551, 23062828 (O) 9868180995 (M) Fax (011) 23712829 (R), 23061157 (O)",
   "present_address": "ahk.chowdhury@sansad.nic.in",
   "email_id": "Education Qualifications: Graduate (Degree in Industrial Psychology) Educated at Northampton College of Technology, England and University of Guleph, Ontario, Canada"
  },
  {
   "full_name": "Deepender Singh Hooda",
   "constituency": "Rohtak",
   "party": "Indian National Congress",
   "state": "Vill. & P.O. Sanghi,Teh. & Distt. Rohtak,Haryana09818368168(M)",
   "permanent_address": "9, Pandit Pant Marg,New Delhi - 110 001Tels. (011) 23737019, 09818368168 (M)",
   "present_address": "office@deepender.in",
   "email_id": "Education Qualifications: B.Tech., M.B.A. Educated at University at Birla Institute, M.D. University, Rohtak (Haryana) and Kelley School of Business, Indiana University, Bloomington, USA"
  },
  {
   "full_name": "Dharmendra Yadav",
   "constituency": "Badaun",
   "party": "Samajwadi Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Vill. & P.O. Saifai, District EtawahUttar PradeshTel : (05688) 276017, 276551 Mob : 09720170999",
   "present_address": "91, Lodhi EstateNew DelhiMob : 09720170999",
   "email_id": "d.yadav@sansad.nic.in",
   "countries_visited": "France, Holland, Italy and Switzerland"
  },
  {
   "full_name": "Mohammad Salim",
   "constituency": "Raiganj",
   "party": "Communist Party of India (Marxist)",
   "state": "West Bengal",
   "permanent_address": "7-C, New Amrapali, 10/2, Diamond Harbour Road, Alipur-700027, West Bengal",
   "present_address": "408, V.P. House, Rafi MargNew Delhi - 110001",
   "email_id": "md.salim@sansad.nic.in",
   "countries_visited": "Widely travelled (22 countries) visited Algeria, Cuba, D.P.R. Korea and U.S.S.R. to attend youth festival, Mongolia to attend a Round Table Discussion on youth, 1988; Pakistan to attend SAARC Speakers and Parliamentarians Conference,1997; and Portugal to attend World Assembly of Youth; and Switzerland and Phillipines to attend IPU"
  },
  {
   "full_name": "P. Karunakaran",
   "constituency": "Kasaragod",
   "party": "Communist Party of India (Marxist)",
   "state": "Kerala",
   "permanent_address": "Amaravathi House, P.O. Nileswaram, Distt. Kasaragod, KeralaTels. (04672) 280990, 09868180357 (M)",
   "present_address": "41, North Avenue,New Delhi - 110 001Tels. (011) 23094503 9868180357, 9847040081 (M) Fax. (011) 23093778",
   "email_id": "karunakaran.p@sansad.nic.in pkarunakaranmp@gmail.com",
   "countries_visited": "Bahrain,China, U.A.E., U.S.A. and Vietnam"
  },
  {
   "full_name": "Shyama Charan Gupta",
   "constituency": "Allahabad",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "44 Thornhill Road, Allahabad - 211 002Uttar PradeshTel : (0532) 2468585/86, Mob : 09415235305 Fax : (0532) 2468579",
   "present_address": "404, Narmada, MS Flats, Dr. B.D. Marg,New Delhi-110001",
   "email_id": "shyamacharangupta@shyamscharangupta.co.in",
   "countries_visited": "U.S.A."
  },
  {
   "full_name": "Sarbananda Sonowal",
   "constituency": "Lakhimpur",
   "party": "Bharatiya Janata Party",
   "state": "12 Tughlak Road,New Delhi - 110 003Tel. (011) 23010214, 23010225",
   "permanent_address": "sarbananda.sonowal@sansad.nic.in",
   "present_address": "Education Qualifications: LL.B., B.C.J. Educated at Dibrugarh University and,Gauhati University"
  },
  {
   "full_name": "Shivaji Adhalrao Patil",
   "constituency": "Shirur",
   "party": "Shiv Sena",
   "state": "Maharashtra",
   "permanent_address": "At & P.O. Landewadi, Tal. Ambegaon,Distt.Pune-410503, MaharashtraTel : (02133) 235101 Mob : 09820021344 </br> Fax : (02133) 235102",
   "present_address": "59, Lodhi Estate,New Delhi - 110003Tel. : (011) 24635556, 24656554 </br>Mob : 09868180788 Fax : (011) 24693334",
   "email_id": "shivajirao@sansad.nic.in <b>website</b> : www.shivajirao.com",
   "countries_visited": "Widely Travelled"
  },
  {
   "full_name": "Mehbooba Mufti",
   "constituency": "Anantnag",
   "party": "Jammu and Kashmir Peoples Democratic Party",
   "state": "Jammu & Kashmir House,</br>Kautilya Marg,</br>Chanakyapuri,New Delhi-110 021",
   "permanent_address": "Education Qualifications: B.A., LL.B. Educated at Kashmir University",
   "present_address": "Saudi Arabia, Ireland, U.K.and U.S.A."
  },
  {
   "full_name": "Jay Prakash Narayan Yadav",
   "constituency": "Banka",
   "party": "Rashtriya Janata Dal",
   "state": "Bihar",
   "permanent_address": "Vill. P.O. Barhat,Distt, Jamui (Bihar)09899550954 (M)",
   "present_address": "6, North Avenue,New Delhi - 110 00109899550954 (M)",
   "email_id": "jpnarayan.yadav@sansad.nic.in"
  },
  {
   "full_name": "Ranjeet Ranjan",
   "constituency": "Supaul",
   "party": "Indian National Congress",
   "state": "Bihar",
   "permanent_address": "Ranjan Niketan, Court Station,Purnia (Bihar)(06454)227479,227922",
   "present_address": "67-68/Z Block, West Patel NagarNew Delhi.",
   "email_id": "ranjeet.ranjan19@sansad.nic.in"
  },
  {
   "full_name": "Asaduddin Owaisi",
   "constituency": "Hyderabad",
   "party": "All India Majlis-E-Ittehadul Muslimeen",
   "state": "Telangana",
   "permanent_address": "3-6-149, Hyderguda,Hyderabad - 500 029,TelanganaTels. (040) 2322278, 09848013569 (M)",
   "present_address": "34, Ashoka Road,New Delhi - 110 001Tels. (011) 23712208, 09868180569 (M)",
   "email_id": "asad.owaisi@sansad.nic.in",
   "countries_visited": "Attended and participated in Commonwealth Parliamentary Conference in Manchester, U.K., 1996"
  },
  {
   "full_name": "Thupstan Chhewang",
   "constituency": "Ladakh",
   "party": "Bharatiya Janata Party",
   "state": "Jammu and Kashmir",
   "permanent_address": "Sankar Khar, Idgah Road, Chhubi, Ladakh,Leh-194101, Jammu & KashmirTel/Fax: (01982) 252955, 09419179174 (M)",
   "present_address": "Ashoka Hotel, Chankyapuri,New Delhi - 110 021Tel. 9013869155 (M)",
   "email_id": "(i) thupstan.chhewang@sansad.nic.in (ii) thupstanc@yahoo.co.in",
   "countries_visited": "Denmark, Germany, South Africa, Soviet Union and Switzerland"
  },
  {
   "full_name": "Vinod Kumar Boianapalli",
   "constituency": "Karimnagar",
   "party": "Telangana Rashtra Samithi",
   "state": "Telangana",
   "permanent_address": "Flat No. 401, Poloumi Towers, Mukarampura, Karimnagar-505001TelenganaMob : 09848037689, 09643013567",
   "present_address": "Harish Chandra Mathur Lane, Bunglow No. 3 Feroz Shah Road,New Delhi-110001",
   "email_id": "vkumar.boinapally@sansad.nic.in",
   "countries_visited": "Austria, France, Germany, Italy, Netherlands, Switzerland, U.K., U.S.A."
  },
  {
   "full_name": "Rahul Gandhi",
   "constituency": "Amethi",
   "party": "Indian National Congress",
   "state": "12, Tughlak Lane,New Delhi - 110 011Tels. (011) 23795161 Fax. (011) 23012410",
   "permanent_address": "office@rahulgandhi.in",
   "present_address": "Education Qualifications: M.Phil. (Development Economics) Educated at Trinity College, Cambridge University, U.K.",
   "email_id": "Widely travelled"
  },
  {
   "full_name": "Thokchom Meinya",
   "constituency": "Inner Manipur",
   "party": "Indian National Congress",
   "state": "Manipur",
   "permanent_address": "Joypurkhul Khumbong BazarP.O. Langjing, Imphal West Manipur - 795 113(0385) 2569205, 2051306 09436021818,08014223769 (M) Fax. (0385) 2569205",
   "present_address": "A-3, M.S.Flats, B.K.S. Marg,New Delhi - 110 001Tels. (011) 23711696 9868180295 (M) Fax. (011) 23766499",
   "email_id": "meinya@sansad.nic.in",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "S.P.Y. Reddy",
   "constituency": "Nandyal",
   "party": "Yuvajana Sramika Rythu Congress Party",
   "state": "Andhra Pradesh",
   "permanent_address": "30/726,Bommala Satram,Nandyal,Distt.Kurnool-518502,Andhra Pradesh(08514)243105, 09848020190, 09868180182(M) <br/>(08514)243350 243340(Fax)",
   "present_address": "4, Talkatora Road,New Delhi - 110 001 09868180182 (M)",
   "email_id": "spy.reddy@sansad.nic.in, spy.reddy19@sansad.nic.in",
   "countries_visited": "Germany, Singapore and U.A.E. (Dubai)"
  },
  {
   "full_name": "Sanjay Shamrao Dhotre",
   "constituency": "Akola",
   "party": "Bharatiya Janata Party",
   "state": "Maharashtra",
   "permanent_address": "At & Post. Palso,(Badhe), Teh. Akola,Distt. Akola-444001, </br>MaharashtraTels. (0724)2457214, 2452000",
   "present_address": "B-801, MS Flats, B.K.S. Marg, New Delhi -110001",
   "email_id": "Education Qualifications: B.E. (Mech.) Educated at Government College of Engineering, Amravati, Maharashtra"
  },
  {
   "full_name": "Dushyant Singh",
   "constituency": "Jhalawar-Baran",
   "party": "Bharatiya Janata Party",
   "state": "Rajasthan",
   "permanent_address": "Raj Niwas, Dholpur, Rajasthan(05642) 220216, 09414027979 (M)",
   "present_address": "AB - 17, Tilak Marg,New Delhi - 110 001Tels. (011) 23782605, 9810896886 (M)",
   "email_id": "Education Qualifications: B.A. , M.B.A. (Hotel Administration) and P.G. Diploma in Hotel Operations Educated at St. Stephen`s College, Delhi, Johnson and Wales University, Providence, RI, USA and IHTTI School of Mangaement, Neuchatel, Switzerland"
  },
  {
   "full_name": "Harishchandra Deoram Chavan",
   "constituency": "Dindori",
   "party": "Bharatiya Janata Party",
   "state": "Maharashtra",
   "permanent_address": "3, Ananddeep Housing Society, Patil Lane, No.2,</br> College Road,Nasik - 422 005, MaharashtraTel: (0253) 2570111",
   "present_address": "C - 6, A - Block, MS Flats,</br> B.K.S. Marg,</br> Opp. Ram Manohar Lohiya Hospital,New Delhi - 110 001Tel: (011) 23352555, 09868180370 (M)",
   "email_id": "harishchandra.chavan@sansad.nic.in"
  },
  {
   "full_name": "Rakesh Singh",
   "constituency": "Jabalpur",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "578, South Civil Lines,Jabalpur - 482 001</br>Madhya PradeshTels. (0761) 2410099, 09425150851 (M)</br> Fax. (0761) 4017799",
   "present_address": "20, Dr. Rajendra Prasad Road,New Delhi - 110 001Tels. (011) 23071900, 9868180233 (M)</br> Fax. (011) 23071900",
   "email_id": "singh.rakesh19@sansad.nic.in",
   "countries_visited": "Frankfurt (Germany), Geneva (Switzerland), Mauritius, Paris (France), Russia"
  },
  {
   "full_name": "Ganesh Singh",
   "constituency": "Satna",
   "party": "Bharatiya Janata Party",
   "state": "Friends Colony, Near ITI,Satna, Madhya PradeshTel : (011) 23093470, (07672) 257999, Mobile : 09425172508 Fax : (07672) 257221",
   "permanent_address": "8, Rakab Ganj Gurudwara Road,New Delhi -110 001Tel : (011) 23093470 Telefax : (011) 23323644 Mobile : 9968410696, 9013180008",
   "present_address": "sganesh@sansad.nic.in",
   "email_id": "Education Qualifications: M.A., LL.B. Educated at Awadesh Pratap Singh University, Rewa and Law College, Satna, Madhya Pradesh"
  },
  {
   "full_name": "Parvatagouda Chandanagouda Gaddigoudar",
   "constituency": "Bagalkot",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "Laxminagar, Badami,Distt. Bagalkot, Karnataka-587102Tel : (08357) 220164 Mob : 09448137164",
   "present_address": "Flat No. 704, Narmada Apartment, B.D. Marg, Near R.M.L. Hospital, New Delhi - 110001Tel : (011) 23314162 Mob : 09868180612",
   "email_id": "pcgaddigoudar@rediffmail.com"
  },
  {
   "full_name": "Suresh Chanabasappa Angadi",
   "constituency": "Belgaum",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "\"Spoorthi\" Sampige Road,Vishweshwarayya Nagar,Belgaum,KarnatakaTels: (0831)2405141, 2452916 Fax:(0831)2476420 09980050813 (M)",
   "present_address": "Flats No. 44-46, South Avenue,New Delhi -110 011Tele Fax. (011) 23795011, 09980050813, 09868180412 (M)",
   "email_id": "suresh.angadi@sansad.nic.in suresh.angadimp@gmail.com",
   "countries_visited": "Australia, France, Italy, Switzerland United Kingdom and United States America"
  },
  {
   "full_name": "Pralhad Venkatesh Joshi",
   "constituency": "Dharwad",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "122-D, Mayuri Estate, KeshwapurHubli-580023, KarnatakaTels(0836) 2258955, 09448283555 (M) 09448283555(M)",
   "present_address": "5, G.R.G. Road,New Delhi - 110 001Telefax. (011) 23795023, 09448283555 (M)",
   "email_id": "(i) joshi.pralhad@sansad.nic.in, (ii) pralhadvjoshi@gmail.com",
   "countries_visited": "Malaysia, Singapore, Sri Lanka and U.S.A."
  },
  {
   "full_name": "D.V. Sadananda Gowda",
   "constituency": "Bangalore North",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "15-22-1390/4 \"KAMALA\" 2nd Cross,Kankanady Bendoorwell Lower,Mangalore Dakshina Kannada -575002, Karnataka09448123249",
   "present_address": "1, Tyagraj Marg,New Delhi - 110 011Tels. (011) 23795006, 9868180269 (M)",
   "email_id": "sadananda.gawda@sansad.nic.insadanandagowda@yahoo.com"
  },
  {
   "full_name": "Gowdar Mallikarjunappa Siddeshwara",
   "constituency": "Davanagere",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "``GEM`` House, Main RoadBheemasamudra, Distt. Chitradurga - 577520, Karnataka(08194) 262017, 262022, 09448161799 (M)",
   "present_address": "2, Safadarjung Lane,New Delhi - 110 011Tel : (011) 23793703, 23793999 (R); 23062676/78, 23061593 (O) Mobile : 9868180264, 09844161799, 09717037679 Fax : (011) 23060584",
   "email_id": "gm.siddeshwara@sansad.nic.in gmsiddeshwara@gov.in",
   "countries_visited": "Widelly travelled (U.S.A., European countries & Middle East)"
  },
  {
   "full_name": "Kiren Rijiju",
   "constituency": "Arunachal West",
   "party": "Bharatiya Janata Party",
   "state": "Arunachal Pradesh",
   "permanent_address": "P.O. Nafra,</br> Distt. West KamengArunachal Pradesh-790001Tel. (0360)2292204",
   "present_address": "Andman & Nicobar Bhawan, Chanakyapuri,New Delhi - 110 021Tels. (011) 26878120,</br> 09818671114, 09818221114 (M)",
   "email_id": "kiren.rijiju@sansad.nic.in",
   "countries_visited": "Australia, Jordan, Libya, Norway, New Zealand , Pakistan, Syria, Singapore, Thailand, , Uzbekistan, U.K., U.S.A. and USSR (Now Russia), Kazakhstan, Sweden, Belgium, Japan, Korea, China, Canada, Holland, Taiwan and many more countries globally."
  },
  {
   "full_name": "H.D. Devegowda",
   "constituency": "Hassan",
   "party": "Janata Dal (Secular)",
   "state": "Karnataka",
   "permanent_address": "743, \"Amogh\" 2nd Main Road9th Cross,Padmanabha Nagar,Bangalore-560 070,Karnataka(080)26891444(Telefax)",
   "present_address": "5, Safdarjung Lane,New Delhi - 110 011Tels. (011) 23794499, 23794431 Fax. (011) 23010288",
   "email_id": "haradanahalli@yahoo.co.in",
   "countries_visited": "Widely travelled; as Minister, Chief Minister, Prime Minister and as a Member, Indian Parliamentary Delegations, Commonwealth Parliamentary Association, London"
  },
  {
  },
  {
   "full_name": "Venkateswara Rao Magantti",
   "constituency": "Eluru",
   "party": "Telugu Desam Party",
   "state": "Andhra Pradesh",
   "permanent_address": "Magantti Nilayam, Door No. 23-4-91, R.R. Peta, Eluru-534002,Distt. West Godavari, Andhra PradeshTels. (08812) 253636, 09848594545 (M)",
   "present_address": "No. 81, K.K. Birla Lane, Lodhi Estate,New Delhi-110003Mob : 09848594545",
   "email_id": "mvenkateswara.rao19@sansad.nic.in maganttibabu@gmail.com",
   "countries_visited": "Italy, Mauritius, Nepal, Singapore and U.K."
  },
  {
   "full_name": "Sushil Kumar Singh",
   "constituency": "Aurangabad",
   "party": "Bharatiya Janata Party",
   "state": "Bihar",
   "permanent_address": "Singh Kothi, Old G.T. Road, Aurangabad - 824 101, Bihar(06186) 223600, 09431223600, 09013180095, 09955888007 (M)",
   "present_address": "16 A, Ferozeshah Road,New Delhi - 110 001Tel. (011) 23354155, 9013180095 (M) Fax. (011) 23354156",
   "email_id": "(i) sushilsingh@sansad.nic.in (ii) sushilsingh.mp@gmail.com (iii) sk.singh@live.in",
   "countries_visited": "France, Nepal, Morocco, and Switzerland"
  },
  {
   "full_name": "Kirti Vardhan Singh",
   "constituency": "Gonda",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Mankapur Kot, Teh. Mankapur, Dist. Gonda,Uttar Pradesh09919442444 (M)",
   "present_address": "Ashok Hotel,</br>Chanakyapuri,New Delhi - 110 021Tel. (011) 23359554",
   "email_id": "kirtivardhan.singh@sansad.nic.in",
   "countries_visited": "Bhutan, Japan, Nepal, Thailand and U.S.A."
  },
  {
   "full_name": "Tathagata Satpathy",
   "constituency": "Dhenkanal",
   "party": "Biju Janata Dal",
   "state": "Odisha",
   "permanent_address": "107, Surya Nagar,Bhubaneswar-751003, Odisha(0647) 2536644, 09868180270, 09437009441 (M)",
   "present_address": "2, Firozshah Road,New Delhi - 110 001Tels (011) 23329821, 23329822",
   "email_id": "Education Qualifications: B.A. Educated at Sri Aurobindo International Centre of Education,Pondicherry"
  },
  {
   "full_name": "Rao Inderjit Singh",
   "constituency": "Gurgaon",
   "party": "Bharatiya Janata Party",
   "state": "Haryana",
   "permanent_address": "Rampura House,(Near B.B. Ashram)Rewari - 123401, HaryanaTel. (01274) 220044",
   "present_address": "6, Lodhi Estate, New Delhi - 110 003Telefax: (011) 24643265-66",
   "email_id": "(I) rao.inderjit@sansad.nic.in (ii) mos-planning@gov.in",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Rama Devi",
   "constituency": "Sheohar",
   "party": "Bharatiya Janata Party",
   "state": "Bihar",
   "permanent_address": "Rama Braj Bhawan, Brahmapura, Lakshmi Tola, Krishna Toli, Rama Braj Bihari Gali,Muzaffarpur-842003, BiharTels. (0621)2260164, 09431240750 (M) Telefax. (0621) 2260164",
   "present_address": "30-A, Atul Grove Road,New Delhi - 110 001Tels. (011) 23354241, 9013180124 (M) Telefax. (011) 23354241",
   "email_id": "rama.devi19@sansad.nic.in",
   "countries_visited": "Mauritius, Singapore, United Kingdom and United Arab Emirates"
  },
  {
   "full_name": "Ram Kripal Yadav",
   "constituency": "Pataliputra",
   "party": "Bharatiya Janata Party",
   "state": "Goriatoli Station Road, Patna- 800 001(Bihar)Tels. (0612)224566, 225303, 09431800966 (M)",
   "permanent_address": "18, Mother Teresa Estate, Wilmington Crescent Road,New Delhi-110 001Tels. (011) 23792555, 09431800966 (M)",
   "present_address": "Education Qualifications: B.A. (Hons.), LL.B. Educated at Magadh University, Patna (Bihar)",
   "email_id": "Member, Indian Paliamentary Delegation to China, Hong Kong, Mongolia and Thailand"
  },
  {
   "full_name": "Bhanu Pratap Singh Verma",
   "constituency": "Jalaun",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Malviya Nagar, KonchDistt. - Jalaun -285123 Uttar Pradesh",
   "present_address": "AB-18, Mathura Road, Near - Opposite Gate No. 6, Pragati MaidanNew Delhi Tels : (011) 23782620, 09013869448 (M)",
   "email_id": "bhanus@sansad.nic.in"
  },
  {
   "full_name": "Sushma Swaraj",
   "constituency": "Vidisha",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "C-7, Civil Lines, Prof. Colony,Bhopal, Madhya PradeshTels. (0755) 2661006 , 09424488888",
   "present_address": "8, Safdarjung Lane,New Delhi - 110 011Tels. (011) 23794344, 23794044 9868181930 (M)",
   "email_id": "sushmaswaraj@hotmail.com",
   "countries_visited": "Widely travelled (18 countries); <I>Member</I>, Indian ParliamentaryDelegation to Inter-Parliamentary Union Conference,Brussels, Belgium and Geneva; <I>participated in</I> Common Wealth Parliamentary Association`s Conference, Fiji; <I>attended</I> (i) SAARC Telecommunication Minister`s Conference, Dhaka; (ii) SAARC I&B Minister`s Conference, Islamabad; and (iii) SAARC Telecommunications Minister`s Conference, Colombo"
  },
  {
   "full_name": "Anirudhan Sampath",
   "constituency": "Attingal",
   "party": "Communist Party of India (Marxist)",
   "state": "4-C-15/1635, Grace Cottage, K. Anirudhan Road, P.O. Thycaud,Thiruvananthapuram - 695014, Kerala(0471) 2326571, 09447066840 (M) Fax. (0471) 2338519",
   "permanent_address": "305, V. P. House,Rafi Marg, New Delhi - 110 001Tel. 9013180340 (M)",
   "present_address": "(i) a.sampath@sansad.nic.in (ii) attingalmp@gmail.com",
   "email_id": "Education Qualifications: M.A. (Eco) LL.M (Constt. Law) Educated at Unviersity of Kerala, Kerala"
  },
  {
   "full_name": "Rayapati Sambasiva Rao",
   "constituency": "Narasaraopet",
   "party": "Telugu Desam Party",
   "state": "Andhra Pradesh",
   "permanent_address": "4th Line, LakshmipuramGuntur-522 007,Andhra Pradesh(0863)2350400,2350500, 09849061777(M),(0863)2240500(Fax)",
   "present_address": "C-1/20, Pandara ParkNew Delhi - 110 003Tels. (011) 23782602, 23388252, 09849061777 (M) Fax. (011) 23388272",
   "email_id": "sambasivaraorayapati@yahoo.co.in rsrdelhi11@gmail.com",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "N.K. Premachandran",
   "constituency": "Kollam",
   "party": "Revolutionary Socialist Party",
   "state": "Kerala",
   "permanent_address": "Maheswary Cantonment, P.O. Kollam-691001, KeralaTel : (0474) 2769922 Mob : 09400117700",
   "present_address": "Kerala House, 3, Jantarmantar Road, New Delhi-110001Tel : (011) 23362100 Mob : 09400117700",
   "email_id": "nk.premachandran@sansad.nic.in nkprem07@gmail.com",
   "countries_visited": "<b>Parliamentary delegation</b> : Australia, Cuba, Iraq, Pakistan, Philippines, Trinidad and Tobago, U.K. and U.S.A. <b>Other Occassions</b> : Bahrain, Canada, Hong Kong (Special Administrative Region of the People`s Republic of China), Kuwait, Malaysia, Maldives, Russia, Singapore, Sri Lanka, Sultanate of Oman, Thailand, Vietnam and U.A.E."
  },
  {
   "full_name": "Pinaki Misra",
   "constituency": "Puri",
   "party": "Biju Janata Dal",
   "state": "Odisha",
   "permanent_address": "12, Forest Park, Bhubaneswar - 751009Odisha(0674) 2596238, 09437033059 (M) Fax. (0674) 2596263",
   "present_address": "202, Golf Link,New Delhi - 110 003Tels: (011) 24658111, 09811078557 (M) Fax: (011) 24629807",
   "email_id": "(i) pinakimisra@hotmail.com (ii) pinakimisra@gmail.com",
   "countries_visited": "Widely travelled over 25 countries. Travelled in 2013 to Sri Lanka as part of Hon`ble Speaker`s delegation for commonwealth Parliamentary Conference. Travelled to Austria in 2013 also as part of Parliamentary delegation"
  },
  {
   "full_name": "Harinder Singh Khalsa",
   "constituency": "Fatehgarh Sahib",
   "party": "Aam Aadmi Party",
   "state": "Punjab",
   "permanent_address": "90, Kohinoor Park, P.O. Rajguru Nagar, Ludhiana - 141012, PunjabTel: (0161) 2550288, 09463268487 (M)",
   "present_address": "C-1/7, Tilak Lane,New Delhi-110001Tel: 09013869331 (M)",
   "email_id": "harinders.khalsa@sansad.nic.in</br> harsinkha@gmail.com",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Anant Kumar Dattatreya Hegde",
   "constituency": "Uttara Kannada",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "No. 17, KHB Colony, Sirsi,North Kanara - 581 401, </br>KarnatakaTel. (08384)234337, </br> Fax. (08384) 235248",
   "present_address": "13, Firozeshah Road, New Delhi - 110 001Telefax. (011) 23782001 +91-8762180337(M)",
   "email_id": "(i)anantkh@sansad.nic.in</br> (ii)mpcanara@gmail.com",
   "countries_visited": "Austria, Germany, Malaysia, Poland and Sri Lanka"
  },
  {
   "full_name": "Prem Singh Chandumajra",
   "constituency": "Anandpur Sahib",
   "party": "Shiromani Akali Dal",
   "state": "ps.chandumajra@sansad.nic.in",
   "permanent_address": "Education Qualifications: M.A. (Economics), M.A. (Political Science) Educated at P. B. University Patiala"
  },
  {
   "full_name": "Subhash Chandra Baheria",
   "constituency": "Bhilwara",
   "party": "Bharatiya Janata Party",
   "state": "Rajasthan",
   "permanent_address": "A-81, Subhash Nagar, Bhilwara-311001, RajasthanTel: (01482) 265730, 09829046344 (M) Fax: (01482)247824",
   "present_address": "Flat No. A-4, M.S. Flats, Baba Khadag Singh Marg,New Delhi-110001Tel. (011) 23324046, 0901389359 (M)",
   "email_id": "(i) subhash.baheria@sansad.nic.in (ii)baheriasc@gmail.com",
   "countries_visited": "Hong Kong, U.S.A."
  },
  {
   "full_name": "Hansraj Gangaram Ahir",
   "constituency": "Chandrapur",
   "party": "Bharatiya Janata Party",
   "state": "Gokul Ward (Bazar Ward), Chandrapur-442402</br> MaharashtraTel.(07172) 251651,</br> Fax. (07172) 254791",
   "permanent_address": "50, Ashoka Road,New Delhi - 110 001Tels. (011) 23358284, 9868180489, 09422135661 (M)",
   "present_address": "Education Qualifications: S.S.C. Educated at L.T.Y. School, Chandrapur, Maharashtra",
   "email_id": "Mauritius, South Africa and U.A.E as Member of Parliamentary Delegation"
  },
  {
   "full_name": "Virendra Singh",
   "constituency": "Bhadohi",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Village and P.O. Dokati, Distt. Ballia - 277001 Uttar PradeshTels.(05414) 224323, 09452105009 (M)",
   "present_address": "11, Windsor Place,New Delhi - 110011Tels: (011) 23782460, 23782461 09013869481 (M)",
   "email_id": "virendra.singh19@sansad.nic.in",
   "countries_visited": "Chaina in 1998"
  },
  {
   "full_name": "Swami Sakshiji Maharaj",
   "constituency": "Unnao",
   "party": "Bharatiya Janata Party",
   "state": "(i) 38, G.R.G. Road,New Delhi - 110 001Tels. (011) 23326595, 09013869777 (M) Fax. (011) 23326596",
   "permanent_address": "(i) sakshi@sansad.nic.in (ii) swamijisakshijimaharaj@gmail.com Website - (i) www.sakshimaharajgroup.com (ii) www.vabdegreecollege.com",
   "present_address": "Education Qualifications: Shastri, Acharya - M.A., Ph.D., Vidya Varidhi. Sampoornanand, Sanskrit Vishvafidyalaya, Varanari, Panjab University, Chandigarh, Maharishi Dayanand University, Rohtak, Sh. Lal Bahadur Kendriya Sanskrit Vidyapeetham, New Delhi"
  },
  {
   "full_name": "Pankaj Chaudhary",
   "constituency": "Maharajganj",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Harbans Gali, Seshpur, P.O. Geetapress, Gorakhpur-273001, Uttar PradeshTel : (0551) 2341360 Mob : 09868180565, 09415008246",
   "present_address": "Bunglow No. 20, Pt. Ravishankar Shukla Lane (Canning Lane), Ferozeshah Road,New Delhi 110001Tel : (011) 23782857 (O) Mob : 09868180565",
   "email_id": "pankajchaudharyloksabha91@gmail.com",
   "countries_visited": "Abuddhabi, Africa, Camroon, Dubai, Malaysia, Singapore, Uganda"
  },
  {
   "full_name": "Taslimuddin",
   "constituency": "Araria",
   "party": "Rashtriya Janata Dal",
   "state": "Bihar Niwas, Chanakyapuri,New Delhi-110 021",
   "permanent_address": "Education Qualifications: B.A., Maulvi",
   "present_address": "Indonesia and Malaysia; as member of High-level Committee of Government of India visited Jeddah, Mecca and Madina (Saudi Arabia) to look after the amenities of Indian Haj pilgrims; and also visited Nepal to find a solution to flood problem"
  },
  {
   "full_name": "Mekapati Rajamohan Reddy",
   "constituency": "Nellore",
   "party": "Yuvajana Sramika Rythu Congress Party",
   "state": "Plot No. 188, Road 13, Jubilee Hills,Hyderabad, TelanganaTels. (040) 23548485, 23548400",
   "permanent_address": "B-104, M.S. Flats, B.K.S. Marg,New Delhi- 110 001Tels. (011) 23766411, 23766412, 9868180561 (M)",
   "present_address": "rajamohan.reddy@sansad.nic.in",
   "email_id": "Education Qualifications: B.E. Educated at Regional Engineering College, Warangal, Telangana"
  },
  {
   "full_name": "Chhedi Paswan",
   "constituency": "Sasaram",
   "party": "Bharatiya Janata Party",
   "state": "Bihar",
   "permanent_address": "Vill. & P.O. Takiya Bazar (Sasaram), Distt. Rohtas, Sasaram-821113, BiharTelefax : (06184) 221102 Mob : 09934774400",
   "present_address": "27, Pandit. Ravi Shankar Shukla Lane (Canning Lane) New Delhi-110001Telefax : (011) 23782092 Mob : 9013869992",
   "email_id": "(i) chhedi.paswan@sansad.nic.in (ii) chhedipaswan.mp@gmail.com",
   "countries_visited": "Attended 13th International Youth and Olympia festival at Pyongyang, D.P.K. (North Korea)"
  },
  {
   "full_name": "Kuruppassery Varkey Thomas",
   "constituency": "Ernakulam",
   "party": "Indian National Congress",
   "state": "Kerala",
   "permanent_address": "Prof. K.V. Thomas Road, Thoppumpady,Kochi - 682 005 Kerala(0484) 2232530, 09847077150 (M) Fax. (0484) 2235541",
   "present_address": "17, B. R. Mehta Lane,New Delhi - 110 001Tels. (011) 23070884, 23070885 (R), 9013180212 (M) Fax. (011) 23070846 (R)",
   "email_id": "(i) thomaskv@sansad.nic.in (ii) prof.kvthomas2014@gmail.com",
   "countries_visited": "China, England, France, Germany, Hong Kong, Indonesia, Italy, Japan, Kuwait, Malaysia, Nepal, Oman, Philippines, Portugal, Quatr, Rome, Saudi Arabia Singapore, Sri Lanka, South Korea, Taiwan, U. A. E. Vietnam and Yugoslavia"
  },
  {
   "full_name": "M. Thambi Durai",
   "constituency": "Karur",
   "party": "All India Anna Dravida Munnetra Kazhagam",
   "state": "21-D, Kumarasamy Apartments,Ramanujam Nagar, Kouai Road, Karur-639001, Tamil Nadu",
   "permanent_address": "Tamil Nadu Bhawan (old), 6, Kautilya Marg, ChanakyapuriNew Delhi - 110 021",
   "present_address": "Education Qualifications: M.A., M.Phil., M.Litt., Ph.D. (Economics) Educated at Madras Christian College, Madras University,Chennai,Tamil Nadu",
   "email_id": "Widely travelled (11 countries); Leader, IndianParliamentary Delegation to Mauritius, 1987; and DeputyLeader, Indian Parliamentary Delegation to Canada"
  },
  {
   "full_name": "Ramachandran Mullappally",
   "constituency": "Vadakara",
   "party": "Indian National Congress",
   "state": "Kerala",
   "permanent_address": "\"Ravi\", P.O. Chombala,Distt. Calicut - 673308 KeralaTel. (0496) 2502345",
   "present_address": "1-A, Sunheri Bagh Lane,New Delhi - 110 011Tel: (011) 23063102, 09968691122 (M)",
   "email_id": "mullappally.ramachandran@gmail.com",
   "countries_visited": "Cuba, Hong Kong, Indonesia, Mosambique, Singapore, South Africa, South Korea, and former U.S.S.R."
  },
  {
   "full_name": "Ashok Shankarrao Chavan",
   "constituency": "Nanded",
   "party": "Indian National Congress",
   "state": "Maharashtra",
   "permanent_address": "1-2-163, Anand Nilayam, Shivaji Nagar, Distt. Nanded- 431602Maharashtra Tele: (02462)234081, 09821527561 (M) Fax: (02462) 237732",
   "present_address": "4, South Avenue Lane,New Delhi-110011Tele: (011) 23794763, 09821527561 (M)",
   "email_id": "asho.shankarrao@sansad.nic.in ashokchavan009@gmail.com",
   "countries_visited": "Australia, China, Egypt, France, Hongkong, Malaysia, Nepal, Singapore, U.K., U.S.A., U.S.S.R."
  },
  {
   "full_name": "Shibu Soren",
   "constituency": "Dumka",
   "party": "Jharkhand Mukti Morcha",
   "state": "14, Sector 1-C, P.O. Ram Mandir,</br> Bokaro Steel City Thana, Bokaro, Jharkhand-827001Tels. (011) 23093857, 23093861, 09431130383, 09631472197 (M)",
   "permanent_address": "224, North Avenue,New Delhi - 110 001Tels. (011) 23093857, 23093861",
   "present_address": "shisoren@sansad.nic.in",
   "email_id": "Education Qualifications: Matriculate Educated at Gola High School, Hazaribagh, Jharkhand"
  },
  {
   "full_name": "Dileep Singh Bhuria",
   "constituency": "Ratlam",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "Vill. and P.O.- Machhalia, Teh. Jhabua,Distt. - Jhabua, Madhya PradeshTels. (073921) 82230, 43310, 09810110764 (M)",
   "present_address": "12, Dr. B.D. MargNew Delhi Tel: (011) 45710572, 09810110764 (M)",
   "email_id": "dileepsingh.bhuria@sansad.nic.in",
   "countries_visited": "Indonesia, Singapore, North Korea, Chaina, France and U.S.A. etc."
  },
  {
   "full_name": "Amarinder Singh",
   "constituency": "Amritsar",
   "party": "Indian National Congress",
   "state": "110, Ground Floor, Sundar Nagar,New Delhi-1100039811399777 (M)",
   "permanent_address": "amarinder.singh@sansad.nic.in",
   "present_address": "Education Qualifications: Graduate Educated at Lawrence School, Sanawar; The Doon School, Dehra Dun; The National Defence Academy, Kharakvasala and the Indian Military Academy, Dehra Dun",
   "email_id": "Belgium, France, Holland, Iran, Italy, Pakistan, Poland, Switzerland, Turkey, U.K. and West Germany"
  },
  {
   "full_name": "Nandi Yellaiah",
   "constituency": "Nagarkurnool",
   "party": "Indian National Congress"
  },
  {
   "full_name": "Saugata Roy",
   "constituency": "Dum Dum",
   "party": "All India Trinamool Congress",
   "state": "West Bengal",
   "permanent_address": "162/D 593, Lake Gardens, Kolkata - 700 045,</br> West BengalTels. (011)24224650, 24220772,</br> 09830031220 (M)</br>Fax. (011) 24224181",
   "present_address": "58, Lodhi Estate,New Delhi- 110 003Tels. (011) 23329730, 9013180175 (M)",
   "email_id": "saugatapolitics_roy@yahoo.co.in",
   "countries_visited": "Belarus, Brazil, Colombia, Egypt, Finland, Indonesia, Israel, Japan, Jordan, Mexico, Myanmar, Pakistan, Poland, Singapore, Thailand, U.S.A. and U.S.S.R."
  },
  {
   "full_name": "Biren Singh Engti",
   "constituency": "Autonomous District",
   "party": "Indian National Congress",
   "state": "Assam",
   "permanent_address": "Vill. Rongmongwe, ITI Colony, Ward No. 5, P.O. & P.S. Diphu,Distt. Karbi Anglong - 782 460, AssamTels. (03671) 272345, 09868180389 (M) Telefax. (011) 23782380",
   "present_address": "17, Windsor Place, Ferozsha Road,New Delhi - 110 001Tels. (011) 23782380, 9868180389 (M) Telefax. (011) 23782380",
   "email_id": "birens.engti@sansad.nic.in shisude@yahoo.com",
   "countries_visited": "France, Poland, U.K., U.S.A. and U.S.S.R."
  },
  {
   "full_name": "Rajesh Ranjan (Pappu Yadav)",
   "constituency": "Madhepura",
   "party": "Rashtriya Janata Dal",
   "state": "Bihar",
   "permanent_address": "Ranjan Niketan, Court Station Road,Distt. Purnia-854303, Bihar(06454)227479,227922",
   "present_address": "67-68/Z Block, West Patel Nagar,New Delhi.",
   "email_id": "pappu.yadav@sansad.nic.in, rajesh.ranjan19@sansad.nic.in"
  },
  {
   "full_name": "Mulayam Singh Yadav",
   "constituency": "Azamgarh",
   "party": "Samajwadi Party",
   "state": "Post-Saifai, Janpad,Itawa-226001, Uttar PradeshTels. (0522) 2235477, 2235454, 09415103070 (M)",
   "permanent_address": "16, Ashoka Road,New Delhi - 110 001Tels. (011) 23736300,</br> 9971820100, 9013180789 (M)",
   "present_address": "mulayamsingh.yadav@sansad.nic.in",
   "email_id": "Education Qualifications: B.A., B.T., M.A. (Political Science) Educated at K.K. College, Etawah, A.K. College, Shikohabad and B.R. College, Agra University, Agra, Uttar Pradesh"
  },
  {
   "full_name": "Hukmdev Narayan Yadav",
   "constituency": "Madhubani",
   "party": "Bharatiya Janata Party",
   "state": "Vill. & P.O. Bijuly,Distt. Darbhanga, BiharTels. (06272) 245094 09431220044 (M)",
   "permanent_address": "4, Dr. Bishwambhar Das Marg,New Delhi - 110 001Tels. (011) 23753885, 9013180264, 9810031003 (M)",
   "present_address": "hukum@sansad.nic.in",
   "email_id": "Education Qualifications: Graduate, Educated at Chandradhari Mithila College, Darbhanga, Bihar"
  },
  {
   "full_name": "Chintaman Navsha Wanaga",
   "constituency": "Palghar",
   "party": "Bharatiya Janata Party",
   "state": "At. Kawada, PO & Teh. Talasari,Distt. Thane-400602, MaharashtraTels. (02521) 691736",
   "permanent_address": "5, Ferozeshah RoadNew Delhi",
   "present_address": "cn.wanaga@sansad.nic.in",
   "email_id": "Education Qualifications: B.A. (Hons.), LL.B. Educated at Bombay University, Mumbai (Maharashtra)"
  },
  {
   "full_name": "Virendra Kumar",
   "constituency": "Tikamgarh",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "Ramayani, Nandishwar Colony,</br> Civil Line, Teekamgarh-472001, Madhya PradeshTels. (07683) 246100, 09868180450 (M)",
   "present_address": "22, Mahadev Road,New Delhi - 110001Tel : (011) 23355600, 23719498</br> Mob : 9868180450, 9868180409",
   "email_id": "vkumar@sansad.nic.in",
   "countries_visited": "Australia, China, Mangolia and Thailand"
  },
  {
   "full_name": "Rajesh Verma",
   "constituency": "Sitapur",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Town & Post-Tambaur, Distt. Sitapur, Uttar PradeshTelefax. (05862) 257352, 09415117777 (M)",
   "present_address": "6, Windsor Place, Opposite Hotel Le MeridianNew Delhi - 110 001Tels. (011) 23320140 , 09013869433 (M)",
   "email_id": "(i) verma.rajesh@sansad.nic.in (ii) suneetkverma@yahoo.co.in"
  },
  {
   "full_name": "Mansukhbhai Dhanjibhai Vasava",
   "constituency": "Bharuch",
   "party": "Bharatiya Janata Party",
   "state": "Gujarat",
   "permanent_address": "Rajendra Nagar Society, Rajpipla, Jalaram Road,Distt. Narmada, GujaratTels.(02640)224300,09868180050 (M)",
   "present_address": "10, Pt. Pant Marg,New Delhi - 110 001Tels. (011) 23314017, 23324017 9868180050 (M)",
   "email_id": "md.vasava@sansad.nic.in"
  },
  {
   "full_name": "Uma Bharati Sushree",
   "constituency": "Jhansi",
   "party": "Bharatiya Janata Party",
   "state": "uma.bharati@sansad.nic.in",
   "permanent_address": "Education Qualifications: 6th Standard",
   "present_address": "Widely travelled"
  },
  {
   "full_name": "Suresh Kodikunnil",
   "constituency": "Mavelikkara",
   "party": "Indian National Congress",
   "state": "Kerala",
   "permanent_address": "School View, Kizhakekara, P.O.Kottarakara, Distt. Kollam, KeralaTelefax. (0474) 2454000 09447145400(M)",
   "present_address": "24, G.R.G. Road,New Delhi - 110 001Tels.(011) 23359009 09013180580 (M) Fax. (011) 23753787",
   "email_id": "(i) kodikunnil.suresh@sansad.nic.in (ii) kodikunnilsuresh@yahoo.com",
   "countries_visited": "Australia, Bahrain, China, France, Germany, Ireland, Japan, Kuwait, Kazakhstan, Malaysia, Qatar, Saudi Arabia, South Korea, Switzerland, U.A.E., U.K. and U.S.A."
  },
  {
   "full_name": "Dr. Kirit Somaiya",
   "constituency": "Mumbai-North-East",
   "party": "Bharatiya Janata Party",
   "state": "Maharashtra",
   "permanent_address": "Neelam Nagar, Mulund (E), Mumbai- 400081, MaharashtraTels : (022) 21634152, 21630696",
   "present_address": "203, South Avenue,New Delhi - 110011Tel : (011) 23794676, 23015513",
   "email_id": "kiritbjp@gmail.com kiritsomaiya@gmail.com"
  },
  {
   "full_name": "Manoj Kumar Sinha",
   "constituency": "Ghazipur",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Vill.-Mohanpura, P.O.-Basudeepar, Distt. Gazipur, Uttar PradeshTels. 09839879958, 09415209958 (M)",
   "present_address": "Room No. 245,</br> Rail Bhawan,New Delhi - 110001(011) 23382323",
   "email_id": "manojsinha.mp@sansad.nic.in"
  },
  {
   "full_name": "Radha Mohan Singh",
   "constituency": "Purvi Champaran",
   "party": "Bharatiya Janata Party",
   "state": "Gandhi Complex, Station Road, Motihari,Distt. East Champaran-845401, BiharTels. (06252) 241210, 09431815551 (M)",
   "permanent_address": "94-96, North Avenue,New Delhi - 110 001Tels. (011) 23092025, 23093225, 9013180251 (M) Fax. (011) 23093225",
   "present_address": "rmsingh@sansad.nic.in",
   "email_id": "Education Qualifications: B.A. Educated at M.S. College, Bihar University, Motihari, Bihar"
  },
  {
   "full_name": "Brijbhushan Sharan Singh",
   "constituency": "Kaiserganj",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Vill. & P.O. Bishnoherpur,</br>Shakti Bhawan, Nawabganj,<br/> Distt. Gonda-208002,</br> Uttar PradeshTels. (05260) 274216, 09415109000 (M)",
   "present_address": "21, Ashoka Road New Delhi - 110001Tels. (011) 23346289, 9868180054 (M) Fax : (011) 23346289",
   "email_id": "brijbhusan.singh@sansad.nic.in bjp2014kaisherganj@gmail.com",
   "countries_visited": "Kazakhstan, Korea, Russia, Singapore, Scotland, Thailand and U.K."
  },
  {
   "full_name": "Bahadur Singh Koli",
   "constituency": "Bharatpur",
   "party": "Bharatiya Janata Party",
   "state": "Rajasthan",
   "permanent_address": "Gandhi Nagar, Sevar Road,Bharatpur-321001, RajasthanTel: (05644) 260451, 09414315320 (M)",
   "present_address": "C-1/20, Humayun Road, New Delhi Tel: (011) 24656525, 09013869345 (M)",
   "email_id": "mpbskoli@gmail.com, bahadurs@sansad.nic.in"
  },
  {
   "full_name": "Shanta Kumar",
   "constituency": "Kangra",
   "party": "Bharatiya Janata Party",
   "state": "Himachal Pradesh",
   "permanent_address": "Yamini Parisar, Palampur,Distt. Kangra, Himachal PradeshTel: (01894) 23063009418030630 (M) Fax: (01894) 232588",
   "present_address": "23, Ashoka Road,New Delhi - 110011Tels:(011) 23745003, 23745005 Fax (011) 23745008",
   "email_id": "shanta.kumar@sansad.nic.in skyamini@gmail.com",
   "countries_visited": "Pakistan and U.S.A. - for treatment only"
  },
  {
   "full_name": "Arjun Charan Sethi",
   "constituency": "Bhadrak",
   "party": "Biju Janata Dal",
   "state": "Odisha",
   "permanent_address": "P.O. Odang, Via Randhiahat,Distt. Bhadrak - 756 135, Odisha09868180238 (M)",
   "present_address": "21, Canning Lane,New Delhi - 110 001Tels. (011) 23782760, 23782745 9868180238 (M)",
   "email_id": "ac.sethi@sansad.nic.in, nama.kmm@gmail.com",
   "countries_visited": "<I>Leader</I>, Indian Delegation to (i) 34th Meeting of the Indo-Bangladesh Joint Rivers Commission (JRC), Dhaka, Bangladesh; (ii) International Conference on Fresh Water, 3 and 4 December 2001, Bonn, Germany; (iii) Meeting to discuss matters of Mutual Benefit in the interests of Advancing the Bilateral Relation in the Area of Water Resources Management, Sydney, Australia, April 2002; (iv) Third World Water Forum, Shiga, Osaka and Kyoto, Japan, March 2003; (v) 13th Stockholm Water Symposium and 8th Annual Meeting of Consulting Partnership of the Global Water Partnership, Stockholm, Sweden, August 2003; and (vi) 35th Meeting of the Indo-Bangladesh Joint Rivers Commission (JRC), New Delhi, 2003; <I>Member</I> (i)Indian Parliamentary Delegation to 63rd Inter-Parliamentary Conference, Madrid, Spain, 1976; and (ii) Indian Delegaton to UNO General Assembly, New York, December 2008"
  },
  {
   "full_name": "Purno Agitok Sangma",
   "constituency": "Tura",
   "party": "National Peoples Party",
   "state": "Meghalaya",
   "permanent_address": "Walbakgiri, P.O. Tura,Distt. West Garo Hills, Meghalaya03651) 232825, 09818003422 (M)",
   "present_address": "34, Aurangzeb Road,New Delhi - 110 011Tels. (011) 23010123, 23013651, Telefax. (011) 23013651",
   "email_id": "pasangma@sansad.nic.in",
   "countries_visited": "Widely travelled; Leader, Indian Delegation to (i) U.N.I.D.O. Conference, Khartoum, Sudan, 1981; (ii) ESCAP Conference, Bangkok, Thailand, 1984; (iii) International Labour Conference organised by I.L.O., six times; and (iv) Conference of Asia Pacific Labour Ministers (C.A.P.L.M.) at Tehran, Iran, 1993; Leader, Inter Parliamentary Delegation, to (i) 42nd CPA Conference, Kuala Lumpur, 1996; (ii) 96th IPU Conference, Beijing, China, 1996; and also led bilateral Parliamentary Delegations to Australia, Croatia, DPR Korea, Finland, Mongolia, Norway, Russia, Saudi Arabia, Sweden, and U.K.; Leader, Indian Parliamentary Delegation to Bulgaria, Mongolia and Thailand, 1997; a member of Commonwealth observer to Zimbabwe Parliamentary Election; Leader of the Commonwealth observer for Presidential Election in Gambia"
  },
  {
   "full_name": "Vishnu Deo Sai",
   "constituency": "Raigarh",
   "party": "Bharatiya Janata Party",
   "state": "Chhattisgarh",
   "permanent_address": "Vill. Bagia, P.O. Bandar Chuan, BagichaDistt. Jashpur-496331, Chhatishgarh(07764) 254252, 09425251933 (M)",
   "present_address": "70, North Avenue,New Delhi - 110 001Tel. (011) 23092402 9868180143, 0945251933 (M)",
   "email_id": "vishnudeo.sai@sansad.nic.in"
  },
  {
   "full_name": "Rajiv Pratap Rudy",
   "constituency": "Saran",
   "party": "Bharatiya Janata Party",
   "state": "3,Shivnandan Bhawan, Boring Road,Patna-800001,BiharTels: 09868252153(M)",
   "permanent_address": "AB-97, Shahjahan Road,New Delhi - 110003Tels: (011) 23070999, 23070300",
   "present_address": "rudypr@sansad.nic.in",
   "email_id": "Education Qualifications: B.A. (Hons.) (Eco.), M.A. (Eco.), LL.B. Educated at St. Michaels High School, Patna (Bihar), and College and University, Panjab University, Chandigarh"
  },
  {
   "full_name": "A.P. Jithender Reddy",
   "constituency": "Mahabubnagar",
   "party": "Telangana Rashtra Samithi",
   "state": "Telangana",
   "permanent_address": "8-6-210/3 Padmavathi Colony, Mahbubnagar-509001, TelanganaMob : 09848030036, 09440630036",
   "present_address": "Room No. 1304,</br> Ashoka Hotel,New Delhi - 110021",
   "email_id": "jreddy@sansad.nic.in jrinfra@gmail.com",
   "countries_visited": "Widely traveled"
  },
  {
   "full_name": "Sukender Reddy Gutha",
   "constituency": "Nalgonda",
   "party": "Indian National Congress",
   "state": "Telangana",
   "permanent_address": "Flat No. 601, Anvith Avenue, Road No. 16,Himayatnnagar, Hyderabad, TelanganaTelefax. (040) 23223399 09493037016(M)",
   "present_address": "47, Lodhi Estate,New Delhi - 110 003.Tels. (011) 24692221 09212219137, 09013180567 (M)",
   "email_id": "gutha.loksabha@gmail.com",
   "countries_visited": "Australia, Egypt, France, Israel, U.K. and U.S.A."
  },
  {
   "full_name": "Bishnu Pada Ray",
   "constituency": "Andaman and Nicobar Islands",
   "party": "Bharatiya Janata Party",
   "state": "26, North Avenue,New Delhi - 110 001Tels. (011) 23093092 09013180198 (M) Fax: (011) 23093095",
   "permanent_address": "andamanmp@gmail.com",
   "present_address": "Education Qualifications: B.Com. (Hons.) Educated at Anand Mohan College, Kolkata, West Bengal"
  },
  {
   "full_name": "Ramsinh Patalyabhai Rathwa",
   "constituency": "Chhota Udaipur",
   "party": "Bharatiya Janata Party",
   "state": "Gujarat",
   "permanent_address": "(i) 192 B, Amit Nagar Society, VIP RoadKarelibaug, Vadodara,Gujarat-390018(0265)2484111, 09909014490(M),(0265)2492558(Fax)",
   "present_address": "48 - 50, South Avenue,New Delhi - 110 011Tels. (011) 23010144, 9013180464 (M) Fax: (011)23010144",
   "email_id": "(i) ramsinh.rathwa@sansad.nic.in (ii) ramsinhrathwa@yahoo.co.in",
   "countries_visited": "Denmark, Egypt, Hong Kong, Israel, Italy, Japan (as a member of Parliamentary Delegation), South Korea, Singapore and Thailand"
  },
  {
   "full_name": "Pon Radhakrishnan",
   "constituency": "Kanniyakumari",
   "party": "Bharatiya Janata Party",
   "state": "16, Talkatora Road,New Delhi - 110011Tels. (011) 23320154, 23323539",
   "permanent_address": "ponrk@sansad.nic.in",
   "present_address": "Education Qualifications: B.A., B.L. Educated at D.V.D.H. School, Nagercoil, V.H.N.S.N. College, Virudhu Nagar and Madras Law College, Chennai (Tamil Nadu)",
   "email_id": "Mauritius"
  },
  {
   "full_name": "Raosaheb Patil Danve",
   "constituency": "Jalna",
   "party": "Bharatiya Janata Party",
   "state": "Maharashtra",
   "permanent_address": "At. & P.O., Bhokardan,Jalna - 431114, MaharashtraTels. (02485) 240125, 240555 09868180280(M)",
   "present_address": "8, Ashoka Road,New Delhi - 110 001Tels. (011) 23092302, 9868180280(M)",
   "email_id": "raosaheb.danve@sansad.nic.in"
  },
  {
   "full_name": "Prahlad Singh Patel",
   "constituency": "Damoh",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "F-23, Sainik Society, Shakti Nagar, Jabalpur-482002, Madhya PradeshTel : (0761) 2426670 Mob : 09425155511, 08354455511",
   "present_address": "14, Dr. B. D. Marg,New Delhi - 110001Tel : (011) 23320121",
   "email_id": "prahladp@sansad.nic.in"
  },
  {
   "full_name": "Prasanna Kumar Patasani",
   "constituency": "Bhubaneswar",
   "party": "Biju Janata Dal",
   "state": "P.O.Balugaon, Distt.KhurshaOdishaTels. (06756) 20034",
   "permanent_address": "11, Mahadev Road,New Delhi - 110 001Tels. (011) 23717559 9873235020, 9868180271 (M)",
   "present_address": "prasanna.patasani@sansad.nic.in",
   "email_id": "Education Qualifications: M.A., LL.B., M.S.C.I., F.I.M.A. Ph.D, D. Litt.(Utkal), D.Sc.(Swiss)D.Litt. (South Africa) Educated at Utkal University, Bhubaneswar, Madhusudan Law College, Cuttack, Orissa, Maharshi Institute of Creative Intelligence, Rishikesh, Uttar Pradesh, Sheelsburg, Switzerland"
  },
  {
   "full_name": "Ramchandra Paswan",
   "constituency": "Samastipur",
   "party": "Lok Jan Shakti Party",
   "state": "Bihar",
   "permanent_address": "Mantri ji Tola, Vill. P.O. Saharbanni, P.S. + AllauliDistt. Khagaria - 851 2004 (Bihar)",
   "present_address": "41, South Avenue,New Delhi - 110 001",
   "email_id": "ramchandra.paswan@sansad.nic.in"
  },
  {
   "full_name": "Ram Vilas Paswan",
   "constituency": "Hajipur",
   "party": "Lok Jan Shakti Party",
   "state": "Vill. & P.O. Shaharbanni,</br> Thana - Bellahi,Distt. Khagaria-851204, BiharTels. (011) 23015249, 23017681",
   "permanent_address": "12, Janpath,New Delhi - 110 001Tel. (011) 23017681, 23015249 (R), 23386364, 23386519, 23062345, 23063586, 23018301 (O) </br> Fax: (011) 23017681 (R), 23384020, 23061477 (O)",
   "present_address": "Education Qualifications: M.A., B.L. Educated at Kosi College, Khagaria and Patna University, Patna (Bihar)",
   "email_id": "Widely travelled"
  },
  {
   "full_name": "Dalpat Singh Paraste",
   "constituency": "Shahdol",
   "party": "Bharatiya Janata Party",
   "state": "Ashoka Hotel, Chanakyapuri,New Delhi-110021.",
   "permanent_address": "dalpat.paraste@sansad.nic.in",
   "present_address": "Education Qualifications: B.A.. LL.B"
  },
  {
   "full_name": "Ravindra Kumar Pandey",
   "constituency": "Giridih",
   "party": "Bharatiya Janata Party",
   "state": "Jharkhand",
   "permanent_address": "Phusro Bazar,Bermo,Distt. Bokaro-829144,JharkhandTel : (06549) 220727, 09431127999 (M)</br> Fax : (06549) 220727",
   "present_address": "B-2, Block A, M.S. Flats, B.K.S. Marg,New Delhi - 110001Tel : (011) 23357211, 09013180163 (M)",
   "email_id": "rkpandey@sansad.nic.in",
   "countries_visited": "South Africa"
  },
  {
   "full_name": "Jual Oram",
   "constituency": "Sundargarh",
   "party": "Bharatiya Janata Party",
   "state": "Odisha",
   "permanent_address": "At Kendudihi, P.O. Kalaiposh, Via-Lahunipara,Distt. Sundargarh - 770 040,Odisha(0661)2643766,(06625)232215,(06622)275037",
   "present_address": "Room No. 107,</br> Odisha Bhawan,</br>Bardoloi Marg,</br>Chanakyapuri,New Delhi - 110 021",
   "email_id": "jualoram@sansad.nic.in"
  },
  {
   "full_name": "Shripad Yesso Naik",
   "constituency": "North Goa",
   "party": "Bharatiya Janata Party",
   "state": "Goa",
   "permanent_address": "Vijayshree, 111, St. Pedro-Old Goa,P.O. Velhagoa - 403 402 Goa(0832) 2444510, 09822122440 (M) Fax. (0832) 2444088",
   "present_address": "1, Lodhi Estate,New Delhi - 110 003Tel. (011) 24635396, 9868180630 (M)",
   "email_id": "sripadnaik@sansad.nic.in",
   "countries_visited": "Brazil, France, Geneva, Switzerland, Thailand, U.K. and U.S.A."
  },
  {
   "full_name": "K.H. Muniyappa",
   "constituency": "Kolar",
   "party": "Indian National Congress",
   "state": "Karnataka",
   "permanent_address": "100/B, 60 Feet Road, Layout, BhoopasandraSanjay Nagar, Bengaluru-560094, Karnataka.(080) 23415733, 23415755",
   "present_address": "7, Tyagraj Marg,New Delhi - 110 011Tels. (011) 23792703 (011)23061566, 23061739 (O) 23381634, 9868180808 (M) Telefax. (011) 23794481 (R) Fax: (011) 23063141 (O)",
   "email_id": "khmuni@sansad.nic.in",
   "countries_visited": "Member, Indian Parliamentary Delegation led by the Honble Speaker, Shri G.M.C. Balayogi, to Russia, 1998"
  },
  {
   "full_name": "Kariya Munda",
   "constituency": "Khunti",
   "party": "Bharatiya Janata Party",
   "state": "Jharkhand",
   "permanent_address": "Vill. & P.O. Anigara, Chandidih, P.S. Khunti,Distt. Khunti, Jharkhand09431108665 (M)",
   "present_address": "1, Sunehari Bagh Road,New Delhi - 110 001Tels. (011) 23012914 9971148222, 9871741133 (M) Telefax. (011) 23792050",
   "email_id": "kariya.munda@sansad.nic.in",
   "countries_visited": "China, France, London, Nepal, North Korea, Singapore, Thailand, U.A.E. and U.S.A."
  },
  {
   "full_name": "Bhartruhari Mahtab",
   "constituency": "Cuttack",
   "party": "Biju Janata Dal",
   "state": "Odisha",
   "permanent_address": "Beharibag, Chandni Chowk,Cuttack - 753 002, OdishaTel : (0671) 2507568, 2508003 Mob : 09437228455 Fax : (0671) 2508001",
   "present_address": "AB-94, Shahjahan Road,New Delhi - 110 011Tel : (011) 23782589, 23782742 Mob : 9868180308 Fax : 23070179",
   "email_id": "bhartruhari.mahatab@gmail.com",
   "countries_visited": "Widely travelled; attended UN Summits at Copenhagen in Denmark and Rome in Italy; and 50th Anniversary of UN at New York in U.S.A.; visited U.S.A. through USIS; accompanied Prime Minister during his visit to Iran, Russia, Senegal, Tunisia and Venezuela; attended IXth and XIth NAM Conferences at Belgrade in Yugoslavia in 1989 and Cartegena in Columbia in 1995; and attended 52nd UNGA (United Nations General Assembly) in October 1998 as unofficial Member for two weeks representing Indian Mission in U.N.; visited Mexico as Member of Indian Parliamentary Delegation in May 2001; attended special session of UN for Children, as a member of Indian Parliamentary Delegation in May 2002; also attended 56th, 57th and 58th UN General Assembly as an unofficial delegate for two weeks representing Indian Mission in United Nations in October 2002, October 2003 and November 2004 respectively; participated in Commonwealth Parliamentary Union Workshop on \"Right to Information\" at Ghana in July 2004; attended CPU at Fiji in Sept. 2007 as Indian Parliamentary Delegate; and attended IPU in Zeneva, Sept. 2008 as Indian Delegate; attended the 64th UNGA as an unofficial Indian delegate representing Indian Mission in United Nations; in Oct. 2009; led Indian Parliamentary Delegation to Dhaka to attend CPU-World Bank Institute sponsored Role of Public Accounts Committee in SAARC Countries in Nov. 2009; attended Climate Change Summit as Indian Delegate at Copenhagen in Dec. 2009. Member Delegate to France, Switzerland in 2010. Member Delegate to Japan in 2011. Member Delegate to Newzealand on Goodwill Mission in 2012 with Hon`ble Speaker, Lok Sabha. Member Parliamentary Delegate to Australia, 2013. Led Indian Parliamentary Team to London to attend Commonwealth Countries` Oversight Committee workshop in 2013. Member Delegate to Turkmenistan, Armenia on Goodwill Mission in 2014. Member Delegate to Vietnam with Hon`ble President of India 2014. Led Indian Parliamentary Delegation to WTO Conference, Geneva, 2015"
  },
  {
   "full_name": "Sumitra Mahajan (Tai)",
   "constituency": "Indore",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "68, Manishpuri, Saket Nagar,Indore-452 018, Madhya PradeshTels.Indore: (0731) 2596655 (R) 2542211/2542233 (O)",
   "present_address": "20, Akbar Road,New Delhi - 110 001Tels. (011) 23014011,23014022",
   "email_id": "speakerloksabha@sansad.nic.in s_mahajan@nic.in",
   "countries_visited": "-Travelled widely across all over the globle. The countries visited by her include Australia, Canada, China, France, Indonesia, Maldives, Morocco,Philippines, Sri Lanka, South Africa, Switzerland, UK, USA etc."
  },
  {
   "full_name": "Arun Kumar",
   "constituency": "Jahanabad",
   "party": "Rashtriya Lok Samta Party",
   "state": "Bihar",
   "permanent_address": "Brij Indu Kunj, Ashiyana Mor, Near New Passport Office, Patna, BiharTel: (0612) 2581448, 09934618518 (M)",
   "present_address": "171-172, South Avenue,New Delhi - 110011Tels: (011) 23018575, 23018584 09868180699",
   "email_id": "dr.arunkumar@sansad.nic.in drarunkumarjahanabad@gmail.com",
   "countries_visited": "England, Myanmar, Thailand and United States of America"
  },
  {
   "full_name": "Faggan Singh Kulaste",
   "constituency": "Mandla",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "Village - Jewara, P.O. - Dewari Kala (Bablia),</br> Tehsil - Niwas, District - Mandla - 481 661 Madhya PradeshTels. (07641) 271350, 9425163775 (M)",
   "present_address": "13-AB, Mathura Road, New Delhi - 110 044Tels. (011) 23782536, 9868180495, Fax (011) 23782540",
   "email_id": "(i) fskulaste@sansad.nic.in (ii) fskulaste@yahoo.com (iii) fskulaste@gmail.com Website - www.fskulaste.in",
   "countries_visited": "Nepal and U.K."
  },
  {
   "full_name": "Vinod Khanna",
   "constituency": "Gurdaspur",
   "party": "Bharatiya Janata Party",
   "state": "13-C, I.L. Palazzo, Little Gibbs Road, Mumbai-400006, MaharashtraTels. (022)23612666, 9464610004 (M), Telefax: (022) 23633053",
   "permanent_address": "Punjab Bhawan, Copernicus Marg,New Delhi - 110001",
   "present_address": "vkhanna@sansad.nic.in vinodkhanna108@gmail.com",
   "email_id": "Education Qualifications: Under Graduate Educated at St. Xavier High School, Mumbai, Delhi Public School, Delhi, Lord Barnes High School, Devlali and Sydenham College, Mumbai (Maharashtra)"
  },
  {
   "full_name": "Bhuwan Chandra AVSM (Retd.) Khanduri",
   "constituency": "Garhwal",
   "party": "Bharatiya Janata Party",
   "state": "Uttarakhand",
   "permanent_address": "Jai Durga Niwas, 12, Vikas Marg,Pauri Garhwal-246 001, UttarakhandTel. (01368) 222600",
   "present_address": "7, K. Kamraj Lane,New Delhi - 110 011Tels. (011) 23794554, 23794555, 23016415",
   "email_id": "bc.khanduri@nic.in",
   "countries_visited": "Austria, France, Germany, Holland, Japan, Malaysia, Switzerland, Thailand, U.K., U.S.A. and Vietnam"
  },
  {
   "full_name": "Chandrakant Bhaurao Khaire",
   "constituency": "Aurangabad",
   "party": "Shiv Sena",
   "state": "Maharashtra",
   "permanent_address": "`Khaire Niwas`, Swatantra Sainik Bhaurao Bhaguji Khaire Marg,Machali Khadak, Sambhaji Nagar, Aurangabad - 431 001, MaharashtraTel : (0240) 2331125, 2331225 Fax : (0240) 2331225",
   "present_address": "2, Teen Murti Lane,New Delhi - 110011Tel : (011) 23018525 Telefax : (011) 23013525",
   "email_id": "bk.chandrakant@sansad.nic.in cbkhaire@gmail.com",
   "countries_visited": "Bulgaria, Egypt, Hungary, Japan, Nepal, Romania, South Africa and U.S.A."
  },
  {
   "full_name": "Rattan Lal Kataria",
   "constituency": "Ambala",
   "party": "Bharatiya Janata Party",
   "state": "Haryana",
   "permanent_address": "352, MDC-4, Panchkula, Haryana(01722) 555352, 09416499855 (M)",
   "present_address": "Haryana Bhawan, Copernicus Marg, New Delhi - 110001",
   "email_id": "ratanlal.kataria@sansad.nic.in",
   "countries_visited": "Australia, Hong Kong, Japan, Singapore, Thailand, UAE, U.K. U.S.A."
  },
  {
   "full_name": "Kamal Nath",
   "constituency": "Chhindwara",
   "party": "Indian National Congress",
   "state": "Madhya Pradesh",
   "permanent_address": "Vill. Shikarpur, P.O. Linga,Distt. Chhindwara - 480 001, Madhya PradeshTelefax.(07162) 242233",
   "present_address": "1, Tuglak Road,New Delhi - 110 011Tels. (011) 23792233, 23792234 Fax: (011) 23793396",
   "email_id": "knshikarpur@gmail.com",
   "countries_visited": "Widely travelled <I>Member</I> (i) Indian Delegation to U.N., 1982, 1983; (ii) NAM Summit, 1983; (iii) I.P.U. Conferences, Nicaragua, 1987, Guatemala, 1988 and Cyprus, 1990; <I>Member Indian Parliamentary Delegation</I> to (i) Tokyo, 1989; (ii) Cyprus, and (iii) U.K., 1990; <I>Leader,</I> Indian Delegation to the Tenth World Forestry Conference in Paris, 1991; the UNEP Governing Council meeting in Nairobi, the PREPCOM IV discussion in New York and Kuala Lampur Conference, all in 1992; hosted the SAARC Environment Ministers` Conference in New Delhi and emerged as one of the chief spokesmen for developing countries at the UNCED in Rio de Janeiro in June 1992; Leader, National delegations to Finland, Sweden, Germany, Japan, Singapore, Dubai and UK and also to UNCTAD and UNEP and World Economic Forum meetings at Davos, Switzerland;<I>Participated in</I> WTO Ministerial/mini-Ministerial and other related meetings around the world."
  },
  {
   "full_name": "Murli Manohar Joshi",
   "constituency": "Kanpur",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "<b>Constituency Office Address :</b> Flat No. 15/96 H, Civil Lines, Kanpur-208001, Uttar Pradesh Tel/Fax : (0512) 2399555 <b>Residence Address :</b> C/o Shri Sudhindra Jain, 113/233, Swaroop Nagar, Kanpur-208002, Uttar Pradesh Tel : (0512) 2532110",
   "present_address": "6, Raisina Road,New Delhi - 110001Tels : (011) 23718444, 23326080 Fax : (011) 23711772",
   "email_id": "murli@sansad.nic.in <b>Website</b> : www.drmurlimanoharjoshi.in <b>Blog</b> : drmurlimjoshi.blogspot.com",
   "countries_visited": "Belgium, Brazil, Bulgaria, Canada, China, Cuba, Denmark, Egypt, England, France, Germany, Holland, Hungary, Iran, Italy, Japan, Malaysia, Mauritius, Mongolia, Nepal, Nigeria, North Korea, Portugal, Russia, South Africa, South Korea, Spain, Sri Lanka, Switzerland, Syria, Thailand, U.S.A. and Yugoslavia"
  },
  {
   "full_name": "Ramesh Chandappa Jigajinagi",
   "constituency": "Bijapur",
   "party": "Bharatiya Janata Party",
   "state": "Vinoda Farm, Near Bhutanal Tank,Bijapur-586101, Karnataka(08352)262233, 09449031477(M)",
   "permanent_address": "3, Canning Lane,New Delhi - 110 001Tels. (011) 23782843, 23073740, 09868180849 (M)",
   "present_address": "Education Qualifications: B.A. Educated at S.B. New Arts College, Bijapur, Karnataka"
  },
  {
   "full_name": "Laxman Giluwa",
   "constituency": "Singhbhum",
   "party": "Bharatiya Janata Party",
   "state": "Jharkhand",
   "permanent_address": "Ward No. 11, Chakradharpur, P.O.& P.S.-Chakradharpur,Distt. West Singhbhum, JharkhandTel. (06587) 238001",
   "present_address": "B-501, M.S. Flats, B.K.S. Marg, New Delhi - 110001",
   "email_id": "laxman.giluwa@sansad.nic.in"
  },
  {
   "full_name": "Rajen Gohain",
   "constituency": "Nawgong",
   "party": "Bharatiya Janata Party",
   "state": "Assam",
   "permanent_address": "Tilak Deka Road, Itachali,Distt. Nagaon - 782001, AssamMob : 09435060010, 09868180654",
   "present_address": "2, Talkatora Lane,New Delhi - 110011Tel : (011) 23093337 Mob : 9868180654",
   "email_id": "r.gohain@sansad.nic.in rajen.gohain@gmail.com",
   "countries_visited": "Laos, Thailand and U.K."
  },
  {
   "full_name": "Anant Gangaram Geete",
   "constituency": "Raigad",
   "party": "Shiv Sena",
   "state": "Maharashtra",
   "permanent_address": "A-5, Joshi Apartments, Lallubhai Park Road,Andheri (West), Mumbai - 400 058, MaharashtraTels. (022) 26705020, 26203131, 26706548",
   "present_address": "10, Raisina Road,New Delhi - 110 001Tels.(011) 23736393",
   "email_id": "geete@sansad.nic.in",
   "countries_visited": "Member, Indian Parliamentary Delegation led by the Honble Speaker, Shri G.M.C. Balayogi, Russia, 1998 and U.K., France, Egypt and U.A.E., March-April, 2000; (i) Addressed United Nations General Assembly, New York in October 2000, October 2004 and 2007"
  },
  {
   "full_name": "Bhavana Gawali (Patil)",
   "constituency": "Yavatmal-Washim",
   "party": "Shiv Sena",
   "state": "42,Canning Lane,New Delhi - 110 001Telefax. (011) 23782070, 09868180222 (M)",
   "permanent_address": "bhavana.gawali0222@gmail.com",
   "present_address": "Education Qualifications: B.A. (Marathi) Educated at Amravati University, Amravati (Maharashtra)",
   "email_id": "Widely travelled"
  },
  {
   "full_name": "Santosh Kumar Gangwar",
   "constituency": "Bareilly",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "Bharat Sewa Trust Bhawan, Pilibhit Road, Prem Nagar,Bareilly- 243 122 (Uttar Pradesh)Tels:(0581) 2545555, 2577777(O) (0581) 2577020 (R)",
   "present_address": "Delhi Residence Address: House No. 13, Sunehri Bagh Road, New Delhi-110011Tels: (011) 23062135, 23062136",
   "email_id": "i) santoshg@sansad.nic.in ii) santosh.gangwar.bareilly@gmail.com",
   "countries_visited": "France, Japan, Malaysia, Romania, Russia, U.A.E. (Abu Dhabi), U.K. and U.S.A."
  },
  {
   "full_name": "Sonia Gandhi",
   "constituency": "Rae Bareli",
   "party": "Indian National Congress",
   "state": "Uttar Pradesh",
   "permanent_address": "10, Janpath, New Delhi - 110011Tels. (011) 23014481 Fax. (011) 23018651",
   "present_address": "10, Janpath,New Delhi - 110 011Tels. (011) 23014481, 23012656 Fax. (011) 23018651",
   "email_id": "soniagandhi@sansad.nic.in",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Maneka Sanjay Gandhi",
   "constituency": "Pilibhit",
   "party": "Bharatiya Janata Party",
   "state": "Uttar Pradesh",
   "permanent_address": "14, Ashoka Road,New Delhi -110 001",
   "present_address": "14, Ashoka Road,</br> Andhra Pradesh Bhawan,New Delhi - 110 001Tels. (011) 23359241, 23357088 9868180604, 9013180192 (M)",
   "email_id": "gandhim@sansad.nic.in",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Dilip Kumar Mansukhlal Gandhi",
   "constituency": "Ahmednagar",
   "party": "Bharatiya Janata Party",
   "state": "Maharashtra",
   "permanent_address": "Devendra Bungalow, Achari Anadrishiji Marg,Ahmednagar - 414 001 Maharashtra(0241) 2451444, 2451515, 2452220 09422226070, 09013180296 (M)",
   "present_address": "6, Dr. Rajendra Prasad Road,New Delhi - 110 001Tels. (011) 23357732, 23354246, 23354145 9013180296 (M)",
   "email_id": "dilipmgandhi@gmail.com"
  },
  {
   "full_name": "Bandaru Dattatreya",
   "constituency": "Secunderabad",
   "party": "Bharatiya Janata Party",
   "state": "Ram Nagar,Hyderabad, Telangana",
   "permanent_address": "311, Andhra Pradesh Bhawan,New Delhi - 110001Tels: (011) 23384188, 23382031",
   "present_address": "bandaru@sansad.nic.in",
   "email_id": "Education Qualifications: B.Sc. Educated at Osmania University, Hyderabad (Andhra Pradesh"
  },
  {
   "full_name": "Adhir Ranjan Chowdhury",
   "constituency": "Baharampur",
   "party": "Indian National Congress",
   "state": "9, Haribapur, Paschim,</br> P.O.-Cossimbazar, Berhampure,Murshidabad-742102,</br> West BengalTels. (03482) 237688</br> Fax. (03483) 274089",
   "permanent_address": "14, New Moti Bagh,New Delhi - 110 021Tels. (011) 26870009,</br> Fax. (011) 26110009",
   "present_address": "adhir@sansad.nic.in",
   "email_id": "Education Qualifications: Educated at Iswar Chandra Vidyalaya"
  },
  {
   "full_name": "Nihal Chand Chauhan",
   "constituency": "Ganganagar",
   "party": "Bharatiya Janata Party",
   "state": "Rajasthan",
   "permanent_address": "Vill & P.O. Bajuwala, Teh. Rai Singh Nagar,Distt. Sriganganagar - 335051, RajasthanTel : (01507) 221317 Mob : 09414090050",
   "present_address": "17, Teen Murti Marg,New Delhi - 110021Tel : (011) 23010150 Mob : 9868180582 Fax : (011) 23010262",
   "email_id": "nihal.chand@sansad.nic.in mos-mopr@nic.in",
   "countries_visited": "Bangladesh & U.S.A."
  },
  {
   "full_name": "Sona Ram Choudhary",
   "constituency": "Barmer",
   "party": "Bharatiya Janata Party",
   "state": "Rajasthan",
   "permanent_address": "181/Ajit Colony, Circuit House Road, Jodhpur, Rajasthan09828999900, 09868180900 (M)",
   "present_address": "9, Talkatora Road,New Delhi - 110001Tel: (011) 23713222, 09868180900 (M)",
   "email_id": "col.sonaram@sansad.nic.in",
   "countries_visited": "Canada Hong Kong, Singapore, Thailand, UK, and USA"
  },
  {
   "full_name": "Nand Kumar Singh Chauhan",
   "constituency": "Khandwa",
   "party": "Bharatiya Janata Party",
   "state": "Madhya Pradesh",
   "permanent_address": "Ward No. 9, Shahpur,Distt. Burhanpur-450 331, Madhya PradeshTel. (07325) 241555, 08989785847 (M) Fax: (07325) 241555",
   "present_address": "6, Teenmurti Lane,New Delhi-110011Telefax:(011) 23011274, 09013869247 (M)",
   "email_id": "nandkumar.bjp@gmail.com",
   "countries_visited": "Brazil, Chile, Mexico"
  },
  {
   "full_name": "Ram Tahal Choudhary",
   "constituency": "Ranchi",
   "party": "Bharatiya Janata Party",
   "state": "Vill. & P.O. Kuchu Ormanjhi,Distt. Ranchi-535700,</br> Jharkhand",
   "permanent_address": "11-A, Pandit Pant Marg,New Delhi - 110001Tels. 9431382187, 9973828156 (M)",
   "present_address": "ramtahal.choudhary@sansad.nic.in",
   "email_id": "Education Qualifications: Matriculate"
  },
  {
   "full_name": "Haribhai Parthibhai Chaudhary",
   "constituency": "Banaskantha",
   "party": "Bharatiya Janata Party",
   "state": "At&PO - Jagana, Ta. - PalanpurDistt. Banaskantha - 385011,</br> GujaratTels. (02742) 220111, 09426502727 (M)",
   "permanent_address": "9, Harish Chander Mathur Lane,</br> Ferozshah Road,New Delhi-110001Tels. (011)23355405, 09013180954 (M)",
   "present_address": "haribhaipchaudhary@gmail.com",
   "email_id": "Education Qualifications: Graduate Educated at Mumbai University, Mumbai (Maharashtra)"
  },
  {
   "full_name": "Bijoya Chakravarty",
   "constituency": "Gauhati",
   "party": "Bharatiya Janata Party",
   "state": "Assam",
   "permanent_address": "39, Srinagar Path, Bye Lane - I,Guwahati - 5, Assam",
   "present_address": "18, Mahadev Road,New Delhi - 110 001Tels. 23752342, 23752343, 09435017048 (M)",
   "email_id": "bijoya.chakravarty@sansad.nic.in</br> bijoya@nic.in",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Sudip Bandyopadhyay",
   "constituency": "Kolkata Uttar",
   "party": "All India Trinamool Congress",
   "state": "West Bengal",
   "permanent_address": "72/4, S.N. Banerjee Road, Waverly Mansion,P.O. Entally, Kolkata-700 014, West BengalTels. (033) 22175010, 09433086118 (M), Fax. (033) 22175010",
   "present_address": "1-B, Maulana Azad Road,New Delhi-110 011Tels. 011-23061153, 23061101, 9013180066 (M)",
   "email_id": "sudip@sansad.nic.in</br> sudip_bandyopadhyay2006@yahoo.com",
   "countries_visited": "Bangladesh, Bulgaria, China, Czechoslovakia, Germany, Holland, Hungary, Italy, Japan, Malaysia, France, Singapore, Switzerland, Thailand, U.K. and U.S.A."
  },
  {
   "full_name": "Ramesh Bais",
   "constituency": "Raipur",
   "party": "Bharatiya Janata Party",
   "state": "Chhattisgarh",
   "permanent_address": "9, Ravi Nagar,Raipur - 492 001, ChhattisgarhTels. (0771) 2423000, 09425509933 (M)",
   "present_address": "85, Lodhi Estate,New Delhi - 110 003Tels. (011) 24692730, 9868180572 (M) Telefax. (011) 24692731",
   "email_id": "ramesh.bais@sansad.nic.in",
   "countries_visited": "Austria, Australia, Brazil, Canada, Greece, Hungary, Indonasia, Italy, Malaysia, Russia, Singapore, Switzerland, U.A.E., U.K. and U.S.A."
  },
  {
   "full_name": "Kirti (JHA) Azad",
   "constituency": "Darbhanga",
   "party": "Bharatiya Janata Party",
   "state": "Bihar",
   "permanent_address": "Kathalbari, Diwani Takia, Distt. Darbhanga, Bihar09006091355, 09431219001 (M)",
   "present_address": "25, Pt. Ravishankar Shukla Lane,</br>K.G. Marg, New Delhi - 110 001Tels. (011) 23073234, 09431219001 (M) Fax: (011) 23782645,",
   "email_id": "(i) kirti.azad@sansad.nic.in (ii) kirtiazad.office@gmail.com",
   "countries_visited": "Widely travelled"
  },
  {
   "full_name": "Ananth Kumar",
   "constituency": "Bangalore South",
   "party": "Bharatiya Janata Party",
   "state": "Karnataka",
   "permanent_address": "No. 84, Shashwati, Ranoji Rao Road, Basavanagudi,Bangalore - 560 004, KarnatakaTel. (080) 26568484 Telefax. (080) 26568483",
   "present_address": "26, Tughlak Crescent,New Delhi - 110 011Tel. (011) 23794754, 9868180284 (M)</br> Fax: (011) 23012791",
   "email_id": "(i) akumar-alpha@sansad.nic.in</br> (ii) ananth@ananth.org",
   "countries_visited": "Brazil, China, France, Germany, Italy,Iran, Japan, Malaysia, Singapore, Switzerland, Turkmenistan, U.A.E., U.K., and U.S.A. (as part of International Exchange Programme; and as Special Emissary of the Government of India to hoist the Tri-colour in Washington for the celebration of 51st Year of Indian Independence, August, 1998)"
  },
  {
   "full_name": "E. Ahamed",
   "constituency": "Malappuram",
   "party": "Indian Union Muslim League",
   "state": "Kerala",
   "permanent_address": "House No.13/40-B, `Sitara` Thana - Kannur-670012KeralaTels. (0497)2706713, 09818882200(M)",
   "present_address": "9, Teen Murti Marg,New Delhi - 110 011Tels. (011) 23017051 Tel/Fax. (011) 23017052",
   "email_id": "eahmed@hotmail.com",
   "countries_visited": "Widelly travelled; <I>Chairman,</I> Meeting of Heads of Indian Missions of GCC countries, Doha, 18th & 19th March 2006; <I>Special Emissary</I> of the then Prime Minister Late Smt. Indira Gandhi and met Heads of States of the Gulf Countries, 1984;<I>Leader of Indian Delegation to :</I> (i) Trade delegation of government of India to Gulf Countries, 1984; (ii) Indian Ocean Rim Association for Regional Co-operation Ministerial Meeting, Colombo, August, 2004; (iii) Signing of Sudan Peace Agreement, Nairobi, January 2005; (iv) Small Island developing States Meeting, Mauritius, January, 2005; (v) League of Arab States Summit, Algiers, March, 2005; (vi) Sudan donors Conference, Oslo, April, 2005; (vii) South Summit/G-77 Ministerial Confernce at Doha, Qatar, June, 2005; (viii) Review Conference on Financing for Development, United Nations General Assembly, June, 2005; (ix) Regional Ministerial Meeting of Asia and Pacific on Millennium Development Goals, Jakarta, August, 2005; (x) Lebanon and Syria on a Bilateral visit from 27 Sept. 2005-1 Oct. 2005; (xi) 26 Session of SAARC Summit, Dhaka, 10-13 November, 2005; (xii) International Donors Conference, Islamabad, 18-22 November, 2005; (xiii) 6th Indian Ocean Rim Associaton for Regional Cooperation Ministerial and Senior officals meeting, Tehran, 20-22 February,2006; (xiv) Eighteenth Summit of League of Arab States, Khartoum, Sudan, 28-30 March, 2006; (xv) 10th Session of India-Tunisia Joint Commission meeting, Tunisia, 5-8 February, 2007; (xvi)7th Council of Ministers meeting of Indian Ocean Rim Association for Regional Cooperation (IOR-ARC), Tehran, 3-8 March, 2007; (xvii) 6th Asia Cooperation Dialogue Ministerial Meeting, Seoul, South Korea; (xviii) NAM Ministerial Meeting on Human Rights and Cultural Diversity, Tehran, Iran, 3-4 September, 2007; (xix) Heads of State Council meeting of the Member & Observer States of the Shanghai Cooperation Organisation, Tashkent, 1-3 November , 2007; (xx)62nd Session, UNGA, New York, 29 November-3 December, 2007; (xxi) 31st Session of SAARC Council of Minsiters meeting, Colombo, 27 February, 2009;(xxii) NAM Ministerial Meeting, Havana 29-30 April, 2009; (xxiii) League of Arab States Summit, Algiers, 2005; Khartoum, 2006; Riyadh, 2007; Damascus, 2008; Doha, 2009; Leader, Fact Finding Team, Mina Fire Tragedy, Saudi Arabia, 1997;<I>Member:</I> (i) Indian Delegation in the UN General Assembly, 1992-97; (ii) Indian Delegation to World Social Summit Copenhagen, 1995; (iii) Indian parliamentary Delegations to various countries, 1994-2001;and (iv) Indian World Parliamentary Conference, Amman, Jordan, 2000;<I>Represented,</I> Indian Parliament in Commonwealth Parliamentary Joint Colloquium at Buckinghamshire, U.K., 1998; <I>Accompanied:</I> (i) Former Vice President, Shri Bhairon Singh Shekhawat in the funeral of ruler of Dubai H. H. Sheikh Makhtoum Rashid Al-Makhtoum on 5 January 2007; (ii) Hon`ble Vice President of India to Turkmenistan and Kazakhstan, April 4-10, 2008; (iii) Prime Minsiter of India to Oman and Qatar, 8-9 November, 2008;"
  },
  {
   "full_name": "Lal Krishna Advani",
   "constituency": "Gandhinagar",
   "party": "Bharatiya Janata Party",
   "state": "Gujarat",
   "permanent_address": "1835/16, Kasturbhai Block, Din Dayal Bhawan,J.P.Chowk, Khanpur, Ahmedabad-380 001, Gujarat(079)22504525",
   "present_address": "30, Prithviraj Road,New Delhi - 110 011Tels. (011) 23794124, 23794125</br> Fax: (011) 23013142",
   "email_id": "advanilk@sansad.nic.in",
   "countries_visited": "Widely travelled; <I>Member</I>, Indian Parliamentary Delegation to, (i) Czechoslovakia, 1972; (ii) Australia, 1974; (iii) I.P.U. Conference at Ottawa, 1985; Leader, (i) Indian Delegation to Inter-Governmental Conference on Communication Policies in Asia and Oceania (ASIOCOM), Kuala Lumpur, 1977; (ii) UNESCO General Conference, 1978; and (iii) Indian Parliamentary Delegation to Strasbourg Conference on Parliamentary Democracy, September 1991; visited Germany, Turkey, UAE (2001); USA (2002 & 2003); Spain (2002); U.K. (2002 & 2003); Qatar & France (2003);Thailand & Singapore (2003) as Deputy Prime Minister and Minister for Home Affairs; visited Pakistan (2005) in the capacity of Leader of Opposition (LS)"
  },
  {
   "full_name": "Anandrao Adsul",
   "constituency": "Amravati",
   "party": "Shiv Sena",
   "state": "Maharashtra",
   "permanent_address": "5/B,Kadamgiri Apartment,Co-operative Housing Society Ltd., (br) Ashok Nagar Chakravarti Ashok Road, Kandivali (East)Mumbai-400101, Maharashatra(022)28871042, 28863403(R), 09868180266 (M)",
   "present_address": "AB-9, Pandara Road,New Delhi - 110 003Tels. (011) 23074036, 9868180266 (M) Telefax: (011) 23074036",
   "email_id": "av.adsul@sansad.nic.in",
   "countries_visited": "Australia, France, Germany, Hong Kong, Israel, Malaysia, Nepal, New Zealand, Singapore, Thailand, U.K. and U.S.A."
  },
  {
   "full_name": "Yogi Adityanath",
   "constituency": "Gorakhpur",
   "party": "Bharatiya Janata Party",
   "state": "yogi.adityanath@sansad.nic.in yogiadityanath72@gmail.com",
   "permanent_address": "Education Qualifications: B.Sc. Educated at H.N.B. Garhwal University, Srinagar, Uttarakhand",
   "present_address": "Combodia, Malaysia, Nepal, Singapore,Thailand and U.S.A."
  },
  {
   "full_name": "Kapil Krishna Thakur",
   "constituency": "Bangaon",
   "party": "All India Trinamool Congress"
  },
  {
   "full_name": "Tariq Anwar",
   "constituency": "Katihar",
   "party": "Nationalist Congress Party"
  },
  {
   "full_name": "Thangso Baite",
   "constituency": "Outer Manipur",
   "party": "Indian National Congress",
   "state": "Manipur",
   "permanent_address": "Vill. Dongjang, Hmarveng, P.O. Sugnu, Distt. Churachandpur,ManipurTels. (0385) 2416555, 09013180079 (M)",
   "present_address": "14, North Avenue,New Delhi -110 001Tels. (011) 23092026, 23092131 9013180079 (M)",
   "email_id": "t.baite@sansad.nic.in</br> tbaite@live.com",
   "countries_visited": "Nepal"
  },
  {
   "full_name": "Hemendra Chandra Singh",
   "constituency": "Kandhamal",
   "party": "Biju Janata Dal"
  }]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Welcome to InfoMP API!'})

@app.route('/infomp', methods=['GET'])
def returnAll():
    return jsonify({'mp_data_unified' : mp_data_unified})

@app.route('/infomp/<string:constituency>', methods=['GET'])
def returnOne(constituency):
    constituency = [mp_data_unified for mp_data_unified in mp_data_unified if mp_data_unified['constituency'] == constituency]
    return jsonify({'MP Bio' : infomp['constituency']})

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app on port 5000 in debug mode