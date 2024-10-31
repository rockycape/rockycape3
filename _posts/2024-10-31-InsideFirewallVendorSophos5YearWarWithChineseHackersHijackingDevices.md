---
title: "Inside a Firewall Vendor's 5-Year War With the Chinese Hackers Hijacking Its Devices"  
categories: cybersecurity
---


[![WIRED](https://www.wired.com/verso/static/wired/assets/logo-header.svg)](https://www.wired.com/)

[Andy Greenberg](https://www.wired.com/author/andy-greenberg/)

[Security](https://www.wired.com/category/security)

Oct 31, 2024 8:45 AM

# Inside a Firewall Vendor's 5-Year War With the Chinese Hackers Hijacking Its Devices

Sophos went so far as to plant surveillance "implants" on its own devices to catch the hackers at work---and in doing so, revealed a glimpse into China's R&D pipeline of intrusion techniques.

![Appliance Security Camera China Flag](https://media.wired.com/photos/671aaef2ebc1cb03f39ea41d/master/w_2560%2Cc_limit/Security_Sophus_Getty-Images.jpg)

Photo Illustration: WIRED Staff; Getty Images

For years, it's been an inconvenient truth within the cybersecurity industry that the network security devices sold to protect customers from spies and cybercriminals are, themselves, often the machines those intruders hack to gain access to their targets. Again and again, vulnerabilities in "perimeter" devices like [firewalls](https://www.wired.com/story/arcanedoor-cyberspies-hacked-cisco-firewalls-to-access-government-networks/) and [VPN](https://www.wired.com/story/tunnelvision-vpn-attack/) appliances have become footholds for sophisticated hackers trying to break into the very systems those appliances were designed to safeguard.

Now one cybersecurity vendor is revealing how intensely---and for how long---it has battled with one group of hackers that have sought to exploit its products to their own advantage. For more than five years, the UK cybersecurity firm Sophos engaged in a cat-and-mouse game with one loosely connected team of adversaries who targeted its firewalls. The company went so far as to track down and monitor the specific devices on which the hackers were testing their intrusion techniques, surveil the hackers at work, and ultimately trace that focused, years-long exploitation effort to a single network of vulnerability researchers in Chengdu, China.

On Thursday, Sophos chronicled that half-decade-long war with those Chinese hackers in a [report](https://www.sophos.com/en-us/content/pacific-rim) that details its escalating tit-for-tat. The company went as far as discreetly installing its own "implants" on the Chinese hackers' Sophos devices to monitor and preempt their attempts at exploiting its firewalls. Sophos researchers even eventually obtained from the hackers' test machines a specimen of "bootkit" malware designed to hide undetectably in the firewalls' low-level code used to boot up the devices, a trick that has never been seen in the wild.

In the process, Sophos analysts identified a series of hacking campaigns that had started with indiscriminate mass exploitation of its products but eventually became more stealthy and targeted, hitting nuclear energy suppliers and regulators, military targets including a military hospital, telecoms, government and intelligence agencies, and the airport of one national capital. While most of the targets---which Sophos declined to identify in greater detail---were in South and Southeast Asia, a smaller number were in Europe, the Middle East, and the United States.

Sophos' report ties those multiple hacking campaigns---with varying levels of confidence---to Chinese state-sponsored hacking groups including those known as APT41, APT31, and Volt Typhoon, the latter of which is a particularly aggressive team that has sought the ability to [disrupt critical infrastructure in the US](https://www.wired.com/story/nsa-china-hacking-criticial-us-infrastructure/), including power grids. But the common thread throughout those efforts to hack Sophos' devices, the company says, is not one of those previously identified hackers groups but instead a broader network of researchers that appears to have developed hacking techniques and supplied them to the Chinese government. Sophos' analysts tie that exploit development to an academic institute and a contractor, both around Chengdu: Sichuan Silence Information Technology---a firm [previously tied by Meta to Chinese state-run disinformation efforts](https://www.bbc.com/news/world-asia-china-59456548)---and the University of Electronic Science and Technology of China.

Sophos says it's telling that story now not just to share a glimpse of China's pipeline of hacking research and development, but also to break the cybersecurity industry's awkward silence around the larger issue of vulnerabilities in security appliances serving as entry points for hackers. In just the past year, for instance, flaws in security products from other vendors including Ivanti, Fortinet, Cisco, and Palo Alto have all been exploited in mass hacking or targeted intrusion campaigns. "This is becoming a bit of an open secret. People understand this is happening, but unfortunately everyone is _zip,_" says Sophos chief information security officer Ross McKerchar, miming pulling a zipper across his lips. "We're taking a different approach, trying to be very transparent, to address this head-on and meet our adversary on the battlefield."

## From One Hacked Display to Waves of Mass Intrusion

As Sophos tells it, the company's long-running battle with the Chinese hackers began in 2018 with a breach of Sophos itself. The company discovered a malware infection on a computer running a display screen in the Ahmedabad office of its India-based subsidiary Cyberoam. The malware had gotten Sophos' attention due to its noisy scanning of the network. But when the company's analysts looked more closely, they found that the hackers behind it had already compromised other machines on the Cyberoam network with a more sophisticated rootkit they [identified as CloudSnooper](https://news.sophos.com/en-us/2020/02/25/cloud-snooper/). In retrospect, the company believes that initial intrusion was designed to gain intelligence about Sophos products that would enable follow-on attacks on its customers.

Then in the spring of 2020, Sophos began to learn about a broad campaign of indiscriminate infections of tens of thousands of firewalls around the world in an apparent attempt to install a trojan [called Asnarök](https://news.sophos.com/en-us/2020/04/26/asnarok/) and create what it calls "operational relay boxes" or ORBs---essentially a botnet of compromised machines the hackers could use as launching points for other operations. The campaign was surprisingly well resourced, exploiting multiple zero-day vulnerabilities the hackers appeared to have discovered in Sophos appliances. Only a bug in the malware's cleanup attempts on a small fraction of the affected machines allowed Sophos to analyze the intrusions and begin to study the hackers targeting its products.

As Sophos pushed out patches to its firewalls, its team responsible for threat intelligence and incident response, which it calls X-Ops, also began an effort to track its adversary: Sophos included in its "hotfix" for the hackers' intrusions additional code that would collect more data from customers' devices. That new data collection revealed that a single Sophos device registered in February of 2020 in Chengdu showed signs of early alterations similar to the Asnarök malware. "We started to find tiny little indicators of the attack that predated any other activity," McKerchar says.

Using registration data and records of downloads of code Sophos made available to its customers, the X-Ops team eventually identified a handful of machines it believed were being used as guinea pig devices for Chinese hackers as they sought to find vulnerabilities and test their intrusion techniques prior to deployment. Some of them seemed to have been obtained by a Chengdu-based company called Sichuan Silence Information Technology. Others were tied to an individual who used the handle TStark, whom X-Ops analysts then found had held a position at the University of Electronic Science and Technology of China, also in Chengdu.

X-Ops analysts could even observe individuals using computers and IP addresses tied to the test devices reading Sophos' online materials that detailed the firewalls' architecture. "We could see them researching us," McKerchar says.

In late April of 2020, Dutch police worked with Sophos to seize a Netherlands-based server that Sophos had identified as being used in the Asnarök infection wave. In June of that year, however, the hackers launched another round of their mass intrusions, and Sophos found they had significantly reduced the complexity and "noise" of their malware in an attempt to evade detection. Yet through the increased data collection from its devices and the intelligence it had assembled on the Chengdu exploit development group, Sophos was able to spot the malware and push out patches for the vulnerabilities the hackers had used within a week, and even identify a "patient zero" machine where the new malware had first been tested two months earlier.

The next month, X-Ops took its most aggressive step yet in countering the effort to exploit its devices, deploying its own spy implants to the Sophos devices in Chengdu they were testing on---essentially hacking the hackers, albeit only through code added to a few installations of its own products the hackers had obtained. Sophos says that preemptive surveillance allowed the company to obtain key portions of the hackers' code and head off a third wave of their intrusions, catching it after only two customers had been compromised and pushing out a patch designed to block the attacks, while obfuscating that fix to avoid tipping off the hackers to Sophos' full knowledge of their techniques.

"In the first wave, we were on the back foot. In the second wave, it was an even match," says McKerchar. "The third attack, we preempted."

## A New Phase of the Game

Starting in 2021, Sophos says it began to see far more targeted attacks from Chinese hacker groups exploiting its products, many of which it was able to uncover due to its efforts to surveil the research of the Chengdu-based exploit development network. Over the next two years, the hackers continued hijack vulnerabilities in Sophos appliances in a wide variety of targeted attacks hitting dozens of targets in Asia and the West.

In September of 2022, for instance, Sophos found a campaign exploiting a vulnerability in its products that had breached military and intelligence agencies in a Southeast Asian country, as well as other targets including water utilities and electric generation facilities in the same region. Later, Sophos says, a different Chinese state-sponsored group appears to have exploited a bypass for its patch for that vulnerability to target government agencies outside of Asia, in one instance hacking an embassy shortly before it was set to host officials from China's ruling Communist Party. It also found intrusions at another country's nuclear energy regulatory agency, then a military facility in the same country and the airport of the country's capital city, as well as other hacking incidents that targeted Tibetan exiles.

"We just opened the door on a huge amount of high-end targeted activity, a Pandora's Box of threat intelligence," McKerchar says.

As the hackers' tooling continued to evolve in response to Sophos' attempts to head them off, the company's X-Ops researchers at one point pulled from a test device they were surveilling a unique new specimen of malware: The hackers had built a "bootkit," an early attempt at malware designed to infect a Sophos firewall's low-level code that's used to boot up the device before its operating system is loaded, which would make the malware far harder to detect---the first time Sophos believes that sort of firewall bootkit has ever been seen.

X-Ops never found that bootkit deployed on an actual victim's machine, but Sophos CISO McKerchar says he can't rule out that it was in fact used somewhere and evaded detection. "We certainly tried to hunt for it, and we have some capability to do that," says McKerchar. "But I would be brash to say it's never been used in the wild."

As Sophos has tried to understand the motives of the Chengdu-based network of hackers digging up vulnerabilities and providing them to the Chinese state, that picture has been complicated by the strange fact that the researchers finding those flaws may have on two occasions also reported them to Sophos itself through its "bug bounty" program. On one occasion, for instance, the exact vulnerability used in a hacking campaign was reported to Sophos by a researcher with a Chinese IP address just after it was first used in an exploitation campaign---Sophos paid the researcher $20,000 for their findings.

That bizarre incongruity with the Chengdu-based researchers' apparent role as suppliers of intrusion techniques for Chinese state hacking groups and its bug bounty reports to Sophos, McKerchar argues, show perhaps how loose the connections are between the researchers finding these vulnerabilities and the state hackers exploiting those bugs. "I think this is a security research community which is patriotically aligned with PRC objectives," he says, referencing the People's Republic of China. "But they're not averse to making a bit of money on the side."

Contacts at the University of Electronic Science and Technology China didn't respond to WIRED's request for comment on Sophos' report. Sichuan Silence Information Technology couldn't be reached for comment, and appears to have no working website.

Sophos' timeline of its struggle against a highly adaptive adversaries sussing out its products' hackable flaws points to the success of China's efforts to corral its security research community and funnel its discoveries of vulnerabilities to the government, says Dakota Cary, a researcher at the Atlantic Council, a nonpartisan think tank, who has focused on that Chinese exploit development pipeline. He points to China's efforts, for instance, to [foster hacking competitions as a source of intrusion techniques](https://www.wired.com/story/china-hacking-competition-real-victim/) for its offensive hacking efforts, as well as 2021 legislation that requires researchers and companies based in China to [report to the government any hackable bug they find in a product](https://www.wired.com/story/china-vulnerability-disclosure-law/).

"In Sophos' document, you see the interconnectedness of that system kind of shine through," says Cary. "The culture of these organizations working together or competing for work, and the way that the government is trying to centralize collection of vulnerabilities and then distribute those tools to offensive teams---you see all of that reflected."

Sophos' report also warns, however, that in the most recent phase of its long-running conflict with the Chinese hackers, they appear more than ever before to have shifted from finding new vulnerabilities in firewalls to exploiting outdated, years-old installations of its products that are no longer receiving updates. That means, company CEO Joe Levy writes in an accompanying document, that device owners need to get rid of unsupported "end-of-life" devices, and security vendors need to be clear with customers about the end-of-life dates of those machines to avoid letting them become unpatched points of entry onto their network. Sophos says it's seen more than a thousand end-of-life devices targeted in just the past 18 months.

"The only problem now isn't the zero-day vulnerability," says Levy, using the term "zero-day" to mean a newly discovered hackable flaw in software that has no patch. "The problem is the 365-day vulnerability, or the 1,500-day vulnerability, where you've got devices that are on the internet that have lapsed into a state of neglect."

That warning was echoed by Cybersecurity and Infrastructure Security Agency assistant director for cybersecurity Jeff Greene, who stresses the risk of Chinese hackers exploiting older, unpatched systems, as well as the broader, ironic threat of network perimeter appliances serving as entry points for hackers. "These edge devices often have inherent insecurities, they're often not managed once they're put out, they're not patched," says Greene. "We'll leave a trail of these devices for a long time that attackers will be looking to compromise."

Sophos CISO McKerchar says the company is revealing its five-year fight with the Chengdu-based hacking network to amplify those warnings, but also to end a kind of cybersecurity industry omertà around the growing issue of security companies' own products creating vulnerabilities for their customers. "Trust in the industry has been massively eroded in the past few years. There's a huge amount of skepticism across about the way that vendors are handling these risks, but we've relied on silence instead," says McKerchar. "We want to show a bit of vulnerability ourselves, recognize that we've had problems, then tell the story about how we stepped up."

[![](https://media.wired.com/photos/65e8363c8aa58009f1f54a9b/1:1/w_270%2Cc_limit/undefined)](https://www.wired.com/author/andy-greenberg/)

[Andy Greenberg](https://www.wired.com/author/andy-greenberg/) is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He's the author of the new book _Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency_. His last book was *Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most... [Read more](https://www.wired.com/author/andy-greenberg/)

Senior Writer

- [Twitter Andy Greenberg](https://www.twitter.com/a_greenberg)

![Wired logo](https://media.wired.com/photos/6335c338010e2be68af5d43a/master/w_125,h_50,c_limit/logo-wired.png?format=original)