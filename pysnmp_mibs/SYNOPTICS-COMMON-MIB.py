_A2='s3CommonBoardIndex'
_A1='s3SlotNumber'
_A0='s3AgentTrapRcvrNetAddress'
_z='localAsBackup'
_y='localConfig'
_x='remoteConfig'
_w='m331xS'
_v='m332xS'
_u='m3299F'
_t='m3299U'
_s='m3299C'
_r='m3513SA'
_q='m3522A'
_p='m3314SA'
_o='m3313SA'
_n='m3517SA'
_m='m3308B'
_l='m3304A'
_k='m3910SA'
_j='m3307HD'
_i='m3314A'
_h='m3313A'
_g='m2912A'
_f='m3902A'
_e='m3505B'
_d='m3502B'
_c='m3040S'
_b='m3395A'
_a='m3100R'
_Z='m3505A'
_Y='m3308A'
_X='m3314M-ST'
_W='m3314-ST'
_V='m3313M'
_U='bothFail'
_T='secondaryFail'
_S='primaryFail'
_R='m2310x'
_Q='m2300x'
_P='m3522'
_O='m3395'
_N='m3394'
_M='m3910S'
_L='m3356'
_K='fail'
_J='SYNOPTICS-COMMON-MIB'
_I='deprecated'
_H='ok'
_G='OctetString'
_F='DisplayString'
_E='other'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
SnpxBackplaneType,SnpxChassisType,s3SnmpAgent,series3000=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','SnpxBackplaneType','SnpxChassisType','s3SnmpAgent','series3000')
class S3ModuleType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129)));namedValues=NamedValues(*(('empty',1),(_E,2),('m3302',3),('m3304-ST',4),('m3305',5),('m3308',6),('m3313',7),(_V,8),(_W,9),(_X,10),('m3323',11),('m3324-ST',12),('m3502',13),('m3532',14),('m3552',15),('m3301',16),('m3307',17),(_L,18),('m3512',19),('m3514',20),('m3505',21),('m3554',22),('m3534',23),('m3383',24),('m3384',25),('m331x',26),('m351x',27),('m3502-A',28),('m3902',29),('m3904',30),(_M,31),('m3386',32),(_N,33),(_O,34),('m3323S',35),('m3324S-ST',36),('m3307A',37),(_Y,38),(_Z,39),('m3513',40),('m3333',41),('m3334-ST',42),('m3040',43),(_a,44),('notUsed45',45),('notUsed46',46),('m2810-hm',47),('m2810-nmm',48),('m3313S',49),('m3314S',50),('m3368',51),('m3512S',52),('m3513S',53),('m3514S',54),(_P,55),('m2912',56),('m2914',57),('notUsed58',58),('m3301-75',59),('m3301-93',60),('m271x-nmm',61),('m2705-hm',62),('m2715-hm',63),('m2813-nmm',64),('m2814-nmm',65),('m2813-hm',66),('m2814-hm',67),('m2803-hm',68),('m2804-hm',69),(_b,70),(_c,71),(_d,72),(_e,73),('m2715-F-hm',74),('m2712-hm',75),('m2712-F-hm',76),('m2702-hm',77),('m2702-C-hm',78),('m2705-F-hm',79),('m2702-F-hm',80),('m2705-C-hm',81),(_f,82),(_g,83),(_h,84),(_i,85),(_j,86),('m3328',87),('m3904-2SM',88),('m3910S-SM',89),('m3800',90),('m3910S-SD',91),('m3904-4SM',92),('m2915',93),(_k,94),('m3910SA-SM',95),('m3905',96),('m2715B-hm',97),('m2705B-hm',98),('m2715B-F-hm',99),('m2712B-hm',100),('m2712B-F-hm',101),('m2702B-C-hm',102),(_l,103),('m3486',104),(_m,105),('m2813SA-nmm',106),('m2814SA-nmm',107),(_n,108),('m810M',109),(_o,110),(_p,111),(_q,112),('m3504-ST',113),(_r,114),('mAlcatel-Eth-nmm',115),('mAlcatel-Eth-hm1',116),('mAlcatel-Eth-hm',117),('m2486-nmm',118),('m2486-hm',119),('m3174',120),('m271xSA-nmm',121),(_s,122),(_t,123),(_u,124),(_Q,125),(_R,126),('m3410',127),('m3405',128),('m3475',129)))
class S3PsType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('low',2),('medium',3),('high',4),('redundantCapable',5),('empty',6)))
_S3AgentSw_ObjectIdentity=ObjectIdentity
s3AgentSw=_S3AgentSw_ObjectIdentity((1,3,6,1,4,1,45,1,2,1))
class _S3AgentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*((_E,1),('m3313',2),(_V,3),(_W,4),(_X,5),('m2310',6),('m3512',7),('m3514',8),('m332x',9),(_L,10),(_v,11),(_M,12),(_O,13),(_N,14),('m3513',15),(_w,16),('m291x',17),('m271x',18),('m281x',19),('m331xA',20),(_P,21),('m2722',22),('m281xSA',23),('m810M',24),('m351xSA',25),('m331xSA',26),('m271xSA',27),('m2486',28),(_Q,29),(_R,30)))
_S3AgentType_Type.__name__=_C
_S3AgentType_Object=MibScalar
s3AgentType=_S3AgentType_Object((1,3,6,1,4,1,45,1,2,1,1),_S3AgentType_Type())
s3AgentType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentType.setStatus(_A)
_S3AgentFwVer_Type=Integer32
_S3AgentFwVer_Object=MibScalar
s3AgentFwVer=_S3AgentFwVer_Object((1,3,6,1,4,1,45,1,2,1,2),_S3AgentFwVer_Type())
s3AgentFwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentFwVer.setStatus(_A)
_S3AgentSwMajorVer_Type=Integer32
_S3AgentSwMajorVer_Object=MibScalar
s3AgentSwMajorVer=_S3AgentSwMajorVer_Object((1,3,6,1,4,1,45,1,2,1,3),_S3AgentSwMajorVer_Type())
s3AgentSwMajorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentSwMajorVer.setStatus(_A)
_S3AgentSwMinorVer_Type=Integer32
_S3AgentSwMinorVer_Object=MibScalar
s3AgentSwMinorVer=_S3AgentSwMinorVer_Object((1,3,6,1,4,1,45,1,2,1,4),_S3AgentSwMinorVer_Type())
s3AgentSwMinorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentSwMinorVer.setStatus(_A)
class _S3AgentBootProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('bootp-tftp',2),('tftp-only',3),('ieee802-1e',4),('proprietary',5),('dll-download',6)))
_S3AgentBootProtocol_Type.__name__=_C
_S3AgentBootProtocol_Object=MibScalar
s3AgentBootProtocol=_S3AgentBootProtocol_Object((1,3,6,1,4,1,45,1,2,1,5),_S3AgentBootProtocol_Type())
s3AgentBootProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentBootProtocol.setStatus(_A)
class _S3AgentBootFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_S3AgentBootFile_Type.__name__=_F
_S3AgentBootFile_Object=MibScalar
s3AgentBootFile=_S3AgentBootFile_Object((1,3,6,1,4,1,45,1,2,1,6),_S3AgentBootFile_Type())
s3AgentBootFile.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentBootFile.setStatus(_A)
class _S3AgentAuthTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_S3AgentAuthTrap_Type.__name__=_C
_S3AgentAuthTrap_Object=MibScalar
s3AgentAuthTrap=_S3AgentAuthTrap_Object((1,3,6,1,4,1,45,1,2,1,7),_S3AgentAuthTrap_Type())
s3AgentAuthTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentAuthTrap.setStatus(_I)
class _S3AgentLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_S3AgentLocation_Type.__name__=_F
_S3AgentLocation_Object=MibScalar
s3AgentLocation=_S3AgentLocation_Object((1,3,6,1,4,1,45,1,2,1,8),_S3AgentLocation_Type())
s3AgentLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentLocation.setStatus(_I)
_S3AgentMibLevel_Type=Integer32
_S3AgentMibLevel_Object=MibScalar
s3AgentMibLevel=_S3AgentMibLevel_Object((1,3,6,1,4,1,45,1,2,1,9),_S3AgentMibLevel_Type())
s3AgentMibLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentMibLevel.setStatus(_A)
_S3AgentFeatureLevel_Type=Integer32
_S3AgentFeatureLevel_Object=MibScalar
s3AgentFeatureLevel=_S3AgentFeatureLevel_Object((1,3,6,1,4,1,45,1,2,1,10),_S3AgentFeatureLevel_Type())
s3AgentFeatureLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentFeatureLevel.setStatus(_I)
_S3AgentMySlotId_Type=Integer32
_S3AgentMySlotId_Object=MibScalar
s3AgentMySlotId=_S3AgentMySlotId_Object((1,3,6,1,4,1,45,1,2,1,11),_S3AgentMySlotId_Type())
s3AgentMySlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentMySlotId.setStatus(_A)
_S3AgentUnAuthIp_Type=IpAddress
_S3AgentUnAuthIp_Object=MibScalar
s3AgentUnAuthIp=_S3AgentUnAuthIp_Object((1,3,6,1,4,1,45,1,2,1,12),_S3AgentUnAuthIp_Type())
s3AgentUnAuthIp.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentUnAuthIp.setStatus(_A)
class _S3AgentUnAuthComm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_S3AgentUnAuthComm_Type.__name__=_G
_S3AgentUnAuthComm_Object=MibScalar
s3AgentUnAuthComm=_S3AgentUnAuthComm_Object((1,3,6,1,4,1,45,1,2,1,13),_S3AgentUnAuthComm_Type())
s3AgentUnAuthComm.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentUnAuthComm.setStatus(_A)
class _S3AgentSwLicenseCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_S3AgentSwLicenseCode_Type.__name__=_F
_S3AgentSwLicenseCode_Object=MibScalar
s3AgentSwLicenseCode=_S3AgentSwLicenseCode_Object((1,3,6,1,4,1,45,1,2,1,14),_S3AgentSwLicenseCode_Type())
s3AgentSwLicenseCode.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentSwLicenseCode.setStatus(_A)
_S3AgentPerformance_Type=Counter32
_S3AgentPerformance_Object=MibScalar
s3AgentPerformance=_S3AgentPerformance_Object((1,3,6,1,4,1,45,1,2,1,15),_S3AgentPerformance_Type())
s3AgentPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentPerformance.setStatus(_A)
_S3AgentSwMaintVer_Type=Integer32
_S3AgentSwMaintVer_Object=MibScalar
s3AgentSwMaintVer=_S3AgentSwMaintVer_Object((1,3,6,1,4,1,45,1,2,1,16),_S3AgentSwMaintVer_Type())
s3AgentSwMaintVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentSwMaintVer.setStatus(_A)
class _S3AgentConfigLoadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_x,2),(_y,3),(_z,4)))
_S3AgentConfigLoadMode_Type.__name__=_C
_S3AgentConfigLoadMode_Object=MibScalar
s3AgentConfigLoadMode=_S3AgentConfigLoadMode_Object((1,3,6,1,4,1,45,1,2,1,17),_S3AgentConfigLoadMode_Type())
s3AgentConfigLoadMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentConfigLoadMode.setStatus(_A)
class _S3AgentConfigActualSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_x,2),(_y,3)))
_S3AgentConfigActualSource_Type.__name__=_C
_S3AgentConfigActualSource_Object=MibScalar
s3AgentConfigActualSource=_S3AgentConfigActualSource_Object((1,3,6,1,4,1,45,1,2,1,18),_S3AgentConfigActualSource_Type())
s3AgentConfigActualSource.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentConfigActualSource.setStatus(_A)
class _S3AgentMgmtProtoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('ip',2),('ipx',3),('ipAndIpx',4)))
_S3AgentMgmtProtoMode_Type.__name__=_C
_S3AgentMgmtProtoMode_Object=MibScalar
s3AgentMgmtProtoMode=_S3AgentMgmtProtoMode_Object((1,3,6,1,4,1,45,1,2,1,19),_S3AgentMgmtProtoMode_Type())
s3AgentMgmtProtoMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentMgmtProtoMode.setStatus(_A)
class _S3AgentActualMgmtProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('ip',2),('ipx',3),('ipAndIpx',4)))
_S3AgentActualMgmtProtocol_Type.__name__=_C
_S3AgentActualMgmtProtocol_Object=MibScalar
s3AgentActualMgmtProtocol=_S3AgentActualMgmtProtocol_Object((1,3,6,1,4,1,45,1,2,1,20),_S3AgentActualMgmtProtocol_Type())
s3AgentActualMgmtProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentActualMgmtProtocol.setStatus(_A)
class _S3AgentImageFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_S3AgentImageFile_Type.__name__=_F
_S3AgentImageFile_Object=MibScalar
s3AgentImageFile=_S3AgentImageFile_Object((1,3,6,1,4,1,45,1,2,1,21),_S3AgentImageFile_Type())
s3AgentImageFile.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentImageFile.setStatus(_A)
_S3AgentNetProtocol_ObjectIdentity=ObjectIdentity
s3AgentNetProtocol=_S3AgentNetProtocol_ObjectIdentity((1,3,6,1,4,1,45,1,2,2))
_S3AgentIpProtocol_ObjectIdentity=ObjectIdentity
s3AgentIpProtocol=_S3AgentIpProtocol_ObjectIdentity((1,3,6,1,4,1,45,1,2,2,1))
_S3AgentIpAddr_Type=IpAddress
_S3AgentIpAddr_Object=MibScalar
s3AgentIpAddr=_S3AgentIpAddr_Object((1,3,6,1,4,1,45,1,2,2,1,1),_S3AgentIpAddr_Type())
s3AgentIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentIpAddr.setStatus(_A)
_S3AgentNetMask_Type=IpAddress
_S3AgentNetMask_Object=MibScalar
s3AgentNetMask=_S3AgentNetMask_Object((1,3,6,1,4,1,45,1,2,2,1,2),_S3AgentNetMask_Type())
s3AgentNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentNetMask.setStatus(_A)
_S3AgentDefaultGateway_Type=IpAddress
_S3AgentDefaultGateway_Object=MibScalar
s3AgentDefaultGateway=_S3AgentDefaultGateway_Object((1,3,6,1,4,1,45,1,2,2,1,3),_S3AgentDefaultGateway_Type())
s3AgentDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentDefaultGateway.setStatus(_A)
_S3AgentBootServerAddr_Type=IpAddress
_S3AgentBootServerAddr_Object=MibScalar
s3AgentBootServerAddr=_S3AgentBootServerAddr_Object((1,3,6,1,4,1,45,1,2,2,1,4),_S3AgentBootServerAddr_Type())
s3AgentBootServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentBootServerAddr.setStatus(_A)
_S3AgentSecDefaultGateway_Type=IpAddress
_S3AgentSecDefaultGateway_Object=MibScalar
s3AgentSecDefaultGateway=_S3AgentSecDefaultGateway_Object((1,3,6,1,4,1,45,1,2,2,1,5),_S3AgentSecDefaultGateway_Type())
s3AgentSecDefaultGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentSecDefaultGateway.setStatus(_A)
class _S3AgentPingDefaultRtrSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('on',2),('off',3)))
_S3AgentPingDefaultRtrSwitch_Type.__name__=_C
_S3AgentPingDefaultRtrSwitch_Object=MibScalar
s3AgentPingDefaultRtrSwitch=_S3AgentPingDefaultRtrSwitch_Object((1,3,6,1,4,1,45,1,2,2,1,6),_S3AgentPingDefaultRtrSwitch_Type())
s3AgentPingDefaultRtrSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentPingDefaultRtrSwitch.setStatus(_A)
_S3AgentPingDefaultRtrTime_Type=TimeTicks
_S3AgentPingDefaultRtrTime_Object=MibScalar
s3AgentPingDefaultRtrTime=_S3AgentPingDefaultRtrTime_Object((1,3,6,1,4,1,45,1,2,2,1,7),_S3AgentPingDefaultRtrTime_Type())
s3AgentPingDefaultRtrTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentPingDefaultRtrTime.setStatus(_A)
_S3AgentBootRouter_Type=IpAddress
_S3AgentBootRouter_Object=MibScalar
s3AgentBootRouter=_S3AgentBootRouter_Object((1,3,6,1,4,1,45,1,2,2,1,8),_S3AgentBootRouter_Type())
s3AgentBootRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentBootRouter.setStatus(_A)
_S3AgentTrapReceiverTable_Object=MibTable
s3AgentTrapReceiverTable=_S3AgentTrapReceiverTable_Object((1,3,6,1,4,1,45,1,2,3))
if mibBuilder.loadTexts:s3AgentTrapReceiverTable.setStatus(_A)
_S3AgentTrapReceiverEntry_Object=MibTableRow
s3AgentTrapReceiverEntry=_S3AgentTrapReceiverEntry_Object((1,3,6,1,4,1,45,1,2,3,1))
s3AgentTrapReceiverEntry.setIndexNames((0,_J,_A0))
if mibBuilder.loadTexts:s3AgentTrapReceiverEntry.setStatus(_A)
class _S3AgentTrapRcvrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('valid',2),('invalid',3)))
_S3AgentTrapRcvrStatus_Type.__name__=_C
_S3AgentTrapRcvrStatus_Object=MibTableColumn
s3AgentTrapRcvrStatus=_S3AgentTrapRcvrStatus_Object((1,3,6,1,4,1,45,1,2,3,1,1),_S3AgentTrapRcvrStatus_Type())
s3AgentTrapRcvrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentTrapRcvrStatus.setStatus(_A)
class _S3AgentTrapRcvrNetAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_S3AgentTrapRcvrNetAddress_Type.__name__=_G
_S3AgentTrapRcvrNetAddress_Object=MibTableColumn
s3AgentTrapRcvrNetAddress=_S3AgentTrapRcvrNetAddress_Object((1,3,6,1,4,1,45,1,2,3,1,2),_S3AgentTrapRcvrNetAddress_Type())
s3AgentTrapRcvrNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentTrapRcvrNetAddress.setStatus(_A)
class _S3AgentTrapRcvrComm_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_S3AgentTrapRcvrComm_Type.__name__=_G
_S3AgentTrapRcvrComm_Object=MibTableColumn
s3AgentTrapRcvrComm=_S3AgentTrapRcvrComm_Object((1,3,6,1,4,1,45,1,2,3,1,3),_S3AgentTrapRcvrComm_Type())
s3AgentTrapRcvrComm.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentTrapRcvrComm.setStatus(_A)
_S3AgentTrapRcvrAgeTime_Type=TimeTicks
_S3AgentTrapRcvrAgeTime_Object=MibTableColumn
s3AgentTrapRcvrAgeTime=_S3AgentTrapRcvrAgeTime_Object((1,3,6,1,4,1,45,1,2,3,1,4),_S3AgentTrapRcvrAgeTime_Type())
s3AgentTrapRcvrAgeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentTrapRcvrAgeTime.setStatus(_A)
_S3AgentHw_ObjectIdentity=ObjectIdentity
s3AgentHw=_S3AgentHw_ObjectIdentity((1,3,6,1,4,1,45,1,2,4))
class _S3AgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('offline',1),('online',2)))
_S3AgentStatus_Type.__name__=_C
_S3AgentStatus_Object=MibScalar
s3AgentStatus=_S3AgentStatus_Object((1,3,6,1,4,1,45,1,2,4,1),_S3AgentStatus_Type())
s3AgentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentStatus.setStatus(_A)
_S3AgentMdaHwVer_Type=Integer32
_S3AgentMdaHwVer_Object=MibScalar
s3AgentMdaHwVer=_S3AgentMdaHwVer_Object((1,3,6,1,4,1,45,1,2,4,2),_S3AgentMdaHwVer_Type())
s3AgentMdaHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentMdaHwVer.setStatus(_A)
class _S3AgentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),(_E,3)))
_S3AgentMode_Type.__name__=_C
_S3AgentMode_Object=MibScalar
s3AgentMode=_S3AgentMode_Object((1,3,6,1,4,1,45,1,2,4,3),_S3AgentMode_Type())
s3AgentMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentMode.setStatus(_A)
class _S3AgentReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_S3AgentReset_Type.__name__=_C
_S3AgentReset_Object=MibScalar
s3AgentReset=_S3AgentReset_Object((1,3,6,1,4,1,45,1,2,4,4),_S3AgentReset_Type())
s3AgentReset.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentReset.setStatus(_A)
class _S3AgentRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noRestart',1),('restart',2)))
_S3AgentRestart_Type.__name__=_C
_S3AgentRestart_Object=MibScalar
s3AgentRestart=_S3AgentRestart_Object((1,3,6,1,4,1,45,1,2,4,5),_S3AgentRestart_Type())
s3AgentRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentRestart.setStatus(_A)
class _S3AgentBootMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('eeprom',1),('net',2),('otherCase',3)))
_S3AgentBootMode_Type.__name__=_C
_S3AgentBootMode_Object=MibScalar
s3AgentBootMode=_S3AgentBootMode_Object((1,3,6,1,4,1,45,1,2,4,6),_S3AgentBootMode_Type())
s3AgentBootMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentBootMode.setStatus(_A)
class _S3AgentWriteEeprom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noWriteEeprom',1),('writeEeprom',2)))
_S3AgentWriteEeprom_Type.__name__=_C
_S3AgentWriteEeprom_Object=MibScalar
s3AgentWriteEeprom=_S3AgentWriteEeprom_Object((1,3,6,1,4,1,45,1,2,4,7),_S3AgentWriteEeprom_Type())
s3AgentWriteEeprom.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentWriteEeprom.setStatus(_A)
_S3AgentBaudRate_Type=Gauge32
_S3AgentBaudRate_Object=MibScalar
s3AgentBaudRate=_S3AgentBaudRate_Object((1,3,6,1,4,1,45,1,2,4,8),_S3AgentBaudRate_Type())
s3AgentBaudRate.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentBaudRate.setStatus(_A)
class _S3AgentInitString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_S3AgentInitString_Type.__name__=_F
_S3AgentInitString_Object=MibScalar
s3AgentInitString=_S3AgentInitString_Object((1,3,6,1,4,1,45,1,2,4,9),_S3AgentInitString_Type())
s3AgentInitString.setMaxAccess(_D)
if mibBuilder.loadTexts:s3AgentInitString.setStatus(_A)
_S3AgentEepromSize_Type=Integer32
_S3AgentEepromSize_Object=MibScalar
s3AgentEepromSize=_S3AgentEepromSize_Object((1,3,6,1,4,1,45,1,2,4,10),_S3AgentEepromSize_Type())
s3AgentEepromSize.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentEepromSize.setStatus(_A)
_S3AgentEpromSize_Type=Integer32
_S3AgentEpromSize_Object=MibScalar
s3AgentEpromSize=_S3AgentEpromSize_Object((1,3,6,1,4,1,45,1,2,4,11),_S3AgentEpromSize_Type())
s3AgentEpromSize.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentEpromSize.setStatus(_A)
_S3AgentDramSize_Type=Integer32
_S3AgentDramSize_Object=MibScalar
s3AgentDramSize=_S3AgentDramSize_Object((1,3,6,1,4,1,45,1,2,4,12),_S3AgentDramSize_Type())
s3AgentDramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentDramSize.setStatus(_A)
class _S3AgentHexDisplay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_S3AgentHexDisplay_Type.__name__=_F
_S3AgentHexDisplay_Object=MibScalar
s3AgentHexDisplay=_S3AgentHexDisplay_Object((1,3,6,1,4,1,45,1,2,4,13),_S3AgentHexDisplay_Type())
s3AgentHexDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentHexDisplay.setStatus(_A)
class _S3AgentFlashStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_K,3)))
_S3AgentFlashStatus_Type.__name__=_C
_S3AgentFlashStatus_Object=MibScalar
s3AgentFlashStatus=_S3AgentFlashStatus_Object((1,3,6,1,4,1,45,1,2,4,14),_S3AgentFlashStatus_Type())
s3AgentFlashStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3AgentFlashStatus.setStatus(_A)
_S3AgentSpecific_ObjectIdentity=ObjectIdentity
s3AgentSpecific=_S3AgentSpecific_ObjectIdentity((1,3,6,1,4,1,45,1,2,5))
_S3AgentLocImage_ObjectIdentity=ObjectIdentity
s3AgentLocImage=_S3AgentLocImage_ObjectIdentity((1,3,6,1,4,1,45,1,2,6))
class _S3LocImageValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('localImageValid',2),('localImageInvalid',3)))
_S3LocImageValid_Type.__name__=_C
_S3LocImageValid_Object=MibScalar
s3LocImageValid=_S3LocImageValid_Object((1,3,6,1,4,1,45,1,2,6,1),_S3LocImageValid_Type())
s3LocImageValid.setMaxAccess(_B)
if mibBuilder.loadTexts:s3LocImageValid.setStatus(_A)
_S3LocImageMajorVersion_Type=Integer32
_S3LocImageMajorVersion_Object=MibScalar
s3LocImageMajorVersion=_S3LocImageMajorVersion_Object((1,3,6,1,4,1,45,1,2,6,2),_S3LocImageMajorVersion_Type())
s3LocImageMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:s3LocImageMajorVersion.setStatus(_A)
_S3LocImageMinorVersion_Type=Integer32
_S3LocImageMinorVersion_Object=MibScalar
s3LocImageMinorVersion=_S3LocImageMinorVersion_Object((1,3,6,1,4,1,45,1,2,6,3),_S3LocImageMinorVersion_Type())
s3LocImageMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:s3LocImageMinorVersion.setStatus(_A)
class _S3LocImageLoadMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('remoteBoot',2),('localBoot',3),(_z,4),('remoteNoUpdate',5),('remoteNewUpdate',6),('localAutoUpdate',7)))
_S3LocImageLoadMode_Type.__name__=_C
_S3LocImageLoadMode_Object=MibScalar
s3LocImageLoadMode=_S3LocImageLoadMode_Object((1,3,6,1,4,1,45,1,2,6,4),_S3LocImageLoadMode_Type())
s3LocImageLoadMode.setMaxAccess(_D)
if mibBuilder.loadTexts:s3LocImageLoadMode.setStatus(_A)
class _S3LocImageActualSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('remoteImage',2),('localImage',3)))
_S3LocImageActualSource_Type.__name__=_C
_S3LocImageActualSource_Object=MibScalar
s3LocImageActualSource=_S3LocImageActualSource_Object((1,3,6,1,4,1,45,1,2,6,5),_S3LocImageActualSource_Type())
s3LocImageActualSource.setMaxAccess(_B)
if mibBuilder.loadTexts:s3LocImageActualSource.setStatus(_A)
_S3LocImageMaintVersion_Type=Integer32
_S3LocImageMaintVersion_Object=MibScalar
s3LocImageMaintVersion=_S3LocImageMaintVersion_Object((1,3,6,1,4,1,45,1,2,6,6),_S3LocImageMaintVersion_Type())
s3LocImageMaintVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:s3LocImageMaintVersion.setStatus(_A)
_S3000Chassis_ObjectIdentity=ObjectIdentity
s3000Chassis=_S3000Chassis_ObjectIdentity((1,3,6,1,4,1,45,1,3,1))
_S3ChassisType_Type=SnpxChassisType
_S3ChassisType_Object=MibScalar
s3ChassisType=_S3ChassisType_Object((1,3,6,1,4,1,45,1,3,1,1),_S3ChassisType_Type())
s3ChassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisType.setStatus(_A)
_S3ChassisBkplType_Type=SnpxBackplaneType
_S3ChassisBkplType_Object=MibScalar
s3ChassisBkplType=_S3ChassisBkplType_Object((1,3,6,1,4,1,45,1,3,1,2),_S3ChassisBkplType_Type())
s3ChassisBkplType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisBkplType.setStatus(_A)
_S3ChassisBkplRev_Type=Integer32
_S3ChassisBkplRev_Object=MibScalar
s3ChassisBkplRev=_S3ChassisBkplRev_Object((1,3,6,1,4,1,45,1,3,1,3),_S3ChassisBkplRev_Type())
s3ChassisBkplRev.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisBkplRev.setStatus(_A)
_S3ChassisPsType_Type=S3PsType
_S3ChassisPsType_Object=MibScalar
s3ChassisPsType=_S3ChassisPsType_Object((1,3,6,1,4,1,45,1,3,1,4),_S3ChassisPsType_Type())
s3ChassisPsType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisPsType.setStatus(_A)
class _S3ChassisPsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_S,2),(_T,3),(_U,4)))
_S3ChassisPsStatus_Type.__name__=_C
_S3ChassisPsStatus_Object=MibScalar
s3ChassisPsStatus=_S3ChassisPsStatus_Object((1,3,6,1,4,1,45,1,3,1,5),_S3ChassisPsStatus_Type())
s3ChassisPsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisPsStatus.setStatus(_A)
class _S3ChassisFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_K,2),(_E,3)))
_S3ChassisFanStatus_Type.__name__=_C
_S3ChassisFanStatus_Object=MibScalar
s3ChassisFanStatus=_S3ChassisFanStatus_Object((1,3,6,1,4,1,45,1,3,1,6),_S3ChassisFanStatus_Type())
s3ChassisFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisFanStatus.setStatus(_A)
_S3SlotConfigTable_Object=MibTable
s3SlotConfigTable=_S3SlotConfigTable_Object((1,3,6,1,4,1,45,1,3,1,7))
if mibBuilder.loadTexts:s3SlotConfigTable.setStatus(_A)
_S3SlotConfigEntry_Object=MibTableRow
s3SlotConfigEntry=_S3SlotConfigEntry_Object((1,3,6,1,4,1,45,1,3,1,7,1))
s3SlotConfigEntry.setIndexNames((0,_J,_A1))
if mibBuilder.loadTexts:s3SlotConfigEntry.setStatus(_A)
_S3SlotNumber_Type=Integer32
_S3SlotNumber_Object=MibTableColumn
s3SlotNumber=_S3SlotNumber_Object((1,3,6,1,4,1,45,1,3,1,7,1,1),_S3SlotNumber_Type())
s3SlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotNumber.setStatus(_A)
_S3SlotModuleId_Type=Integer32
_S3SlotModuleId_Object=MibTableColumn
s3SlotModuleId=_S3SlotModuleId_Object((1,3,6,1,4,1,45,1,3,1,7,1,2),_S3SlotModuleId_Type())
s3SlotModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotModuleId.setStatus(_A)
_S3SlotModuleType_Type=S3ModuleType
_S3SlotModuleType_Object=MibTableColumn
s3SlotModuleType=_S3SlotModuleType_Object((1,3,6,1,4,1,45,1,3,1,7,1,3),_S3SlotModuleType_Type())
s3SlotModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotModuleType.setStatus(_I)
class _S3SlotModuleDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_S3SlotModuleDescr_Type.__name__=_F
_S3SlotModuleDescr_Object=MibTableColumn
s3SlotModuleDescr=_S3SlotModuleDescr_Object((1,3,6,1,4,1,45,1,3,1,7,1,4),_S3SlotModuleDescr_Type())
s3SlotModuleDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotModuleDescr.setStatus(_A)
class _S3SlotModuleLed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_S3SlotModuleLed_Type.__name__=_G
_S3SlotModuleLed_Object=MibTableColumn
s3SlotModuleLed=_S3SlotModuleLed_Object((1,3,6,1,4,1,45,1,3,1,7,1,5),_S3SlotModuleLed_Type())
s3SlotModuleLed.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotModuleLed.setStatus(_A)
_S3SlotModuleMdaId_Type=Integer32
_S3SlotModuleMdaId_Object=MibTableColumn
s3SlotModuleMdaId=_S3SlotModuleMdaId_Object((1,3,6,1,4,1,45,1,3,1,7,1,6),_S3SlotModuleMdaId_Type())
s3SlotModuleMdaId.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotModuleMdaId.setStatus(_A)
_S3CommonBoardTable_Object=MibTable
s3CommonBoardTable=_S3CommonBoardTable_Object((1,3,6,1,4,1,45,1,3,1,8))
if mibBuilder.loadTexts:s3CommonBoardTable.setStatus(_A)
_S3CommonBoardEntry_Object=MibTableRow
s3CommonBoardEntry=_S3CommonBoardEntry_Object((1,3,6,1,4,1,45,1,3,1,8,1))
s3CommonBoardEntry.setIndexNames((0,_J,_A2))
if mibBuilder.loadTexts:s3CommonBoardEntry.setStatus(_A)
_S3CommonBoardIndex_Type=Integer32
_S3CommonBoardIndex_Object=MibTableColumn
s3CommonBoardIndex=_S3CommonBoardIndex_Object((1,3,6,1,4,1,45,1,3,1,8,1,1),_S3CommonBoardIndex_Type())
s3CommonBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardIndex.setStatus(_A)
class _S3CommonBoardId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,88,101,102,103,104,105,106,107,108,109,110,114,115,116,117,119,120,121,122,250,251,252)));namedValues=NamedValues(*(('m331x',1),('m3302',2),('m332x',3),('m3304ST',4),('m3305',5),('m333x',6),('m3307',7),('m3308',8),('m3301',9),('m3904',10),('m3902',11),(_M,12),(_w,14),(_a,15),('m3502',16),('m3502A',17),('m353x',18),('m3040',19),('m3505',20),(_Z,21),('m355x',22),(_c,23),('m351x',24),(_v,25),('m338x',26),('m3328',27),(_O,28),(_N,29),(_P,30),(_b,31),('m3800',32),('m3368',36),(_Y,38),('m2810nmm',39),('m2810hm',40),('m3301ohms75',41),('m3301ohms93',42),('m2912',43),('m2914',44),(_d,45),(_e,46),(_j,47),('m2702Fhm',48),('m2712Fhm',49),('m2712hm',50),('m2702hm',51),('m2813nmm',52),('m2813hm',53),('m2814hm',54),('m2803hm',55),(_L,56),('m2814nmm',57),('m2804hm',58),('m2702Chm',59),('m2715Fhm',60),('m2705Fhm',61),('m2705Chm',62),(_f,63),(_g,64),('m271xnmm',65),('m2715hm',66),('m3910SSD',67),(_h,68),(_i,69),(_l,70),(_k,71),('m2705hm',72),('m3905',73),('m2915',74),('m2715Bhm',75),('m2705Bhm',76),('m2715BFhm',77),('m2712Bhm',78),('m2712BFhm',79),('m2702BChm',80),('m3486',82),('m810m',88),(_n,101),(_m,102),('m2813SAnmm',103),('m2814SAnmm',104),(_o,105),(_p,106),('m3174',107),(_q,108),(_r,109),('m271xSAnmm',110),(_Q,114),(_R,115),(_s,116),(_t,117),(_u,119),('m3410',120),('m3405',121),('m3475',122),('mAlcatelEthConcnmm',250),('mAlcatelEthConchm',251),('mAlcatelEthExpConchm',252)))
_S3CommonBoardId_Type.__name__=_C
_S3CommonBoardId_Object=MibTableColumn
s3CommonBoardId=_S3CommonBoardId_Object((1,3,6,1,4,1,45,1,3,1,8,1,2),_S3CommonBoardId_Type())
s3CommonBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardId.setStatus(_A)
_S3CommonBoardHwVer_Type=Integer32
_S3CommonBoardHwVer_Object=MibTableColumn
s3CommonBoardHwVer=_S3CommonBoardHwVer_Object((1,3,6,1,4,1,45,1,3,1,8,1,3),_S3CommonBoardHwVer_Type())
s3CommonBoardHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardHwVer.setStatus(_A)
class _S3CommonBoardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_K,2)))
_S3CommonBoardStatus_Type.__name__=_C
_S3CommonBoardStatus_Object=MibTableColumn
s3CommonBoardStatus=_S3CommonBoardStatus_Object((1,3,6,1,4,1,45,1,3,1,8,1,4),_S3CommonBoardStatus_Type())
s3CommonBoardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardStatus.setStatus(_A)
class _S3CommonBoardReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_S3CommonBoardReset_Type.__name__=_C
_S3CommonBoardReset_Object=MibTableColumn
s3CommonBoardReset=_S3CommonBoardReset_Object((1,3,6,1,4,1,45,1,3,1,8,1,5),_S3CommonBoardReset_Type())
s3CommonBoardReset.setMaxAccess(_D)
if mibBuilder.loadTexts:s3CommonBoardReset.setStatus(_A)
class _S3CommonBoardPartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('partition',2),('timedPartition',3)))
_S3CommonBoardPartStatus_Type.__name__=_C
_S3CommonBoardPartStatus_Object=MibTableColumn
s3CommonBoardPartStatus=_S3CommonBoardPartStatus_Object((1,3,6,1,4,1,45,1,3,1,8,1,6),_S3CommonBoardPartStatus_Type())
s3CommonBoardPartStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:s3CommonBoardPartStatus.setStatus(_A)
class _S3CommonBoardNmCntlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notNmControl',1),('nmControl',2)))
_S3CommonBoardNmCntlStatus_Type.__name__=_C
_S3CommonBoardNmCntlStatus_Object=MibTableColumn
s3CommonBoardNmCntlStatus=_S3CommonBoardNmCntlStatus_Object((1,3,6,1,4,1,45,1,3,1,8,1,7),_S3CommonBoardNmCntlStatus_Type())
s3CommonBoardNmCntlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardNmCntlStatus.setStatus(_A)
class _S3CommonBoardPsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_K,2)))
_S3CommonBoardPsStatus_Type.__name__=_C
_S3CommonBoardPsStatus_Object=MibTableColumn
s3CommonBoardPsStatus=_S3CommonBoardPsStatus_Object((1,3,6,1,4,1,45,1,3,1,8,1,8),_S3CommonBoardPsStatus_Type())
s3CommonBoardPsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3CommonBoardPsStatus.setStatus(_A)
_S3CommonBoardPartTime_Type=TimeTicks
_S3CommonBoardPartTime_Object=MibTableColumn
s3CommonBoardPartTime=_S3CommonBoardPartTime_Object((1,3,6,1,4,1,45,1,3,1,8,1,9),_S3CommonBoardPartTime_Type())
s3CommonBoardPartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:s3CommonBoardPartTime.setStatus(_A)
class _S3SlotConfigOctetString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,144))
_S3SlotConfigOctetString_Type.__name__=_G
_S3SlotConfigOctetString_Object=MibScalar
s3SlotConfigOctetString=_S3SlotConfigOctetString_Object((1,3,6,1,4,1,45,1,3,1,9),_S3SlotConfigOctetString_Type())
s3SlotConfigOctetString.setMaxAccess(_B)
if mibBuilder.loadTexts:s3SlotConfigOctetString.setStatus(_A)
_S3000RedundantPs_ObjectIdentity=ObjectIdentity
s3000RedundantPs=_S3000RedundantPs_ObjectIdentity((1,3,6,1,4,1,45,1,3,1,10))
_S3RedPsPlus5vCurrent_Type=Gauge32
_S3RedPsPlus5vCurrent_Object=MibScalar
s3RedPsPlus5vCurrent=_S3RedPsPlus5vCurrent_Object((1,3,6,1,4,1,45,1,3,1,10,1),_S3RedPsPlus5vCurrent_Type())
s3RedPsPlus5vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsPlus5vCurrent.setStatus(_A)
_S3RedPsPlus12vCurrent_Type=Gauge32
_S3RedPsPlus12vCurrent_Object=MibScalar
s3RedPsPlus12vCurrent=_S3RedPsPlus12vCurrent_Object((1,3,6,1,4,1,45,1,3,1,10,2),_S3RedPsPlus12vCurrent_Type())
s3RedPsPlus12vCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsPlus12vCurrent.setStatus(_A)
class _S3RedPsAmbientTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('normalTemperature',2),('aboveNormalTemp',3)))
_S3RedPsAmbientTempStatus_Type.__name__=_C
_S3RedPsAmbientTempStatus_Object=MibScalar
s3RedPsAmbientTempStatus=_S3RedPsAmbientTempStatus_Object((1,3,6,1,4,1,45,1,3,1,10,3),_S3RedPsAmbientTempStatus_Type())
s3RedPsAmbientTempStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsAmbientTempStatus.setStatus(_A)
_S3RedPsAmbientTemperature_Type=Gauge32
_S3RedPsAmbientTemperature_Object=MibScalar
s3RedPsAmbientTemperature=_S3RedPsAmbientTemperature_Object((1,3,6,1,4,1,45,1,3,1,10,4),_S3RedPsAmbientTemperature_Type())
s3RedPsAmbientTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsAmbientTemperature.setStatus(_A)
_S3RedPsPrimaryConfig_Type=S3PsType
_S3RedPsPrimaryConfig_Object=MibScalar
s3RedPsPrimaryConfig=_S3RedPsPrimaryConfig_Object((1,3,6,1,4,1,45,1,3,1,10,5),_S3RedPsPrimaryConfig_Type())
s3RedPsPrimaryConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsPrimaryConfig.setStatus(_A)
_S3RedPsSecondaryConfig_Type=S3PsType
_S3RedPsSecondaryConfig_Object=MibScalar
s3RedPsSecondaryConfig=_S3RedPsSecondaryConfig_Object((1,3,6,1,4,1,45,1,3,1,10,6),_S3RedPsSecondaryConfig_Type())
s3RedPsSecondaryConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsSecondaryConfig.setStatus(_A)
class _S3RedPsDiodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('bothOk',2),(_S,3),(_T,4),(_U,5)))
_S3RedPsDiodeStatus_Type.__name__=_C
_S3RedPsDiodeStatus_Object=MibScalar
s3RedPsDiodeStatus=_S3RedPsDiodeStatus_Object((1,3,6,1,4,1,45,1,3,1,10,7),_S3RedPsDiodeStatus_Type())
s3RedPsDiodeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsDiodeStatus.setStatus(_A)
class _S3RedPsPowerAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('bothOk',2),(_S,3),(_T,4),(_U,5)))
_S3RedPsPowerAlarm_Type.__name__=_C
_S3RedPsPowerAlarm_Object=MibScalar
s3RedPsPowerAlarm=_S3RedPsPowerAlarm_Object((1,3,6,1,4,1,45,1,3,1,10,8),_S3RedPsPowerAlarm_Type())
s3RedPsPowerAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:s3RedPsPowerAlarm.setStatus(_A)
_S3ChassisBkPlEthChanDiv_Type=Integer32
_S3ChassisBkPlEthChanDiv_Object=MibScalar
s3ChassisBkPlEthChanDiv=_S3ChassisBkPlEthChanDiv_Object((1,3,6,1,4,1,45,1,3,1,11),_S3ChassisBkPlEthChanDiv_Type())
s3ChassisBkPlEthChanDiv.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisBkPlEthChanDiv.setStatus(_A)
class _S3ChassisEnetChannelAType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('aSegmentable',2),('aNotSegmentable',3)))
_S3ChassisEnetChannelAType_Type.__name__=_C
_S3ChassisEnetChannelAType_Object=MibScalar
s3ChassisEnetChannelAType=_S3ChassisEnetChannelAType_Object((1,3,6,1,4,1,45,1,3,1,12),_S3ChassisEnetChannelAType_Type())
s3ChassisEnetChannelAType.setMaxAccess(_B)
if mibBuilder.loadTexts:s3ChassisEnetChannelAType.setStatus(_A)
_S3000Ethernet_ObjectIdentity=ObjectIdentity
s3000Ethernet=_S3000Ethernet_ObjectIdentity((1,3,6,1,4,1,45,1,3,2))
_S3000TokenRing_ObjectIdentity=ObjectIdentity
s3000TokenRing=_S3000TokenRing_ObjectIdentity((1,3,6,1,4,1,45,1,3,3))
_S3000FDDI_ObjectIdentity=ObjectIdentity
s3000FDDI=_S3000FDDI_ObjectIdentity((1,3,6,1,4,1,45,1,3,4))
_S3000Bridge_ObjectIdentity=ObjectIdentity
s3000Bridge=_S3000Bridge_ObjectIdentity((1,3,6,1,4,1,45,1,3,5))
_S3000TerminalServer_ObjectIdentity=ObjectIdentity
s3000TerminalServer=_S3000TerminalServer_ObjectIdentity((1,3,6,1,4,1,45,1,3,6))
_S3000LattisTalk_ObjectIdentity=ObjectIdentity
s3000LattisTalk=_S3000LattisTalk_ObjectIdentity((1,3,6,1,4,1,45,1,3,7))
_S3000Trb_ObjectIdentity=ObjectIdentity
s3000Trb=_S3000Trb_ObjectIdentity((1,3,6,1,4,1,45,1,3,8))
mibBuilder.exportSymbols(_J,**{'S3ModuleType':S3ModuleType,'S3PsType':S3PsType,'s3AgentSw':s3AgentSw,'s3AgentType':s3AgentType,'s3AgentFwVer':s3AgentFwVer,'s3AgentSwMajorVer':s3AgentSwMajorVer,'s3AgentSwMinorVer':s3AgentSwMinorVer,'s3AgentBootProtocol':s3AgentBootProtocol,'s3AgentBootFile':s3AgentBootFile,'s3AgentAuthTrap':s3AgentAuthTrap,'s3AgentLocation':s3AgentLocation,'s3AgentMibLevel':s3AgentMibLevel,'s3AgentFeatureLevel':s3AgentFeatureLevel,'s3AgentMySlotId':s3AgentMySlotId,'s3AgentUnAuthIp':s3AgentUnAuthIp,'s3AgentUnAuthComm':s3AgentUnAuthComm,'s3AgentSwLicenseCode':s3AgentSwLicenseCode,'s3AgentPerformance':s3AgentPerformance,'s3AgentSwMaintVer':s3AgentSwMaintVer,'s3AgentConfigLoadMode':s3AgentConfigLoadMode,'s3AgentConfigActualSource':s3AgentConfigActualSource,'s3AgentMgmtProtoMode':s3AgentMgmtProtoMode,'s3AgentActualMgmtProtocol':s3AgentActualMgmtProtocol,'s3AgentImageFile':s3AgentImageFile,'s3AgentNetProtocol':s3AgentNetProtocol,'s3AgentIpProtocol':s3AgentIpProtocol,'s3AgentIpAddr':s3AgentIpAddr,'s3AgentNetMask':s3AgentNetMask,'s3AgentDefaultGateway':s3AgentDefaultGateway,'s3AgentBootServerAddr':s3AgentBootServerAddr,'s3AgentSecDefaultGateway':s3AgentSecDefaultGateway,'s3AgentPingDefaultRtrSwitch':s3AgentPingDefaultRtrSwitch,'s3AgentPingDefaultRtrTime':s3AgentPingDefaultRtrTime,'s3AgentBootRouter':s3AgentBootRouter,'s3AgentTrapReceiverTable':s3AgentTrapReceiverTable,'s3AgentTrapReceiverEntry':s3AgentTrapReceiverEntry,'s3AgentTrapRcvrStatus':s3AgentTrapRcvrStatus,_A0:s3AgentTrapRcvrNetAddress,'s3AgentTrapRcvrComm':s3AgentTrapRcvrComm,'s3AgentTrapRcvrAgeTime':s3AgentTrapRcvrAgeTime,'s3AgentHw':s3AgentHw,'s3AgentStatus':s3AgentStatus,'s3AgentMdaHwVer':s3AgentMdaHwVer,'s3AgentMode':s3AgentMode,'s3AgentReset':s3AgentReset,'s3AgentRestart':s3AgentRestart,'s3AgentBootMode':s3AgentBootMode,'s3AgentWriteEeprom':s3AgentWriteEeprom,'s3AgentBaudRate':s3AgentBaudRate,'s3AgentInitString':s3AgentInitString,'s3AgentEepromSize':s3AgentEepromSize,'s3AgentEpromSize':s3AgentEpromSize,'s3AgentDramSize':s3AgentDramSize,'s3AgentHexDisplay':s3AgentHexDisplay,'s3AgentFlashStatus':s3AgentFlashStatus,'s3AgentSpecific':s3AgentSpecific,'s3AgentLocImage':s3AgentLocImage,'s3LocImageValid':s3LocImageValid,'s3LocImageMajorVersion':s3LocImageMajorVersion,'s3LocImageMinorVersion':s3LocImageMinorVersion,'s3LocImageLoadMode':s3LocImageLoadMode,'s3LocImageActualSource':s3LocImageActualSource,'s3LocImageMaintVersion':s3LocImageMaintVersion,'s3000Chassis':s3000Chassis,'s3ChassisType':s3ChassisType,'s3ChassisBkplType':s3ChassisBkplType,'s3ChassisBkplRev':s3ChassisBkplRev,'s3ChassisPsType':s3ChassisPsType,'s3ChassisPsStatus':s3ChassisPsStatus,'s3ChassisFanStatus':s3ChassisFanStatus,'s3SlotConfigTable':s3SlotConfigTable,'s3SlotConfigEntry':s3SlotConfigEntry,_A1:s3SlotNumber,'s3SlotModuleId':s3SlotModuleId,'s3SlotModuleType':s3SlotModuleType,'s3SlotModuleDescr':s3SlotModuleDescr,'s3SlotModuleLed':s3SlotModuleLed,'s3SlotModuleMdaId':s3SlotModuleMdaId,'s3CommonBoardTable':s3CommonBoardTable,'s3CommonBoardEntry':s3CommonBoardEntry,_A2:s3CommonBoardIndex,'s3CommonBoardId':s3CommonBoardId,'s3CommonBoardHwVer':s3CommonBoardHwVer,'s3CommonBoardStatus':s3CommonBoardStatus,'s3CommonBoardReset':s3CommonBoardReset,'s3CommonBoardPartStatus':s3CommonBoardPartStatus,'s3CommonBoardNmCntlStatus':s3CommonBoardNmCntlStatus,'s3CommonBoardPsStatus':s3CommonBoardPsStatus,'s3CommonBoardPartTime':s3CommonBoardPartTime,'s3SlotConfigOctetString':s3SlotConfigOctetString,'s3000RedundantPs':s3000RedundantPs,'s3RedPsPlus5vCurrent':s3RedPsPlus5vCurrent,'s3RedPsPlus12vCurrent':s3RedPsPlus12vCurrent,'s3RedPsAmbientTempStatus':s3RedPsAmbientTempStatus,'s3RedPsAmbientTemperature':s3RedPsAmbientTemperature,'s3RedPsPrimaryConfig':s3RedPsPrimaryConfig,'s3RedPsSecondaryConfig':s3RedPsSecondaryConfig,'s3RedPsDiodeStatus':s3RedPsDiodeStatus,'s3RedPsPowerAlarm':s3RedPsPowerAlarm,'s3ChassisBkPlEthChanDiv':s3ChassisBkPlEthChanDiv,'s3ChassisEnetChannelAType':s3ChassisEnetChannelAType,'s3000Ethernet':s3000Ethernet,'s3000TokenRing':s3000TokenRing,'s3000FDDI':s3000FDDI,'s3000Bridge':s3000Bridge,'s3000TerminalServer':s3000TerminalServer,'s3000LattisTalk':s3000LattisTalk,'s3000Trb':s3000Trb})