_e='iveTemperature'
_d='nodeName'
_c='newVIP'
_b='currentVIP'
_a='vipType'
_Z='nodeList'
_Y='clusterName'
_X='raidDescription'
_W='psDescription'
_V='fanDescription'
_U='ocspResponderURL'
_T='ivsName'
_S='iveSwapUtil'
_R='iveCpuUtil'
_Q='iveMemoryUtil'
_P='logDescription'
_O='logType'
_N='diskFullPercent'
_M='meetingCount'
_L='meetingUserCount'
_K='fileName'
_J='authServerName'
_I='blockedIP'
_H='logFullPercent'
_G='ipIndex'
_F='logName'
_E='nicEvent'
_D='accessible-for-notify'
_C='read-only'
_B='JUNIPER-IVE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniper_ive=ModuleIdentity((1,3,6,1,4,1,12532))
if mibBuilder.loadTexts:juniper_ive.setRevisions(('2010-02-22 10:00',))
_LogFullPercent_Type=Gauge32
_LogFullPercent_Object=MibScalar
logFullPercent=_LogFullPercent_Object((1,3,6,1,4,1,12532,1),_LogFullPercent_Type())
logFullPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:logFullPercent.setStatus(_A)
_SignedInWebUsers_Type=Gauge32
_SignedInWebUsers_Object=MibScalar
signedInWebUsers=_SignedInWebUsers_Object((1,3,6,1,4,1,12532,2),_SignedInWebUsers_Type())
signedInWebUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:signedInWebUsers.setStatus(_A)
_SignedInMailUsers_Type=Gauge32
_SignedInMailUsers_Object=MibScalar
signedInMailUsers=_SignedInMailUsers_Object((1,3,6,1,4,1,12532,3),_SignedInMailUsers_Type())
signedInMailUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:signedInMailUsers.setStatus(_A)
_BlockedIP_Type=IpAddress
_BlockedIP_Object=MibScalar
blockedIP=_BlockedIP_Object((1,3,6,1,4,1,12532,4),_BlockedIP_Type())
blockedIP.setMaxAccess(_D)
if mibBuilder.loadTexts:blockedIP.setStatus(_A)
_AuthServerName_Type=OctetString
_AuthServerName_Object=MibScalar
authServerName=_AuthServerName_Object((1,3,6,1,4,1,12532,5),_AuthServerName_Type())
authServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:authServerName.setStatus(_A)
_ProductName_Type=OctetString
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,12532,6),_ProductName_Type())
productName.setMaxAccess(_C)
if mibBuilder.loadTexts:productName.setStatus(_A)
_ProductVersion_Type=OctetString
_ProductVersion_Object=MibScalar
productVersion=_ProductVersion_Object((1,3,6,1,4,1,12532,7),_ProductVersion_Type())
productVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:productVersion.setStatus(_A)
_FileName_Type=OctetString
_FileName_Object=MibScalar
fileName=_FileName_Object((1,3,6,1,4,1,12532,8),_FileName_Type())
fileName.setMaxAccess(_D)
if mibBuilder.loadTexts:fileName.setStatus(_A)
_MeetingUserCount_Type=Gauge32
_MeetingUserCount_Object=MibScalar
meetingUserCount=_MeetingUserCount_Object((1,3,6,1,4,1,12532,9),_MeetingUserCount_Type())
meetingUserCount.setMaxAccess(_D)
if mibBuilder.loadTexts:meetingUserCount.setStatus(_A)
_IveCpuUtil_Type=Gauge32
_IveCpuUtil_Object=MibScalar
iveCpuUtil=_IveCpuUtil_Object((1,3,6,1,4,1,12532,10),_IveCpuUtil_Type())
iveCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:iveCpuUtil.setStatus(_A)
_IveMemoryUtil_Type=Gauge32
_IveMemoryUtil_Object=MibScalar
iveMemoryUtil=_IveMemoryUtil_Object((1,3,6,1,4,1,12532,11),_IveMemoryUtil_Type())
iveMemoryUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:iveMemoryUtil.setStatus(_A)
_IveConcurrentUsers_Type=Gauge32
_IveConcurrentUsers_Object=MibScalar
iveConcurrentUsers=_IveConcurrentUsers_Object((1,3,6,1,4,1,12532,12),_IveConcurrentUsers_Type())
iveConcurrentUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:iveConcurrentUsers.setStatus(_A)
_ClusterConcurrentUsers_Type=Gauge32
_ClusterConcurrentUsers_Object=MibScalar
clusterConcurrentUsers=_ClusterConcurrentUsers_Object((1,3,6,1,4,1,12532,13),_ClusterConcurrentUsers_Type())
clusterConcurrentUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:clusterConcurrentUsers.setStatus(_A)
_IveTotalHits_Type=Counter64
_IveTotalHits_Object=MibScalar
iveTotalHits=_IveTotalHits_Object((1,3,6,1,4,1,12532,14),_IveTotalHits_Type())
iveTotalHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveTotalHits.setStatus(_A)
_IveFileHits_Type=Counter64
_IveFileHits_Object=MibScalar
iveFileHits=_IveFileHits_Object((1,3,6,1,4,1,12532,15),_IveFileHits_Type())
iveFileHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveFileHits.setStatus(_A)
_IveWebHits_Type=Counter64
_IveWebHits_Object=MibScalar
iveWebHits=_IveWebHits_Object((1,3,6,1,4,1,12532,16),_IveWebHits_Type())
iveWebHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveWebHits.setStatus(_A)
_IveAppletHits_Type=Counter64
_IveAppletHits_Object=MibScalar
iveAppletHits=_IveAppletHits_Object((1,3,6,1,4,1,12532,17),_IveAppletHits_Type())
iveAppletHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveAppletHits.setStatus(_A)
_IvetermHits_Type=Counter64
_IvetermHits_Object=MibScalar
ivetermHits=_IvetermHits_Object((1,3,6,1,4,1,12532,18),_IvetermHits_Type())
ivetermHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ivetermHits.setStatus(_A)
_IveSAMHits_Type=Counter64
_IveSAMHits_Object=MibScalar
iveSAMHits=_IveSAMHits_Object((1,3,6,1,4,1,12532,19),_IveSAMHits_Type())
iveSAMHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveSAMHits.setStatus(_A)
_IveNCHits_Type=Counter64
_IveNCHits_Object=MibScalar
iveNCHits=_IveNCHits_Object((1,3,6,1,4,1,12532,20),_IveNCHits_Type())
iveNCHits.setMaxAccess(_C)
if mibBuilder.loadTexts:iveNCHits.setStatus(_A)
_MeetingHits_Type=Counter64
_MeetingHits_Object=MibScalar
meetingHits=_MeetingHits_Object((1,3,6,1,4,1,12532,21),_MeetingHits_Type())
meetingHits.setMaxAccess(_C)
if mibBuilder.loadTexts:meetingHits.setStatus(_A)
_MeetingCount_Type=Gauge32
_MeetingCount_Object=MibScalar
meetingCount=_MeetingCount_Object((1,3,6,1,4,1,12532,22),_MeetingCount_Type())
meetingCount.setMaxAccess(_D)
if mibBuilder.loadTexts:meetingCount.setStatus(_A)
_LogName_Type=OctetString
_LogName_Object=MibScalar
logName=_LogName_Object((1,3,6,1,4,1,12532,23),_LogName_Type())
logName.setMaxAccess(_D)
if mibBuilder.loadTexts:logName.setStatus(_A)
_IveSwapUtil_Type=Gauge32
_IveSwapUtil_Object=MibScalar
iveSwapUtil=_IveSwapUtil_Object((1,3,6,1,4,1,12532,24),_IveSwapUtil_Type())
iveSwapUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:iveSwapUtil.setStatus(_A)
_DiskFullPercent_Type=Gauge32
_DiskFullPercent_Object=MibScalar
diskFullPercent=_DiskFullPercent_Object((1,3,6,1,4,1,12532,25),_DiskFullPercent_Type())
diskFullPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:diskFullPercent.setStatus(_A)
_BlockedIPList_Object=MibTable
blockedIPList=_BlockedIPList_Object((1,3,6,1,4,1,12532,26))
if mibBuilder.loadTexts:blockedIPList.setStatus(_A)
_IpEntry_Object=MibTableRow
ipEntry=_IpEntry_Object((1,3,6,1,4,1,12532,26,1))
ipEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ipEntry.setStatus(_A)
_IpIndex_Type=Integer32
_IpIndex_Object=MibTableColumn
ipIndex=_IpIndex_Object((1,3,6,1,4,1,12532,26,1,1),_IpIndex_Type())
ipIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipIndex.setStatus(_A)
_IpValue_Type=IpAddress
_IpValue_Object=MibTableColumn
ipValue=_IpValue_Object((1,3,6,1,4,1,12532,26,1,2),_IpValue_Type())
ipValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ipValue.setStatus(_A)
_LogID_Type=OctetString
_LogID_Object=MibScalar
logID=_LogID_Object((1,3,6,1,4,1,12532,27),_LogID_Type())
logID.setMaxAccess(_D)
if mibBuilder.loadTexts:logID.setStatus(_A)
_LogType_Type=OctetString
_LogType_Object=MibScalar
logType=_LogType_Object((1,3,6,1,4,1,12532,28),_LogType_Type())
logType.setMaxAccess(_D)
if mibBuilder.loadTexts:logType.setStatus(_A)
_LogDescription_Type=OctetString
_LogDescription_Object=MibScalar
logDescription=_LogDescription_Object((1,3,6,1,4,1,12532,29),_LogDescription_Type())
logDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:logDescription.setStatus(_A)
_IvsName_Type=OctetString
_IvsName_Object=MibScalar
ivsName=_IvsName_Object((1,3,6,1,4,1,12532,30),_IvsName_Type())
ivsName.setMaxAccess(_D)
if mibBuilder.loadTexts:ivsName.setStatus(_A)
_OcspResponderURL_Type=OctetString
_OcspResponderURL_Object=MibScalar
ocspResponderURL=_OcspResponderURL_Object((1,3,6,1,4,1,12532,31),_OcspResponderURL_Type())
ocspResponderURL.setMaxAccess(_D)
if mibBuilder.loadTexts:ocspResponderURL.setStatus(_A)
_FanDescription_Type=OctetString
_FanDescription_Object=MibScalar
fanDescription=_FanDescription_Object((1,3,6,1,4,1,12532,32),_FanDescription_Type())
fanDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:fanDescription.setStatus(_A)
_PsDescription_Type=OctetString
_PsDescription_Object=MibScalar
psDescription=_PsDescription_Object((1,3,6,1,4,1,12532,33),_PsDescription_Type())
psDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:psDescription.setStatus(_A)
_RaidDescription_Type=OctetString
_RaidDescription_Object=MibScalar
raidDescription=_RaidDescription_Object((1,3,6,1,4,1,12532,34),_RaidDescription_Type())
raidDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:raidDescription.setStatus(_A)
_ClusterName_Type=OctetString
_ClusterName_Object=MibScalar
clusterName=_ClusterName_Object((1,3,6,1,4,1,12532,35),_ClusterName_Type())
clusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusterName.setStatus(_A)
_NodeList_Type=OctetString
_NodeList_Object=MibScalar
nodeList=_NodeList_Object((1,3,6,1,4,1,12532,36),_NodeList_Type())
nodeList.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeList.setStatus(_A)
_VipType_Type=OctetString
_VipType_Object=MibScalar
vipType=_VipType_Object((1,3,6,1,4,1,12532,37),_VipType_Type())
vipType.setMaxAccess(_D)
if mibBuilder.loadTexts:vipType.setStatus(_A)
_CurrentVIP_Type=OctetString
_CurrentVIP_Object=MibScalar
currentVIP=_CurrentVIP_Object((1,3,6,1,4,1,12532,38),_CurrentVIP_Type())
currentVIP.setMaxAccess(_D)
if mibBuilder.loadTexts:currentVIP.setStatus(_A)
_NewVIP_Type=OctetString
_NewVIP_Object=MibScalar
newVIP=_NewVIP_Object((1,3,6,1,4,1,12532,39),_NewVIP_Type())
newVIP.setMaxAccess(_D)
if mibBuilder.loadTexts:newVIP.setStatus(_A)
_NicEvent_Type=OctetString
_NicEvent_Object=MibScalar
nicEvent=_NicEvent_Object((1,3,6,1,4,1,12532,40),_NicEvent_Type())
nicEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:nicEvent.setStatus(_A)
_NodeName_Type=OctetString
_NodeName_Object=MibScalar
nodeName=_NodeName_Object((1,3,6,1,4,1,12532,41),_NodeName_Type())
nodeName.setMaxAccess(_D)
if mibBuilder.loadTexts:nodeName.setStatus(_A)
_IveTemperature_Type=Gauge32
_IveTemperature_Object=MibScalar
iveTemperature=_IveTemperature_Object((1,3,6,1,4,1,12532,42),_IveTemperature_Type())
iveTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:iveTemperature.setStatus(_A)
_IveTraps_ObjectIdentity=ObjectIdentity
iveTraps=_IveTraps_ObjectIdentity((1,3,6,1,4,1,12532,251))
_IveSAProduct_ObjectIdentity=ObjectIdentity
iveSAProduct=_IveSAProduct_ObjectIdentity((1,3,6,1,4,1,12532,252))
_IveProductSA700_ObjectIdentity=ObjectIdentity
iveProductSA700=_IveProductSA700_ObjectIdentity((1,3,6,1,4,1,12532,252,1))
_IveSA700_ObjectIdentity=ObjectIdentity
iveSA700=_IveSA700_ObjectIdentity((1,3,6,1,4,1,12532,252,1,1))
_IveProductSA2000_ObjectIdentity=ObjectIdentity
iveProductSA2000=_IveProductSA2000_ObjectIdentity((1,3,6,1,4,1,12532,252,2))
_IveSA2000_ObjectIdentity=ObjectIdentity
iveSA2000=_IveSA2000_ObjectIdentity((1,3,6,1,4,1,12532,252,2,1))
_IveProductSA2500_ObjectIdentity=ObjectIdentity
iveProductSA2500=_IveProductSA2500_ObjectIdentity((1,3,6,1,4,1,12532,252,3))
_IveSA2500_ObjectIdentity=ObjectIdentity
iveSA2500=_IveSA2500_ObjectIdentity((1,3,6,1,4,1,12532,252,3,1))
_IveProductSA4000_ObjectIdentity=ObjectIdentity
iveProductSA4000=_IveProductSA4000_ObjectIdentity((1,3,6,1,4,1,12532,252,4))
_IveSA4000_ObjectIdentity=ObjectIdentity
iveSA4000=_IveSA4000_ObjectIdentity((1,3,6,1,4,1,12532,252,4,1))
_IveSA4000FIPS_ObjectIdentity=ObjectIdentity
iveSA4000FIPS=_IveSA4000FIPS_ObjectIdentity((1,3,6,1,4,1,12532,252,4,2))
_IveProductSA4500_ObjectIdentity=ObjectIdentity
iveProductSA4500=_IveProductSA4500_ObjectIdentity((1,3,6,1,4,1,12532,252,5))
_IveSA4500_ObjectIdentity=ObjectIdentity
iveSA4500=_IveSA4500_ObjectIdentity((1,3,6,1,4,1,12532,252,5,1))
_IveSA4500FIPS_ObjectIdentity=ObjectIdentity
iveSA4500FIPS=_IveSA4500FIPS_ObjectIdentity((1,3,6,1,4,1,12532,252,5,2))
_IveProductSA6000_ObjectIdentity=ObjectIdentity
iveProductSA6000=_IveProductSA6000_ObjectIdentity((1,3,6,1,4,1,12532,252,6))
_IveSA6000_ObjectIdentity=ObjectIdentity
iveSA6000=_IveSA6000_ObjectIdentity((1,3,6,1,4,1,12532,252,6,1))
_IveSA6000FIPS_ObjectIdentity=ObjectIdentity
iveSA6000FIPS=_IveSA6000FIPS_ObjectIdentity((1,3,6,1,4,1,12532,252,6,2))
_IveProductSA6500_ObjectIdentity=ObjectIdentity
iveProductSA6500=_IveProductSA6500_ObjectIdentity((1,3,6,1,4,1,12532,252,7))
_IveSA6500_ObjectIdentity=ObjectIdentity
iveSA6500=_IveSA6500_ObjectIdentity((1,3,6,1,4,1,12532,252,7,1))
_IveSA6500FIPS_ObjectIdentity=ObjectIdentity
iveSA6500FIPS=_IveSA6500FIPS_ObjectIdentity((1,3,6,1,4,1,12532,252,7,2))
_IveICProduct_ObjectIdentity=ObjectIdentity
iveICProduct=_IveICProduct_ObjectIdentity((1,3,6,1,4,1,12532,253))
_IveProductIC4000_ObjectIdentity=ObjectIdentity
iveProductIC4000=_IveProductIC4000_ObjectIdentity((1,3,6,1,4,1,12532,253,1))
_IveIC4000_ObjectIdentity=ObjectIdentity
iveIC4000=_IveIC4000_ObjectIdentity((1,3,6,1,4,1,12532,253,1,1))
_IveProductIC4500_ObjectIdentity=ObjectIdentity
iveProductIC4500=_IveProductIC4500_ObjectIdentity((1,3,6,1,4,1,12532,253,2))
_IveIC4500_ObjectIdentity=ObjectIdentity
iveIC4500=_IveIC4500_ObjectIdentity((1,3,6,1,4,1,12532,253,2,1))
_IveProductIC6000_ObjectIdentity=ObjectIdentity
iveProductIC6000=_IveProductIC6000_ObjectIdentity((1,3,6,1,4,1,12532,253,3))
_IveIC6000_ObjectIdentity=ObjectIdentity
iveIC6000=_IveIC6000_ObjectIdentity((1,3,6,1,4,1,12532,253,3,1))
_IveIC6000FIPS_ObjectIdentity=ObjectIdentity
iveIC6000FIPS=_IveIC6000FIPS_ObjectIdentity((1,3,6,1,4,1,12532,253,3,2))
_IveProductIC6500_ObjectIdentity=ObjectIdentity
iveProductIC6500=_IveProductIC6500_ObjectIdentity((1,3,6,1,4,1,12532,253,4))
_IveIC6500_ObjectIdentity=ObjectIdentity
iveIC6500=_IveIC6500_ObjectIdentity((1,3,6,1,4,1,12532,253,4,1))
_IveMAGProduct_ObjectIdentity=ObjectIdentity
iveMAGProduct=_IveMAGProduct_ObjectIdentity((1,3,6,1,4,1,12532,254))
_IveProductMAG2600_ObjectIdentity=ObjectIdentity
iveProductMAG2600=_IveProductMAG2600_ObjectIdentity((1,3,6,1,4,1,12532,254,1))
_IveMAG2600_ObjectIdentity=ObjectIdentity
iveMAG2600=_IveMAG2600_ObjectIdentity((1,3,6,1,4,1,12532,254,1,1))
_IveProductMAG4610_ObjectIdentity=ObjectIdentity
iveProductMAG4610=_IveProductMAG4610_ObjectIdentity((1,3,6,1,4,1,12532,254,2))
_IveMAG4610_ObjectIdentity=ObjectIdentity
iveMAG4610=_IveMAG4610_ObjectIdentity((1,3,6,1,4,1,12532,254,2,1))
_IveProductSM160_ObjectIdentity=ObjectIdentity
iveProductSM160=_IveProductSM160_ObjectIdentity((1,3,6,1,4,1,12532,254,3))
_IveMAGSM160_ObjectIdentity=ObjectIdentity
iveMAGSM160=_IveMAGSM160_ObjectIdentity((1,3,6,1,4,1,12532,254,3,1))
_IveProductSM360_ObjectIdentity=ObjectIdentity
iveProductSM360=_IveProductSM360_ObjectIdentity((1,3,6,1,4,1,12532,254,4))
_IveMAGSM360_ObjectIdentity=ObjectIdentity
iveMAGSM360=_IveMAGSM360_ObjectIdentity((1,3,6,1,4,1,12532,254,4,1))
iveLogNearlyFull=NotificationType((1,3,6,1,4,1,12532,251,4))
iveLogNearlyFull.setObjects(*((_B,_H),(_B,_F)))
if mibBuilder.loadTexts:iveLogNearlyFull.setStatus(_A)
iveLogFull=NotificationType((1,3,6,1,4,1,12532,251,5))
iveLogFull.setObjects((_B,_F))
if mibBuilder.loadTexts:iveLogFull.setStatus(_A)
iveMaxConcurrentUsersSignedIn=NotificationType((1,3,6,1,4,1,12532,251,6))
if mibBuilder.loadTexts:iveMaxConcurrentUsersSignedIn.setStatus(_A)
iveTooManyFailedLoginAttempts=NotificationType((1,3,6,1,4,1,12532,251,7))
iveTooManyFailedLoginAttempts.setObjects((_B,_I))
if mibBuilder.loadTexts:iveTooManyFailedLoginAttempts.setStatus(_A)
externalAuthServerUnreachable=NotificationType((1,3,6,1,4,1,12532,251,8))
externalAuthServerUnreachable.setObjects((_B,_J))
if mibBuilder.loadTexts:externalAuthServerUnreachable.setStatus(_A)
iveStart=NotificationType((1,3,6,1,4,1,12532,251,9))
if mibBuilder.loadTexts:iveStart.setStatus(_A)
iveShutdown=NotificationType((1,3,6,1,4,1,12532,251,10))
if mibBuilder.loadTexts:iveShutdown.setStatus(_A)
iveReboot=NotificationType((1,3,6,1,4,1,12532,251,11))
if mibBuilder.loadTexts:iveReboot.setStatus(_A)
archiveServerUnreachable=NotificationType((1,3,6,1,4,1,12532,251,12))
if mibBuilder.loadTexts:archiveServerUnreachable.setStatus(_A)
archiveServerLoginFailed=NotificationType((1,3,6,1,4,1,12532,251,13))
if mibBuilder.loadTexts:archiveServerLoginFailed.setStatus(_A)
archiveFileTransferFailed=NotificationType((1,3,6,1,4,1,12532,251,14))
archiveFileTransferFailed.setObjects((_B,_K))
if mibBuilder.loadTexts:archiveFileTransferFailed.setStatus(_A)
meetingUserLimit=NotificationType((1,3,6,1,4,1,12532,251,15))
meetingUserLimit.setObjects((_B,_L))
if mibBuilder.loadTexts:meetingUserLimit.setStatus(_A)
iveRestart=NotificationType((1,3,6,1,4,1,12532,251,16))
if mibBuilder.loadTexts:iveRestart.setStatus(_A)
meetingLimit=NotificationType((1,3,6,1,4,1,12532,251,17))
meetingLimit.setObjects((_B,_M))
if mibBuilder.loadTexts:meetingLimit.setStatus(_A)
iveDiskNearlyFull=NotificationType((1,3,6,1,4,1,12532,251,18))
iveDiskNearlyFull.setObjects((_B,_N))
if mibBuilder.loadTexts:iveDiskNearlyFull.setStatus(_A)
iveDiskFull=NotificationType((1,3,6,1,4,1,12532,251,19))
if mibBuilder.loadTexts:iveDiskFull.setStatus(_A)
logMessageTrap=NotificationType((1,3,6,1,4,1,12532,251,20))
logMessageTrap.setObjects(*((_B,'logID'),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:logMessageTrap.setStatus(_A)
memUtilNotify=NotificationType((1,3,6,1,4,1,12532,251,21))
memUtilNotify.setObjects((_B,_Q))
if mibBuilder.loadTexts:memUtilNotify.setStatus(_A)
cpuUtilNotify=NotificationType((1,3,6,1,4,1,12532,251,22))
cpuUtilNotify.setObjects((_B,_R))
if mibBuilder.loadTexts:cpuUtilNotify.setStatus(_A)
swapUtilNotify=NotificationType((1,3,6,1,4,1,12532,251,23))
swapUtilNotify.setObjects((_B,_S))
if mibBuilder.loadTexts:swapUtilNotify.setStatus(_A)
iveMaxConcurrentUsersVirtualSystem=NotificationType((1,3,6,1,4,1,12532,251,24))
iveMaxConcurrentUsersVirtualSystem.setObjects((_B,_T))
if mibBuilder.loadTexts:iveMaxConcurrentUsersVirtualSystem.setStatus(_A)
ocspResponderConnectionFailed=NotificationType((1,3,6,1,4,1,12532,251,25))
ocspResponderConnectionFailed.setObjects((_B,_U))
if mibBuilder.loadTexts:ocspResponderConnectionFailed.setStatus(_A)
iveFanNotify=NotificationType((1,3,6,1,4,1,12532,251,26))
iveFanNotify.setObjects((_B,_V))
if mibBuilder.loadTexts:iveFanNotify.setStatus(_A)
ivePowerSupplyNotify=NotificationType((1,3,6,1,4,1,12532,251,27))
ivePowerSupplyNotify.setObjects((_B,_W))
if mibBuilder.loadTexts:ivePowerSupplyNotify.setStatus(_A)
iveRaidNotify=NotificationType((1,3,6,1,4,1,12532,251,28))
iveRaidNotify.setObjects((_B,_X))
if mibBuilder.loadTexts:iveRaidNotify.setStatus(_A)
iveClusterDisableNodeTrap=NotificationType((1,3,6,1,4,1,12532,251,29))
iveClusterDisableNodeTrap.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:iveClusterDisableNodeTrap.setStatus(_A)
iveClusterChangedVIPTrap=NotificationType((1,3,6,1,4,1,12532,251,30))
iveClusterChangedVIPTrap.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:iveClusterChangedVIPTrap.setStatus(_A)
iveNetExternalInterfaceDownTrap=NotificationType((1,3,6,1,4,1,12532,251,31))
iveNetExternalInterfaceDownTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:iveNetExternalInterfaceDownTrap.setStatus(_A)
iveClusterDeleteTrap=NotificationType((1,3,6,1,4,1,12532,251,32))
iveClusterDeleteTrap.setObjects((_B,_d))
if mibBuilder.loadTexts:iveClusterDeleteTrap.setStatus(_A)
iveNetInternalInterfaceDownTrap=NotificationType((1,3,6,1,4,1,12532,251,33))
iveNetInternalInterfaceDownTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:iveNetInternalInterfaceDownTrap.setStatus(_A)
iveNetManagementInterfaceDownTrap=NotificationType((1,3,6,1,4,1,12532,251,34))
iveNetManagementInterfaceDownTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:iveNetManagementInterfaceDownTrap.setStatus(_A)
iveTemperatureNotify=NotificationType((1,3,6,1,4,1,12532,251,35))
iveTemperatureNotify.setObjects((_B,_e))
if mibBuilder.loadTexts:iveTemperatureNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniper-ive':juniper_ive,_H:logFullPercent,'signedInWebUsers':signedInWebUsers,'signedInMailUsers':signedInMailUsers,_I:blockedIP,_J:authServerName,'productName':productName,'productVersion':productVersion,_K:fileName,_L:meetingUserCount,_R:iveCpuUtil,_Q:iveMemoryUtil,'iveConcurrentUsers':iveConcurrentUsers,'clusterConcurrentUsers':clusterConcurrentUsers,'iveTotalHits':iveTotalHits,'iveFileHits':iveFileHits,'iveWebHits':iveWebHits,'iveAppletHits':iveAppletHits,'ivetermHits':ivetermHits,'iveSAMHits':iveSAMHits,'iveNCHits':iveNCHits,'meetingHits':meetingHits,_M:meetingCount,_F:logName,_S:iveSwapUtil,_N:diskFullPercent,'blockedIPList':blockedIPList,'ipEntry':ipEntry,_G:ipIndex,'ipValue':ipValue,'logID':logID,_O:logType,_P:logDescription,_T:ivsName,_U:ocspResponderURL,_V:fanDescription,_W:psDescription,_X:raidDescription,_Y:clusterName,_Z:nodeList,_a:vipType,_b:currentVIP,_c:newVIP,_E:nicEvent,_d:nodeName,_e:iveTemperature,'iveTraps':iveTraps,'iveLogNearlyFull':iveLogNearlyFull,'iveLogFull':iveLogFull,'iveMaxConcurrentUsersSignedIn':iveMaxConcurrentUsersSignedIn,'iveTooManyFailedLoginAttempts':iveTooManyFailedLoginAttempts,'externalAuthServerUnreachable':externalAuthServerUnreachable,'iveStart':iveStart,'iveShutdown':iveShutdown,'iveReboot':iveReboot,'archiveServerUnreachable':archiveServerUnreachable,'archiveServerLoginFailed':archiveServerLoginFailed,'archiveFileTransferFailed':archiveFileTransferFailed,'meetingUserLimit':meetingUserLimit,'iveRestart':iveRestart,'meetingLimit':meetingLimit,'iveDiskNearlyFull':iveDiskNearlyFull,'iveDiskFull':iveDiskFull,'logMessageTrap':logMessageTrap,'memUtilNotify':memUtilNotify,'cpuUtilNotify':cpuUtilNotify,'swapUtilNotify':swapUtilNotify,'iveMaxConcurrentUsersVirtualSystem':iveMaxConcurrentUsersVirtualSystem,'ocspResponderConnectionFailed':ocspResponderConnectionFailed,'iveFanNotify':iveFanNotify,'ivePowerSupplyNotify':ivePowerSupplyNotify,'iveRaidNotify':iveRaidNotify,'iveClusterDisableNodeTrap':iveClusterDisableNodeTrap,'iveClusterChangedVIPTrap':iveClusterChangedVIPTrap,'iveNetExternalInterfaceDownTrap':iveNetExternalInterfaceDownTrap,'iveClusterDeleteTrap':iveClusterDeleteTrap,'iveNetInternalInterfaceDownTrap':iveNetInternalInterfaceDownTrap,'iveNetManagementInterfaceDownTrap':iveNetManagementInterfaceDownTrap,'iveTemperatureNotify':iveTemperatureNotify,'iveSAProduct':iveSAProduct,'iveProductSA700':iveProductSA700,'iveSA700':iveSA700,'iveProductSA2000':iveProductSA2000,'iveSA2000':iveSA2000,'iveProductSA2500':iveProductSA2500,'iveSA2500':iveSA2500,'iveProductSA4000':iveProductSA4000,'iveSA4000':iveSA4000,'iveSA4000FIPS':iveSA4000FIPS,'iveProductSA4500':iveProductSA4500,'iveSA4500':iveSA4500,'iveSA4500FIPS':iveSA4500FIPS,'iveProductSA6000':iveProductSA6000,'iveSA6000':iveSA6000,'iveSA6000FIPS':iveSA6000FIPS,'iveProductSA6500':iveProductSA6500,'iveSA6500':iveSA6500,'iveSA6500FIPS':iveSA6500FIPS,'iveICProduct':iveICProduct,'iveProductIC4000':iveProductIC4000,'iveIC4000':iveIC4000,'iveProductIC4500':iveProductIC4500,'iveIC4500':iveIC4500,'iveProductIC6000':iveProductIC6000,'iveIC6000':iveIC6000,'iveIC6000FIPS':iveIC6000FIPS,'iveProductIC6500':iveProductIC6500,'iveIC6500':iveIC6500,'iveMAGProduct':iveMAGProduct,'iveProductMAG2600':iveProductMAG2600,'iveMAG2600':iveMAG2600,'iveProductMAG4610':iveProductMAG4610,'iveMAG4610':iveMAG4610,'iveProductSM160':iveProductSM160,'iveMAGSM160':iveMAGSM160,'iveProductSM360':iveProductSM360,'iveMAGSM360':iveMAGSM360})