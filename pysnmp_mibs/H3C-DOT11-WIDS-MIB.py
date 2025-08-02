_z='h3cDot11WIDSRptAPLstDctTime'
_y='h3cDot11WIDSRptAPRadioID'
_x='h3cDot11WIDSRptAPName'
_w='h3cDot11WIDSAtkHisAPName'
_v='h3cDot11WIDSAtkHisDctTime'
_u='h3cDot11WIDSAtkHisChl'
_t='h3cDot11WIDSAtkHisType'
_s='h3cDot11UnauthorSSIDName'
_r='h3cDot11WIDSAdHocMAC'
_q='h3cDot11WIDSRogueType'
_p='h3cDot11BlackListMAC'
_o='h3cDot11WIDSAtkStasType'
_n='h3cDot11WIDSAtkHisIndex'
_m='h3cDot11WIDSRogueHisIndex'
_l='h3cDot11DynBlackListMAC'
_k='h3cDot11WIDSRptAPMAC'
_j='h3cDot11PermitBSSID'
_i='h3cDot11StaticBlackListMAC'
_h='h3cDot11StaticWhiteListMAC'
_g='h3cDot11AttackDeviceMac'
_f='h3cDot11IgnoreMAC'
_e='h3cDot11PermitSSID'
_d='h3cDot11VendorOUI'
_c='unknown'
_b='H3cDot11SSIDStringType'
_a='h3cDot11WIDSAtkDestMac'
_Z='h3cDot11WIDSAtkTime'
_Y='h3cDot11WIDSAtkChannel'
_X='h3cDot11WIDSAtkFrameType'
_W='h3cDot11MonitorApRadioID'
_V='h3cDot11MonitorAPID'
_U='h3cDot11WIDSRogueMAC'
_T='h3cDot11WIDSDevMAC'
_S='h3cDot11RogueStaMAC'
_R='h3cDot11WIDSAPID'
_Q='h3cDot11RogueAPBSSMAC'
_P='TruthValue'
_O='Unsigned32'
_N='h3cDot11WIDSFirstTrapTime'
_M='h3cDot11WIDSAtkMac'
_L='h3cDot11WIDSMonitorMAC'
_K='dBm'
_J='second'
_I='OctetString'
_H='Integer32'
_G='read-create'
_F='accessible-for-notify'
_E='not-accessible'
_D='read-write'
_C='H3C-DOT11-WIDS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11ChannelScopeType,H3cDot11ObjectIDType,H3cDot11RadioScopeType,H3cDot11RadioType,H3cDot11SSIDStringType,h3cDot11=mibBuilder.importSymbols('H3C-DOT11-REF-MIB','H3cDot11ChannelScopeType','H3cDot11ObjectIDType','H3cDot11RadioScopeType','H3cDot11RadioType',_b,'h3cDot11')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_P)
h3cDot11WIDS=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,5))
if mibBuilder.loadTexts:h3cDot11WIDS.setRevisions(('2010-05-31 18:00','2009-07-29 18:00','2009-05-07 20:00','2008-07-25 19:00','2007-06-19 19:00','2007-05-16 19:00','2006-08-20 19:00'))
class H3cDot11WIDSDevType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('client',1),('ap',2),('adhoc',3),('wirelessBridge',4),(_c,5)))
class H3cDot11WIDSDevPermitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('rogue',2)))
class H3cDot11WIDSAtkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('act',1),('asr',2),('aur',3),('daf',4),('dar',5),('ndf',6),('pbr',7),('rar',8),('saf',9),('sdf',10),('wiv',11),(_c,12)))
_H3cDot11WIDSConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11WIDSConfigGroup=_H3cDot11WIDSConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,1))
_H3cDot11WIDSGlobalConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11WIDSGlobalConfigGroup=_H3cDot11WIDSGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,1,1))
class _H3cDot11WIDSScanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('auto',2)))
_H3cDot11WIDSScanMode_Type.__name__=_H
_H3cDot11WIDSScanMode_Object=MibScalar
h3cDot11WIDSScanMode=_H3cDot11WIDSScanMode_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,1),_H3cDot11WIDSScanMode_Type())
h3cDot11WIDSScanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WIDSScanMode.setStatus(_A)
class _H3cDot11WIDSScanChannelList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_H3cDot11WIDSScanChannelList_Type.__name__=_I
_H3cDot11WIDSScanChannelList_Object=MibScalar
h3cDot11WIDSScanChannelList=_H3cDot11WIDSScanChannelList_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,2),_H3cDot11WIDSScanChannelList_Type())
h3cDot11WIDSScanChannelList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WIDSScanChannelList.setStatus('obsolete')
class _H3cDot11CntMsrMode_Type(Bits):namedValues=NamedValues(*(('rogue',0),('adhoc',1),('config',2)))
_H3cDot11CntMsrMode_Type.__name__='Bits'
_H3cDot11CntMsrMode_Object=MibScalar
h3cDot11CntMsrMode=_H3cDot11CntMsrMode_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,3),_H3cDot11CntMsrMode_Type())
h3cDot11CntMsrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CntMsrMode.setStatus(_A)
class _H3cDot11DevAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1800))
_H3cDot11DevAgingTime_Type.__name__=_H
_H3cDot11DevAgingTime_Object=MibScalar
h3cDot11DevAgingTime=_H3cDot11DevAgingTime_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,4),_H3cDot11DevAgingTime_Type())
h3cDot11DevAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11DevAgingTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DevAgingTime.setUnits(_J)
_H3cDot11DynBlkListEnable_Type=TruthValue
_H3cDot11DynBlkListEnable_Object=MibScalar
h3cDot11DynBlkListEnable=_H3cDot11DynBlkListEnable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,5),_H3cDot11DynBlkListEnable_Type())
h3cDot11DynBlkListEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11DynBlkListEnable.setStatus(_A)
class _H3cDot11DynBlkListLifeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_H3cDot11DynBlkListLifeTime_Type.__name__=_H
_H3cDot11DynBlkListLifeTime_Object=MibScalar
h3cDot11DynBlkListLifeTime=_H3cDot11DynBlkListLifeTime_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,6),_H3cDot11DynBlkListLifeTime_Type())
h3cDot11DynBlkListLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11DynBlkListLifeTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DynBlkListLifeTime.setUnits(_J)
_H3cDot11FloodAtkDctEnable_Type=TruthValue
_H3cDot11FloodAtkDctEnable_Object=MibScalar
h3cDot11FloodAtkDctEnable=_H3cDot11FloodAtkDctEnable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,7),_H3cDot11FloodAtkDctEnable_Type())
h3cDot11FloodAtkDctEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11FloodAtkDctEnable.setStatus(_A)
_H3cDot11SpoofAtkDctEnable_Type=TruthValue
_H3cDot11SpoofAtkDctEnable_Object=MibScalar
h3cDot11SpoofAtkDctEnable=_H3cDot11SpoofAtkDctEnable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,8),_H3cDot11SpoofAtkDctEnable_Type())
h3cDot11SpoofAtkDctEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SpoofAtkDctEnable.setStatus(_A)
_H3cDot11WeakIVAtkDctEnable_Type=TruthValue
_H3cDot11WeakIVAtkDctEnable_Object=MibScalar
h3cDot11WeakIVAtkDctEnable=_H3cDot11WeakIVAtkDctEnable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,9),_H3cDot11WeakIVAtkDctEnable_Type())
h3cDot11WeakIVAtkDctEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WeakIVAtkDctEnable.setStatus(_A)
_H3cDot11ResetWIDSRogueHistory_Type=TruthValue
_H3cDot11ResetWIDSRogueHistory_Object=MibScalar
h3cDot11ResetWIDSRogueHistory=_H3cDot11ResetWIDSRogueHistory_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,10),_H3cDot11ResetWIDSRogueHistory_Type())
h3cDot11ResetWIDSRogueHistory.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetWIDSRogueHistory.setStatus(_A)
_H3cDot11ResetWIDSHistroy_Type=TruthValue
_H3cDot11ResetWIDSHistroy_Object=MibScalar
h3cDot11ResetWIDSHistroy=_H3cDot11ResetWIDSHistroy_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,11),_H3cDot11ResetWIDSHistroy_Type())
h3cDot11ResetWIDSHistroy.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetWIDSHistroy.setStatus(_A)
_H3cDot11ResetWIDSStatistics_Type=TruthValue
_H3cDot11ResetWIDSStatistics_Object=MibScalar
h3cDot11ResetWIDSStatistics=_H3cDot11ResetWIDSStatistics_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,12),_H3cDot11ResetWIDSStatistics_Type())
h3cDot11ResetWIDSStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetWIDSStatistics.setStatus(_A)
_H3cDot11ResetAllDynBlkList_Type=TruthValue
_H3cDot11ResetAllDynBlkList_Object=MibScalar
h3cDot11ResetAllDynBlkList=_H3cDot11ResetAllDynBlkList_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,13),_H3cDot11ResetAllDynBlkList_Type())
h3cDot11ResetAllDynBlkList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDynBlkList.setStatus(_A)
_H3cDot11ResetAllStcBlkList_Type=TruthValue
_H3cDot11ResetAllStcBlkList_Object=MibScalar
h3cDot11ResetAllStcBlkList=_H3cDot11ResetAllStcBlkList_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,14),_H3cDot11ResetAllStcBlkList_Type())
h3cDot11ResetAllStcBlkList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllStcBlkList.setStatus(_A)
_H3cDot11ResetAllWhtBlkList_Type=TruthValue
_H3cDot11ResetAllWhtBlkList_Object=MibScalar
h3cDot11ResetAllWhtBlkList=_H3cDot11ResetAllWhtBlkList_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,15),_H3cDot11ResetAllWhtBlkList_Type())
h3cDot11ResetAllWhtBlkList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllWhtBlkList.setStatus(_A)
_H3cDot11ResetAllDctRogueAP_Type=TruthValue
_H3cDot11ResetAllDctRogueAP_Object=MibScalar
h3cDot11ResetAllDctRogueAP=_H3cDot11ResetAllDctRogueAP_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,16),_H3cDot11ResetAllDctRogueAP_Type())
h3cDot11ResetAllDctRogueAP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDctRogueAP.setStatus(_A)
_H3cDot11ResetAllDctRogueSta_Type=TruthValue
_H3cDot11ResetAllDctRogueSta_Object=MibScalar
h3cDot11ResetAllDctRogueSta=_H3cDot11ResetAllDctRogueSta_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,17),_H3cDot11ResetAllDctRogueSta_Type())
h3cDot11ResetAllDctRogueSta.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDctRogueSta.setStatus(_A)
_H3cDot11ResetAllDctAdhoc_Type=TruthValue
_H3cDot11ResetAllDctAdhoc_Object=MibScalar
h3cDot11ResetAllDctAdhoc=_H3cDot11ResetAllDctAdhoc_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,18),_H3cDot11ResetAllDctAdhoc_Type())
h3cDot11ResetAllDctAdhoc.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDctAdhoc.setStatus(_A)
_H3cDot11ResetAllDctDevice_Type=TruthValue
_H3cDot11ResetAllDctDevice_Object=MibScalar
h3cDot11ResetAllDctDevice=_H3cDot11ResetAllDctDevice_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,19),_H3cDot11ResetAllDctDevice_Type())
h3cDot11ResetAllDctDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDctDevice.setStatus(_A)
_H3cDot11ResetAllDctSSID_Type=TruthValue
_H3cDot11ResetAllDctSSID_Object=MibScalar
h3cDot11ResetAllDctSSID=_H3cDot11ResetAllDctSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,20),_H3cDot11ResetAllDctSSID_Type())
h3cDot11ResetAllDctSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ResetAllDctSSID.setStatus(_A)
class _H3cDot11WidsFloodInterval_Type(Unsigned32):defaultValue=1
_H3cDot11WidsFloodInterval_Type.__name__=_O
_H3cDot11WidsFloodInterval_Object=MibScalar
h3cDot11WidsFloodInterval=_H3cDot11WidsFloodInterval_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,21),_H3cDot11WidsFloodInterval_Type())
h3cDot11WidsFloodInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WidsFloodInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11WidsFloodInterval.setUnits(_J)
class _H3cDot11WidsBlackListThreshold_Type(Unsigned32):defaultValue=100
_H3cDot11WidsBlackListThreshold_Type.__name__=_O
_H3cDot11WidsBlackListThreshold_Object=MibScalar
h3cDot11WidsBlackListThreshold=_H3cDot11WidsBlackListThreshold_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,22),_H3cDot11WidsBlackListThreshold_Type())
h3cDot11WidsBlackListThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WidsBlackListThreshold.setStatus(_A)
class _H3cDot11SSIDFilterOnOff_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cDot11SSIDFilterOnOff_Type.__name__=_H
_H3cDot11SSIDFilterOnOff_Object=MibScalar
h3cDot11SSIDFilterOnOff=_H3cDot11SSIDFilterOnOff_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,23),_H3cDot11SSIDFilterOnOff_Type())
h3cDot11SSIDFilterOnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SSIDFilterOnOff.setStatus(_A)
class _H3cDot11BSSIDFilterOnOff_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cDot11BSSIDFilterOnOff_Type.__name__=_H
_H3cDot11BSSIDFilterOnOff_Object=MibScalar
h3cDot11BSSIDFilterOnOff=_H3cDot11BSSIDFilterOnOff_Object((1,3,6,1,4,1,2011,10,2,75,5,1,1,24),_H3cDot11BSSIDFilterOnOff_Type())
h3cDot11BSSIDFilterOnOff.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11BSSIDFilterOnOff.setStatus(_A)
_H3cDot11WIDSPermitVendorTable_Object=MibTable
h3cDot11WIDSPermitVendorTable=_H3cDot11WIDSPermitVendorTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,2))
if mibBuilder.loadTexts:h3cDot11WIDSPermitVendorTable.setStatus(_A)
_H3cDot11WIDSPermitVendorEntry_Object=MibTableRow
h3cDot11WIDSPermitVendorEntry=_H3cDot11WIDSPermitVendorEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,2,1))
h3cDot11WIDSPermitVendorEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:h3cDot11WIDSPermitVendorEntry.setStatus(_A)
class _H3cDot11VendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cDot11VendorOUI_Type.__name__=_I
_H3cDot11VendorOUI_Object=MibTableColumn
h3cDot11VendorOUI=_H3cDot11VendorOUI_Object((1,3,6,1,4,1,2011,10,2,75,5,1,2,1,1),_H3cDot11VendorOUI_Type())
h3cDot11VendorOUI.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11VendorOUI.setStatus(_A)
_H3cDot11PermitVendorRowStatus_Type=RowStatus
_H3cDot11PermitVendorRowStatus_Object=MibTableColumn
h3cDot11PermitVendorRowStatus=_H3cDot11PermitVendorRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,2,1,2),_H3cDot11PermitVendorRowStatus_Type())
h3cDot11PermitVendorRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11PermitVendorRowStatus.setStatus(_A)
class _H3cDot11VendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11VendorName_Type.__name__=_I
_H3cDot11VendorName_Object=MibTableColumn
h3cDot11VendorName=_H3cDot11VendorName_Object((1,3,6,1,4,1,2011,10,2,75,5,1,2,1,3),_H3cDot11VendorName_Type())
h3cDot11VendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11VendorName.setStatus(_A)
_H3cDot11WIDSPermitSSIDTable_Object=MibTable
h3cDot11WIDSPermitSSIDTable=_H3cDot11WIDSPermitSSIDTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,3))
if mibBuilder.loadTexts:h3cDot11WIDSPermitSSIDTable.setStatus(_A)
_H3cDot11WIDSPermitSSIDEntry_Object=MibTableRow
h3cDot11WIDSPermitSSIDEntry=_H3cDot11WIDSPermitSSIDEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,3,1))
h3cDot11WIDSPermitSSIDEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:h3cDot11WIDSPermitSSIDEntry.setStatus(_A)
class _H3cDot11PermitSSID_Type(H3cDot11SSIDStringType):subtypeSpec=H3cDot11SSIDStringType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11PermitSSID_Type.__name__=_b
_H3cDot11PermitSSID_Object=MibTableColumn
h3cDot11PermitSSID=_H3cDot11PermitSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,1,3,1,1),_H3cDot11PermitSSID_Type())
h3cDot11PermitSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11PermitSSID.setStatus(_A)
_H3cDot11PermitSSIDRowStatus_Type=RowStatus
_H3cDot11PermitSSIDRowStatus_Object=MibTableColumn
h3cDot11PermitSSIDRowStatus=_H3cDot11PermitSSIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,3,1,2),_H3cDot11PermitSSIDRowStatus_Type())
h3cDot11PermitSSIDRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11PermitSSIDRowStatus.setStatus(_A)
_H3cDot11PermitSSIDDetected_Type=TruthValue
_H3cDot11PermitSSIDDetected_Object=MibTableColumn
h3cDot11PermitSSIDDetected=_H3cDot11PermitSSIDDetected_Object((1,3,6,1,4,1,2011,10,2,75,5,1,3,1,3),_H3cDot11PermitSSIDDetected_Type())
h3cDot11PermitSSIDDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PermitSSIDDetected.setStatus(_A)
_H3cDot11WIDSIgnoreListTable_Object=MibTable
h3cDot11WIDSIgnoreListTable=_H3cDot11WIDSIgnoreListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4))
if mibBuilder.loadTexts:h3cDot11WIDSIgnoreListTable.setStatus(_A)
_H3cDot11WIDSIgnoreListEntry_Object=MibTableRow
h3cDot11WIDSIgnoreListEntry=_H3cDot11WIDSIgnoreListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4,1))
h3cDot11WIDSIgnoreListEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:h3cDot11WIDSIgnoreListEntry.setStatus(_A)
_H3cDot11IgnoreMAC_Type=MacAddress
_H3cDot11IgnoreMAC_Object=MibTableColumn
h3cDot11IgnoreMAC=_H3cDot11IgnoreMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4,1,1),_H3cDot11IgnoreMAC_Type())
h3cDot11IgnoreMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11IgnoreMAC.setStatus(_A)
_H3cDot11IgnoreListRowStatus_Type=RowStatus
_H3cDot11IgnoreListRowStatus_Object=MibTableColumn
h3cDot11IgnoreListRowStatus=_H3cDot11IgnoreListRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4,1,2),_H3cDot11IgnoreListRowStatus_Type())
h3cDot11IgnoreListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11IgnoreListRowStatus.setStatus(_A)
_H3cDot11IgnoreMACDetected_Type=TruthValue
_H3cDot11IgnoreMACDetected_Object=MibTableColumn
h3cDot11IgnoreMACDetected=_H3cDot11IgnoreMACDetected_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4,1,3),_H3cDot11IgnoreMACDetected_Type())
h3cDot11IgnoreMACDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11IgnoreMACDetected.setStatus(_A)
_H3cDot11IgnoreDevType_Type=H3cDot11WIDSDevType
_H3cDot11IgnoreDevType_Object=MibTableColumn
h3cDot11IgnoreDevType=_H3cDot11IgnoreDevType_Object((1,3,6,1,4,1,2011,10,2,75,5,1,4,1,4),_H3cDot11IgnoreDevType_Type())
h3cDot11IgnoreDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11IgnoreDevType.setStatus(_A)
_H3cDot11WIDSAttackListTable_Object=MibTable
h3cDot11WIDSAttackListTable=_H3cDot11WIDSAttackListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5))
if mibBuilder.loadTexts:h3cDot11WIDSAttackListTable.setStatus(_A)
_H3cDot11WIDSAttackListEntry_Object=MibTableRow
h3cDot11WIDSAttackListEntry=_H3cDot11WIDSAttackListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5,1))
h3cDot11WIDSAttackListEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:h3cDot11WIDSAttackListEntry.setStatus(_A)
_H3cDot11AttackDeviceMac_Type=MacAddress
_H3cDot11AttackDeviceMac_Object=MibTableColumn
h3cDot11AttackDeviceMac=_H3cDot11AttackDeviceMac_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5,1,1),_H3cDot11AttackDeviceMac_Type())
h3cDot11AttackDeviceMac.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11AttackDeviceMac.setStatus(_A)
_H3cDot11AttackListRowStatus_Type=RowStatus
_H3cDot11AttackListRowStatus_Object=MibTableColumn
h3cDot11AttackListRowStatus=_H3cDot11AttackListRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5,1,2),_H3cDot11AttackListRowStatus_Type())
h3cDot11AttackListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11AttackListRowStatus.setStatus(_A)
_H3cDot11AttackDevDetected_Type=TruthValue
_H3cDot11AttackDevDetected_Object=MibTableColumn
h3cDot11AttackDevDetected=_H3cDot11AttackDevDetected_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5,1,3),_H3cDot11AttackDevDetected_Type())
h3cDot11AttackDevDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AttackDevDetected.setStatus(_A)
_H3cDot11AttackDevType_Type=H3cDot11WIDSDevType
_H3cDot11AttackDevType_Object=MibTableColumn
h3cDot11AttackDevType=_H3cDot11AttackDevType_Object((1,3,6,1,4,1,2011,10,2,75,5,1,5,1,4),_H3cDot11AttackDevType_Type())
h3cDot11AttackDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AttackDevType.setStatus(_A)
_H3cDot11StaticWhiteListTable_Object=MibTable
h3cDot11StaticWhiteListTable=_H3cDot11StaticWhiteListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,6))
if mibBuilder.loadTexts:h3cDot11StaticWhiteListTable.setStatus(_A)
_H3cDot11StaticWhiteListEntry_Object=MibTableRow
h3cDot11StaticWhiteListEntry=_H3cDot11StaticWhiteListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,6,1))
h3cDot11StaticWhiteListEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:h3cDot11StaticWhiteListEntry.setStatus(_A)
_H3cDot11StaticWhiteListMAC_Type=MacAddress
_H3cDot11StaticWhiteListMAC_Object=MibTableColumn
h3cDot11StaticWhiteListMAC=_H3cDot11StaticWhiteListMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,1,6,1,1),_H3cDot11StaticWhiteListMAC_Type())
h3cDot11StaticWhiteListMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11StaticWhiteListMAC.setStatus(_A)
_H3cDot11StaticWhiteListRowStatus_Type=RowStatus
_H3cDot11StaticWhiteListRowStatus_Object=MibTableColumn
h3cDot11StaticWhiteListRowStatus=_H3cDot11StaticWhiteListRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,6,1,2),_H3cDot11StaticWhiteListRowStatus_Type())
h3cDot11StaticWhiteListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11StaticWhiteListRowStatus.setStatus(_A)
_H3cDot11StaticBlackListTable_Object=MibTable
h3cDot11StaticBlackListTable=_H3cDot11StaticBlackListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,7))
if mibBuilder.loadTexts:h3cDot11StaticBlackListTable.setStatus(_A)
_H3cDot11StaticBlackListEntry_Object=MibTableRow
h3cDot11StaticBlackListEntry=_H3cDot11StaticBlackListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,7,1))
h3cDot11StaticBlackListEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:h3cDot11StaticBlackListEntry.setStatus(_A)
_H3cDot11StaticBlackListMAC_Type=MacAddress
_H3cDot11StaticBlackListMAC_Object=MibTableColumn
h3cDot11StaticBlackListMAC=_H3cDot11StaticBlackListMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,1,7,1,1),_H3cDot11StaticBlackListMAC_Type())
h3cDot11StaticBlackListMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11StaticBlackListMAC.setStatus(_A)
_H3cDot11StaticBlackListRowStatus_Type=RowStatus
_H3cDot11StaticBlackListRowStatus_Object=MibTableColumn
h3cDot11StaticBlackListRowStatus=_H3cDot11StaticBlackListRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,7,1,2),_H3cDot11StaticBlackListRowStatus_Type())
h3cDot11StaticBlackListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11StaticBlackListRowStatus.setStatus(_A)
_H3cDot11WIDSPermitBSSIDTable_Object=MibTable
h3cDot11WIDSPermitBSSIDTable=_H3cDot11WIDSPermitBSSIDTable_Object((1,3,6,1,4,1,2011,10,2,75,5,1,8))
if mibBuilder.loadTexts:h3cDot11WIDSPermitBSSIDTable.setStatus(_A)
_H3cDot11WIDSPermitBSSIDEntry_Object=MibTableRow
h3cDot11WIDSPermitBSSIDEntry=_H3cDot11WIDSPermitBSSIDEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,1,8,1))
h3cDot11WIDSPermitBSSIDEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:h3cDot11WIDSPermitBSSIDEntry.setStatus(_A)
_H3cDot11PermitBSSID_Type=MacAddress
_H3cDot11PermitBSSID_Object=MibTableColumn
h3cDot11PermitBSSID=_H3cDot11PermitBSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,1,8,1,1),_H3cDot11PermitBSSID_Type())
h3cDot11PermitBSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11PermitBSSID.setStatus(_A)
_H3cDot11PermitBSSIDDetected_Type=TruthValue
_H3cDot11PermitBSSIDDetected_Object=MibTableColumn
h3cDot11PermitBSSIDDetected=_H3cDot11PermitBSSIDDetected_Object((1,3,6,1,4,1,2011,10,2,75,5,1,8,1,2),_H3cDot11PermitBSSIDDetected_Type())
h3cDot11PermitBSSIDDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PermitBSSIDDetected.setStatus(_A)
_H3cDot11PermitBSSIDRowStatus_Type=RowStatus
_H3cDot11PermitBSSIDRowStatus_Object=MibTableColumn
h3cDot11PermitBSSIDRowStatus=_H3cDot11PermitBSSIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,1,8,1,3),_H3cDot11PermitBSSIDRowStatus_Type())
h3cDot11PermitBSSIDRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11PermitBSSIDRowStatus.setStatus(_A)
_H3cDot11WIDSDetectGroup_ObjectIdentity=ObjectIdentity
h3cDot11WIDSDetectGroup=_H3cDot11WIDSDetectGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,2))
_H3cDot11WIDSRogueAPTable_Object=MibTable
h3cDot11WIDSRogueAPTable=_H3cDot11WIDSRogueAPTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1))
if mibBuilder.loadTexts:h3cDot11WIDSRogueAPTable.setStatus(_A)
_H3cDot11WIDSRogueAPEntry_Object=MibTableRow
h3cDot11WIDSRogueAPEntry=_H3cDot11WIDSRogueAPEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1))
h3cDot11WIDSRogueAPEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:h3cDot11WIDSRogueAPEntry.setStatus(_A)
_H3cDot11RogueAPBSSMAC_Type=MacAddress
_H3cDot11RogueAPBSSMAC_Object=MibTableColumn
h3cDot11RogueAPBSSMAC=_H3cDot11RogueAPBSSMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,1),_H3cDot11RogueAPBSSMAC_Type())
h3cDot11RogueAPBSSMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RogueAPBSSMAC.setStatus(_A)
class _H3cDot11RogueAPVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11RogueAPVendorName_Type.__name__=_I
_H3cDot11RogueAPVendorName_Object=MibTableColumn
h3cDot11RogueAPVendorName=_H3cDot11RogueAPVendorName_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,2),_H3cDot11RogueAPVendorName_Type())
h3cDot11RogueAPVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPVendorName.setStatus(_A)
_H3cDot11RogueAPMonitorNum_Type=Integer32
_H3cDot11RogueAPMonitorNum_Object=MibTableColumn
h3cDot11RogueAPMonitorNum=_H3cDot11RogueAPMonitorNum_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,3),_H3cDot11RogueAPMonitorNum_Type())
h3cDot11RogueAPMonitorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPMonitorNum.setStatus(_A)
_H3cDot11RogueAPFirstDetectTm_Type=TimeTicks
_H3cDot11RogueAPFirstDetectTm_Object=MibTableColumn
h3cDot11RogueAPFirstDetectTm=_H3cDot11RogueAPFirstDetectTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,4),_H3cDot11RogueAPFirstDetectTm_Type())
h3cDot11RogueAPFirstDetectTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPFirstDetectTm.setStatus(_A)
_H3cDot11RogueAPLastDetectTm_Type=TimeTicks
_H3cDot11RogueAPLastDetectTm_Object=MibTableColumn
h3cDot11RogueAPLastDetectTm=_H3cDot11RogueAPLastDetectTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,5),_H3cDot11RogueAPLastDetectTm_Type())
h3cDot11RogueAPLastDetectTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPLastDetectTm.setStatus(_A)
_H3cDot11RogueAPSSID_Type=H3cDot11SSIDStringType
_H3cDot11RogueAPSSID_Object=MibTableColumn
h3cDot11RogueAPSSID=_H3cDot11RogueAPSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,6),_H3cDot11RogueAPSSID_Type())
h3cDot11RogueAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPSSID.setStatus(_A)
_H3cDot11RogueAPMaxSigStrength_Type=Integer32
_H3cDot11RogueAPMaxSigStrength_Object=MibTableColumn
h3cDot11RogueAPMaxSigStrength=_H3cDot11RogueAPMaxSigStrength_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,7),_H3cDot11RogueAPMaxSigStrength_Type())
h3cDot11RogueAPMaxSigStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPMaxSigStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RogueAPMaxSigStrength.setUnits(_K)
_H3cDot11RogueAPChannel_Type=H3cDot11ChannelScopeType
_H3cDot11RogueAPChannel_Object=MibTableColumn
h3cDot11RogueAPChannel=_H3cDot11RogueAPChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,8),_H3cDot11RogueAPChannel_Type())
h3cDot11RogueAPChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPChannel.setStatus(_A)
_H3cDot11RogueAPBeaconInterval_Type=Integer32
_H3cDot11RogueAPBeaconInterval_Object=MibTableColumn
h3cDot11RogueAPBeaconInterval=_H3cDot11RogueAPBeaconInterval_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,9),_H3cDot11RogueAPBeaconInterval_Type())
h3cDot11RogueAPBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RogueAPBeaconInterval.setUnits('millisecond')
_H3cDot11RogueAPAttackedStatus_Type=TruthValue
_H3cDot11RogueAPAttackedStatus_Object=MibTableColumn
h3cDot11RogueAPAttackedStatus=_H3cDot11RogueAPAttackedStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,10),_H3cDot11RogueAPAttackedStatus_Type())
h3cDot11RogueAPAttackedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPAttackedStatus.setStatus(_A)
class _H3cDot11RogueAPToIgnore_Type(TruthValue):defaultValue=2
_H3cDot11RogueAPToIgnore_Type.__name__=_P
_H3cDot11RogueAPToIgnore_Object=MibTableColumn
h3cDot11RogueAPToIgnore=_H3cDot11RogueAPToIgnore_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,11),_H3cDot11RogueAPToIgnore_Type())
h3cDot11RogueAPToIgnore.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RogueAPToIgnore.setStatus(_A)
_H3cDot11RogueAPEncryptStatus_Type=TruthValue
_H3cDot11RogueAPEncryptStatus_Object=MibTableColumn
h3cDot11RogueAPEncryptStatus=_H3cDot11RogueAPEncryptStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,12),_H3cDot11RogueAPEncryptStatus_Type())
h3cDot11RogueAPEncryptStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPEncryptStatus.setStatus(_A)
_H3cDot11RogueAPReset_Type=TruthValue
_H3cDot11RogueAPReset_Object=MibTableColumn
h3cDot11RogueAPReset=_H3cDot11RogueAPReset_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,13),_H3cDot11RogueAPReset_Type())
h3cDot11RogueAPReset.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RogueAPReset.setStatus(_A)
_H3cDot11RogueAPFirstDetectTmStr_Type=OctetString
_H3cDot11RogueAPFirstDetectTmStr_Object=MibTableColumn
h3cDot11RogueAPFirstDetectTmStr=_H3cDot11RogueAPFirstDetectTmStr_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,14),_H3cDot11RogueAPFirstDetectTmStr_Type())
h3cDot11RogueAPFirstDetectTmStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPFirstDetectTmStr.setStatus(_A)
_H3cDot11RogueAPLastDetectTmStr_Type=OctetString
_H3cDot11RogueAPLastDetectTmStr_Object=MibTableColumn
h3cDot11RogueAPLastDetectTmStr=_H3cDot11RogueAPLastDetectTmStr_Object((1,3,6,1,4,1,2011,10,2,75,5,2,1,1,15),_H3cDot11RogueAPLastDetectTmStr_Type())
h3cDot11RogueAPLastDetectTmStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueAPLastDetectTmStr.setStatus(_A)
_H3cDot11WIDSRogueAPExtTable_Object=MibTable
h3cDot11WIDSRogueAPExtTable=_H3cDot11WIDSRogueAPExtTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2))
if mibBuilder.loadTexts:h3cDot11WIDSRogueAPExtTable.setStatus(_A)
_H3cDot11WIDSRogueAPExtEntry_Object=MibTableRow
h3cDot11WIDSRogueAPExtEntry=_H3cDot11WIDSRogueAPExtEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1))
h3cDot11WIDSRogueAPExtEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:h3cDot11WIDSRogueAPExtEntry.setStatus(_A)
_H3cDot11WIDSAPID_Type=H3cDot11ObjectIDType
_H3cDot11WIDSAPID_Object=MibTableColumn
h3cDot11WIDSAPID=_H3cDot11WIDSAPID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,1),_H3cDot11WIDSAPID_Type())
h3cDot11WIDSAPID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSAPID.setStatus(_A)
_H3cDot11DetectCurAPSigStrength_Type=Integer32
_H3cDot11DetectCurAPSigStrength_Object=MibTableColumn
h3cDot11DetectCurAPSigStrength=_H3cDot11DetectCurAPSigStrength_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,2),_H3cDot11DetectCurAPSigStrength_Type())
h3cDot11DetectCurAPSigStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectCurAPSigStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DetectCurAPSigStrength.setUnits(_K)
_H3cDot11DetectAPByChannel_Type=H3cDot11ChannelScopeType
_H3cDot11DetectAPByChannel_Object=MibTableColumn
h3cDot11DetectAPByChannel=_H3cDot11DetectAPByChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,3),_H3cDot11DetectAPByChannel_Type())
h3cDot11DetectAPByChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectAPByChannel.setStatus(_A)
_H3cDot11DetectAPByRadioID_Type=H3cDot11RadioScopeType
_H3cDot11DetectAPByRadioID_Object=MibTableColumn
h3cDot11DetectAPByRadioID=_H3cDot11DetectAPByRadioID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,4),_H3cDot11DetectAPByRadioID_Type())
h3cDot11DetectAPByRadioID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectAPByRadioID.setStatus(_A)
_H3cDot11AttackAPStatus_Type=TruthValue
_H3cDot11AttackAPStatus_Object=MibTableColumn
h3cDot11AttackAPStatus=_H3cDot11AttackAPStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,5),_H3cDot11AttackAPStatus_Type())
h3cDot11AttackAPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AttackAPStatus.setStatus(_A)
_H3cDot11DetectAPFirstTm_Type=TimeTicks
_H3cDot11DetectAPFirstTm_Object=MibTableColumn
h3cDot11DetectAPFirstTm=_H3cDot11DetectAPFirstTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,6),_H3cDot11DetectAPFirstTm_Type())
h3cDot11DetectAPFirstTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectAPFirstTm.setStatus(_A)
_H3cDot11DetectAPLastTm_Type=TimeTicks
_H3cDot11DetectAPLastTm_Object=MibTableColumn
h3cDot11DetectAPLastTm=_H3cDot11DetectAPLastTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,2,1,7),_H3cDot11DetectAPLastTm_Type())
h3cDot11DetectAPLastTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectAPLastTm.setStatus(_A)
_H3cDot11WIDSRogueStaTable_Object=MibTable
h3cDot11WIDSRogueStaTable=_H3cDot11WIDSRogueStaTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3))
if mibBuilder.loadTexts:h3cDot11WIDSRogueStaTable.setStatus(_A)
_H3cDot11WIDSRogueStaEntry_Object=MibTableRow
h3cDot11WIDSRogueStaEntry=_H3cDot11WIDSRogueStaEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1))
h3cDot11WIDSRogueStaEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:h3cDot11WIDSRogueStaEntry.setStatus(_A)
_H3cDot11RogueStaMAC_Type=MacAddress
_H3cDot11RogueStaMAC_Object=MibTableColumn
h3cDot11RogueStaMAC=_H3cDot11RogueStaMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,1),_H3cDot11RogueStaMAC_Type())
h3cDot11RogueStaMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11RogueStaMAC.setStatus(_A)
class _H3cDot11RogueStaVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11RogueStaVendorName_Type.__name__=_I
_H3cDot11RogueStaVendorName_Object=MibTableColumn
h3cDot11RogueStaVendorName=_H3cDot11RogueStaVendorName_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,2),_H3cDot11RogueStaVendorName_Type())
h3cDot11RogueStaVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaVendorName.setStatus(_A)
_H3cDot11RogueStaMonitorNum_Type=Integer32
_H3cDot11RogueStaMonitorNum_Object=MibTableColumn
h3cDot11RogueStaMonitorNum=_H3cDot11RogueStaMonitorNum_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,3),_H3cDot11RogueStaMonitorNum_Type())
h3cDot11RogueStaMonitorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaMonitorNum.setStatus(_A)
_H3cDot11RogueStaFirstDetectTm_Type=TimeTicks
_H3cDot11RogueStaFirstDetectTm_Object=MibTableColumn
h3cDot11RogueStaFirstDetectTm=_H3cDot11RogueStaFirstDetectTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,4),_H3cDot11RogueStaFirstDetectTm_Type())
h3cDot11RogueStaFirstDetectTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaFirstDetectTm.setStatus(_A)
_H3cDot11RogueStaLastDetectTm_Type=TimeTicks
_H3cDot11RogueStaLastDetectTm_Object=MibTableColumn
h3cDot11RogueStaLastDetectTm=_H3cDot11RogueStaLastDetectTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,5),_H3cDot11RogueStaLastDetectTm_Type())
h3cDot11RogueStaLastDetectTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaLastDetectTm.setStatus(_A)
_H3cDot11RogueStaAccessBSSID_Type=MacAddress
_H3cDot11RogueStaAccessBSSID_Object=MibTableColumn
h3cDot11RogueStaAccessBSSID=_H3cDot11RogueStaAccessBSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,6),_H3cDot11RogueStaAccessBSSID_Type())
h3cDot11RogueStaAccessBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaAccessBSSID.setStatus(_A)
_H3cDot11RogueStaMaxSigStrength_Type=Integer32
_H3cDot11RogueStaMaxSigStrength_Object=MibTableColumn
h3cDot11RogueStaMaxSigStrength=_H3cDot11RogueStaMaxSigStrength_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,7),_H3cDot11RogueStaMaxSigStrength_Type())
h3cDot11RogueStaMaxSigStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaMaxSigStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RogueStaMaxSigStrength.setUnits(_K)
_H3cDot11RogueStaChannel_Type=H3cDot11ChannelScopeType
_H3cDot11RogueStaChannel_Object=MibTableColumn
h3cDot11RogueStaChannel=_H3cDot11RogueStaChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,8),_H3cDot11RogueStaChannel_Type())
h3cDot11RogueStaChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaChannel.setStatus(_A)
_H3cDot11RogueStaAttackedStatus_Type=TruthValue
_H3cDot11RogueStaAttackedStatus_Object=MibTableColumn
h3cDot11RogueStaAttackedStatus=_H3cDot11RogueStaAttackedStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,9),_H3cDot11RogueStaAttackedStatus_Type())
h3cDot11RogueStaAttackedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaAttackedStatus.setStatus(_A)
class _H3cDot11RogueStaToIgnore_Type(TruthValue):defaultValue=2
_H3cDot11RogueStaToIgnore_Type.__name__=_P
_H3cDot11RogueStaToIgnore_Object=MibTableColumn
h3cDot11RogueStaToIgnore=_H3cDot11RogueStaToIgnore_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,10),_H3cDot11RogueStaToIgnore_Type())
h3cDot11RogueStaToIgnore.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RogueStaToIgnore.setStatus(_A)
_H3cDot11RogueStaAdHocStatus_Type=TruthValue
_H3cDot11RogueStaAdHocStatus_Object=MibTableColumn
h3cDot11RogueStaAdHocStatus=_H3cDot11RogueStaAdHocStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,11),_H3cDot11RogueStaAdHocStatus_Type())
h3cDot11RogueStaAdHocStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaAdHocStatus.setStatus(_A)
_H3cDot11RogueStaReset_Type=TruthValue
_H3cDot11RogueStaReset_Object=MibTableColumn
h3cDot11RogueStaReset=_H3cDot11RogueStaReset_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,12),_H3cDot11RogueStaReset_Type())
h3cDot11RogueStaReset.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RogueStaReset.setStatus(_A)
_H3cDot11RogueStaFirstDetectTmStr_Type=OctetString
_H3cDot11RogueStaFirstDetectTmStr_Object=MibTableColumn
h3cDot11RogueStaFirstDetectTmStr=_H3cDot11RogueStaFirstDetectTmStr_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,13),_H3cDot11RogueStaFirstDetectTmStr_Type())
h3cDot11RogueStaFirstDetectTmStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaFirstDetectTmStr.setStatus(_A)
_H3cDot11RogueStaLastDetectTmStr_Type=OctetString
_H3cDot11RogueStaLastDetectTmStr_Object=MibTableColumn
h3cDot11RogueStaLastDetectTmStr=_H3cDot11RogueStaLastDetectTmStr_Object((1,3,6,1,4,1,2011,10,2,75,5,2,3,1,14),_H3cDot11RogueStaLastDetectTmStr_Type())
h3cDot11RogueStaLastDetectTmStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RogueStaLastDetectTmStr.setStatus(_A)
_H3cDot11WIDSRogueStaExtTable_Object=MibTable
h3cDot11WIDSRogueStaExtTable=_H3cDot11WIDSRogueStaExtTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4))
if mibBuilder.loadTexts:h3cDot11WIDSRogueStaExtTable.setStatus(_A)
_H3cDot11WIDSRogueStaExtEntry_Object=MibTableRow
h3cDot11WIDSRogueStaExtEntry=_H3cDot11WIDSRogueStaExtEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1))
h3cDot11WIDSRogueStaExtEntry.setIndexNames((0,_C,_S),(0,_C,_R))
if mibBuilder.loadTexts:h3cDot11WIDSRogueStaExtEntry.setStatus(_A)
_H3cDot11DetectCurStaSigStrength_Type=Integer32
_H3cDot11DetectCurStaSigStrength_Object=MibTableColumn
h3cDot11DetectCurStaSigStrength=_H3cDot11DetectCurStaSigStrength_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,1),_H3cDot11DetectCurStaSigStrength_Type())
h3cDot11DetectCurStaSigStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectCurStaSigStrength.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DetectCurStaSigStrength.setUnits(_K)
_H3cDot11DetectStaByChannel_Type=H3cDot11ChannelScopeType
_H3cDot11DetectStaByChannel_Object=MibTableColumn
h3cDot11DetectStaByChannel=_H3cDot11DetectStaByChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,2),_H3cDot11DetectStaByChannel_Type())
h3cDot11DetectStaByChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectStaByChannel.setStatus(_A)
_H3cDot11DetectStaByRadioID_Type=H3cDot11RadioScopeType
_H3cDot11DetectStaByRadioID_Object=MibTableColumn
h3cDot11DetectStaByRadioID=_H3cDot11DetectStaByRadioID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,3),_H3cDot11DetectStaByRadioID_Type())
h3cDot11DetectStaByRadioID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectStaByRadioID.setStatus(_A)
_H3cDot11AttackStaStatus_Type=TruthValue
_H3cDot11AttackStaStatus_Object=MibTableColumn
h3cDot11AttackStaStatus=_H3cDot11AttackStaStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,4),_H3cDot11AttackStaStatus_Type())
h3cDot11AttackStaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AttackStaStatus.setStatus(_A)
_H3cDot11DetectStaFirstTm_Type=TimeTicks
_H3cDot11DetectStaFirstTm_Object=MibTableColumn
h3cDot11DetectStaFirstTm=_H3cDot11DetectStaFirstTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,5),_H3cDot11DetectStaFirstTm_Type())
h3cDot11DetectStaFirstTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectStaFirstTm.setStatus(_A)
_H3cDot11DetectStaLastTm_Type=TimeTicks
_H3cDot11DetectStaLastTm_Object=MibTableColumn
h3cDot11DetectStaLastTm=_H3cDot11DetectStaLastTm_Object((1,3,6,1,4,1,2011,10,2,75,5,2,4,1,6),_H3cDot11DetectStaLastTm_Type())
h3cDot11DetectStaLastTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DetectStaLastTm.setStatus(_A)
_H3cDot11WIDSDetectedDevTable_Object=MibTable
h3cDot11WIDSDetectedDevTable=_H3cDot11WIDSDetectedDevTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5))
if mibBuilder.loadTexts:h3cDot11WIDSDetectedDevTable.setStatus(_A)
_H3cDot11WIDSDetectedDevEntry_Object=MibTableRow
h3cDot11WIDSDetectedDevEntry=_H3cDot11WIDSDetectedDevEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1))
h3cDot11WIDSDetectedDevEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:h3cDot11WIDSDetectedDevEntry.setStatus(_A)
_H3cDot11WIDSDevMAC_Type=MacAddress
_H3cDot11WIDSDevMAC_Object=MibTableColumn
h3cDot11WIDSDevMAC=_H3cDot11WIDSDevMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,1),_H3cDot11WIDSDevMAC_Type())
h3cDot11WIDSDevMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSDevMAC.setStatus(_A)
_H3cDot11WIDSDevType_Type=H3cDot11WIDSDevType
_H3cDot11WIDSDevType_Object=MibTableColumn
h3cDot11WIDSDevType=_H3cDot11WIDSDevType_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,2),_H3cDot11WIDSDevType_Type())
h3cDot11WIDSDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevType.setStatus(_A)
_H3cDot11WIDSDevPermitType_Type=H3cDot11WIDSDevPermitType
_H3cDot11WIDSDevPermitType_Object=MibTableColumn
h3cDot11WIDSDevPermitType=_H3cDot11WIDSDevPermitType_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,3),_H3cDot11WIDSDevPermitType_Type())
h3cDot11WIDSDevPermitType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevPermitType.setStatus(_A)
_H3cDot11WIDSDevVendor_Type=OctetString
_H3cDot11WIDSDevVendor_Object=MibTableColumn
h3cDot11WIDSDevVendor=_H3cDot11WIDSDevVendor_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,4),_H3cDot11WIDSDevVendor_Type())
h3cDot11WIDSDevVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevVendor.setStatus(_A)
_H3cDot11WIDSDevMonitorNum_Type=Integer32
_H3cDot11WIDSDevMonitorNum_Object=MibTableColumn
h3cDot11WIDSDevMonitorNum=_H3cDot11WIDSDevMonitorNum_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,5),_H3cDot11WIDSDevMonitorNum_Type())
h3cDot11WIDSDevMonitorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevMonitorNum.setStatus(_A)
_H3cDot11WIDSDevSSID_Type=OctetString
_H3cDot11WIDSDevSSID_Object=MibTableColumn
h3cDot11WIDSDevSSID=_H3cDot11WIDSDevSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,6),_H3cDot11WIDSDevSSID_Type())
h3cDot11WIDSDevSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevSSID.setStatus(_A)
_H3cDot11WIDSDevBSSID_Type=MacAddress
_H3cDot11WIDSDevBSSID_Object=MibTableColumn
h3cDot11WIDSDevBSSID=_H3cDot11WIDSDevBSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,7),_H3cDot11WIDSDevBSSID_Type())
h3cDot11WIDSDevBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevBSSID.setStatus(_A)
_H3cDot11WIDSDevChannel_Type=H3cDot11ChannelScopeType
_H3cDot11WIDSDevChannel_Object=MibTableColumn
h3cDot11WIDSDevChannel=_H3cDot11WIDSDevChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,8),_H3cDot11WIDSDevChannel_Type())
h3cDot11WIDSDevChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevChannel.setStatus(_A)
_H3cDot11WIDSDevMaxRSSI_Type=Integer32
_H3cDot11WIDSDevMaxRSSI_Object=MibTableColumn
h3cDot11WIDSDevMaxRSSI=_H3cDot11WIDSDevMaxRSSI_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,9),_H3cDot11WIDSDevMaxRSSI_Type())
h3cDot11WIDSDevMaxRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevMaxRSSI.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11WIDSDevMaxRSSI.setUnits('dbm')
_H3cDot11WIDSDevBeaconIntvl_Type=Integer32
_H3cDot11WIDSDevBeaconIntvl_Object=MibTableColumn
h3cDot11WIDSDevBeaconIntvl=_H3cDot11WIDSDevBeaconIntvl_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,10),_H3cDot11WIDSDevBeaconIntvl_Type())
h3cDot11WIDSDevBeaconIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevBeaconIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11WIDSDevBeaconIntvl.setUnits('millionsecond')
_H3cDot11WIDSDevFstDctTime_Type=DateAndTime
_H3cDot11WIDSDevFstDctTime_Object=MibTableColumn
h3cDot11WIDSDevFstDctTime=_H3cDot11WIDSDevFstDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,11),_H3cDot11WIDSDevFstDctTime_Type())
h3cDot11WIDSDevFstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevFstDctTime.setStatus(_A)
_H3cDot11WIDSDevLstDctTime_Type=DateAndTime
_H3cDot11WIDSDevLstDctTime_Object=MibTableColumn
h3cDot11WIDSDevLstDctTime=_H3cDot11WIDSDevLstDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,12),_H3cDot11WIDSDevLstDctTime_Type())
h3cDot11WIDSDevLstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevLstDctTime.setStatus(_A)
_H3cDot11WIDSDevReset_Type=TruthValue
_H3cDot11WIDSDevReset_Object=MibTableColumn
h3cDot11WIDSDevReset=_H3cDot11WIDSDevReset_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,13),_H3cDot11WIDSDevReset_Type())
h3cDot11WIDSDevReset.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WIDSDevReset.setStatus(_A)
_H3cDot11WIDSDevSnr_Type=Integer32
_H3cDot11WIDSDevSnr_Object=MibTableColumn
h3cDot11WIDSDevSnr=_H3cDot11WIDSDevSnr_Object((1,3,6,1,4,1,2011,10,2,75,5,2,5,1,14),_H3cDot11WIDSDevSnr_Type())
h3cDot11WIDSDevSnr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSDevSnr.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11WIDSDevSnr.setUnits('dB')
_H3cDot11WIDSRptAPTable_Object=MibTable
h3cDot11WIDSRptAPTable=_H3cDot11WIDSRptAPTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6))
if mibBuilder.loadTexts:h3cDot11WIDSRptAPTable.setStatus(_A)
_H3cDot11WIDSRptAPEntry_Object=MibTableRow
h3cDot11WIDSRptAPEntry=_H3cDot11WIDSRptAPEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1))
h3cDot11WIDSRptAPEntry.setIndexNames((0,_C,_T),(0,_C,_k))
if mibBuilder.loadTexts:h3cDot11WIDSRptAPEntry.setStatus(_A)
_H3cDot11WIDSRptAPMAC_Type=MacAddress
_H3cDot11WIDSRptAPMAC_Object=MibTableColumn
h3cDot11WIDSRptAPMAC=_H3cDot11WIDSRptAPMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,1),_H3cDot11WIDSRptAPMAC_Type())
h3cDot11WIDSRptAPMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPMAC.setStatus(_A)
_H3cDot11WIDSRptAPName_Type=OctetString
_H3cDot11WIDSRptAPName_Object=MibTableColumn
h3cDot11WIDSRptAPName=_H3cDot11WIDSRptAPName_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,2),_H3cDot11WIDSRptAPName_Type())
h3cDot11WIDSRptAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPName.setStatus(_A)
_H3cDot11WIDSRptAPRadioID_Type=H3cDot11RadioScopeType
_H3cDot11WIDSRptAPRadioID_Object=MibTableColumn
h3cDot11WIDSRptAPRadioID=_H3cDot11WIDSRptAPRadioID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,3),_H3cDot11WIDSRptAPRadioID_Type())
h3cDot11WIDSRptAPRadioID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPRadioID.setStatus(_A)
_H3cDot11WIDSRptAPMaxRSSI_Type=Integer32
_H3cDot11WIDSRptAPMaxRSSI_Object=MibTableColumn
h3cDot11WIDSRptAPMaxRSSI=_H3cDot11WIDSRptAPMaxRSSI_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,4),_H3cDot11WIDSRptAPMaxRSSI_Type())
h3cDot11WIDSRptAPMaxRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPMaxRSSI.setStatus(_A)
_H3cDot11WIDSRptAPFstDctTime_Type=DateAndTime
_H3cDot11WIDSRptAPFstDctTime_Object=MibTableColumn
h3cDot11WIDSRptAPFstDctTime=_H3cDot11WIDSRptAPFstDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,5),_H3cDot11WIDSRptAPFstDctTime_Type())
h3cDot11WIDSRptAPFstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPFstDctTime.setStatus(_A)
_H3cDot11WIDSRptAPLstDctTime_Type=DateAndTime
_H3cDot11WIDSRptAPLstDctTime_Object=MibTableColumn
h3cDot11WIDSRptAPLstDctTime=_H3cDot11WIDSRptAPLstDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,6,1,6),_H3cDot11WIDSRptAPLstDctTime_Type())
h3cDot11WIDSRptAPLstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRptAPLstDctTime.setStatus(_A)
_H3cDot11DynBlackListTable_Object=MibTable
h3cDot11DynBlackListTable=_H3cDot11DynBlackListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7))
if mibBuilder.loadTexts:h3cDot11DynBlackListTable.setStatus(_A)
_H3cDot11DynBlackListEntry_Object=MibTableRow
h3cDot11DynBlackListEntry=_H3cDot11DynBlackListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1))
h3cDot11DynBlackListEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:h3cDot11DynBlackListEntry.setStatus(_A)
_H3cDot11DynBlackListMAC_Type=MacAddress
_H3cDot11DynBlackListMAC_Object=MibTableColumn
h3cDot11DynBlackListMAC=_H3cDot11DynBlackListMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1,1),_H3cDot11DynBlackListMAC_Type())
h3cDot11DynBlackListMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11DynBlackListMAC.setStatus(_A)
_H3cDot11DynBlackListTime_Type=Unsigned32
_H3cDot11DynBlackListTime_Object=MibTableColumn
h3cDot11DynBlackListTime=_H3cDot11DynBlackListTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1,2),_H3cDot11DynBlackListTime_Type())
h3cDot11DynBlackListTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DynBlackListTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11DynBlackListTime.setUnits(_J)
_H3cDot11DynBlackListReason_Type=OctetString
_H3cDot11DynBlackListReason_Object=MibTableColumn
h3cDot11DynBlackListReason=_H3cDot11DynBlackListReason_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1,3),_H3cDot11DynBlackListReason_Type())
h3cDot11DynBlackListReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DynBlackListReason.setStatus(_A)
_H3cDot11DynBlackListReset_Type=TruthValue
_H3cDot11DynBlackListReset_Object=MibTableColumn
h3cDot11DynBlackListReset=_H3cDot11DynBlackListReset_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1,4),_H3cDot11DynBlackListReset_Type())
h3cDot11DynBlackListReset.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11DynBlackListReset.setStatus(_A)
_H3cDot11DynBlackListTimeTicks_Type=TimeTicks
_H3cDot11DynBlackListTimeTicks_Object=MibTableColumn
h3cDot11DynBlackListTimeTicks=_H3cDot11DynBlackListTimeTicks_Object((1,3,6,1,4,1,2011,10,2,75,5,2,7,1,5),_H3cDot11DynBlackListTimeTicks_Type())
h3cDot11DynBlackListTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DynBlackListTimeTicks.setStatus(_A)
_H3cDot11WIDSRogueHistoryTable_Object=MibTable
h3cDot11WIDSRogueHistoryTable=_H3cDot11WIDSRogueHistoryTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8))
if mibBuilder.loadTexts:h3cDot11WIDSRogueHistoryTable.setStatus(_A)
_H3cDot11WIDSRogueHistoryEntry_Object=MibTableRow
h3cDot11WIDSRogueHistoryEntry=_H3cDot11WIDSRogueHistoryEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1))
h3cDot11WIDSRogueHistoryEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:h3cDot11WIDSRogueHistoryEntry.setStatus(_A)
_H3cDot11WIDSRogueHisIndex_Type=Integer32
_H3cDot11WIDSRogueHisIndex_Object=MibTableColumn
h3cDot11WIDSRogueHisIndex=_H3cDot11WIDSRogueHisIndex_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,1),_H3cDot11WIDSRogueHisIndex_Type())
h3cDot11WIDSRogueHisIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisIndex.setStatus(_A)
_H3cDot11WIDSRogueHisMAC_Type=MacAddress
_H3cDot11WIDSRogueHisMAC_Object=MibTableColumn
h3cDot11WIDSRogueHisMAC=_H3cDot11WIDSRogueHisMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,2),_H3cDot11WIDSRogueHisMAC_Type())
h3cDot11WIDSRogueHisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisMAC.setStatus(_A)
_H3cDot11WIDSRogueHisVendor_Type=OctetString
_H3cDot11WIDSRogueHisVendor_Object=MibTableColumn
h3cDot11WIDSRogueHisVendor=_H3cDot11WIDSRogueHisVendor_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,3),_H3cDot11WIDSRogueHisVendor_Type())
h3cDot11WIDSRogueHisVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisVendor.setStatus(_A)
_H3cDot11WIDSRogueHisType_Type=H3cDot11WIDSDevType
_H3cDot11WIDSRogueHisType_Object=MibTableColumn
h3cDot11WIDSRogueHisType=_H3cDot11WIDSRogueHisType_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,4),_H3cDot11WIDSRogueHisType_Type())
h3cDot11WIDSRogueHisType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisType.setStatus(_A)
_H3cDot11WIDSRogueHisChl_Type=H3cDot11ChannelScopeType
_H3cDot11WIDSRogueHisChl_Object=MibTableColumn
h3cDot11WIDSRogueHisChl=_H3cDot11WIDSRogueHisChl_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,5),_H3cDot11WIDSRogueHisChl_Type())
h3cDot11WIDSRogueHisChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisChl.setStatus(_A)
_H3cDot11WIDSRogueHisSSID_Type=OctetString
_H3cDot11WIDSRogueHisSSID_Object=MibTableColumn
h3cDot11WIDSRogueHisSSID=_H3cDot11WIDSRogueHisSSID_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,6),_H3cDot11WIDSRogueHisSSID_Type())
h3cDot11WIDSRogueHisSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisSSID.setStatus(_A)
_H3cDot11WIDSRogueHisLastDctTime_Type=DateAndTime
_H3cDot11WIDSRogueHisLastDctTime_Object=MibTableColumn
h3cDot11WIDSRogueHisLastDctTime=_H3cDot11WIDSRogueHisLastDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,8,1,7),_H3cDot11WIDSRogueHisLastDctTime_Type())
h3cDot11WIDSRogueHisLastDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSRogueHisLastDctTime.setStatus(_A)
_H3cDot11WIDSAtkHistroyTable_Object=MibTable
h3cDot11WIDSAtkHistroyTable=_H3cDot11WIDSAtkHistroyTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9))
if mibBuilder.loadTexts:h3cDot11WIDSAtkHistroyTable.setStatus(_A)
_H3cDot11WIDSAtkHistroyEntry_Object=MibTableRow
h3cDot11WIDSAtkHistroyEntry=_H3cDot11WIDSAtkHistroyEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1))
h3cDot11WIDSAtkHistroyEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:h3cDot11WIDSAtkHistroyEntry.setStatus(_A)
_H3cDot11WIDSAtkHisIndex_Type=Integer32
_H3cDot11WIDSAtkHisIndex_Object=MibTableColumn
h3cDot11WIDSAtkHisIndex=_H3cDot11WIDSAtkHisIndex_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,1),_H3cDot11WIDSAtkHisIndex_Type())
h3cDot11WIDSAtkHisIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisIndex.setStatus(_A)
_H3cDot11WIDSAtkHisMAC_Type=MacAddress
_H3cDot11WIDSAtkHisMAC_Object=MibTableColumn
h3cDot11WIDSAtkHisMAC=_H3cDot11WIDSAtkHisMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,2),_H3cDot11WIDSAtkHisMAC_Type())
h3cDot11WIDSAtkHisMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisMAC.setStatus(_A)
_H3cDot11WIDSAtkHisType_Type=H3cDot11WIDSAtkType
_H3cDot11WIDSAtkHisType_Object=MibTableColumn
h3cDot11WIDSAtkHisType=_H3cDot11WIDSAtkHisType_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,3),_H3cDot11WIDSAtkHisType_Type())
h3cDot11WIDSAtkHisType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisType.setStatus(_A)
_H3cDot11WIDSAtkHisChl_Type=H3cDot11ChannelScopeType
_H3cDot11WIDSAtkHisChl_Object=MibTableColumn
h3cDot11WIDSAtkHisChl=_H3cDot11WIDSAtkHisChl_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,4),_H3cDot11WIDSAtkHisChl_Type())
h3cDot11WIDSAtkHisChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisChl.setStatus(_A)
_H3cDot11WIDSAtkHisRSSI_Type=Integer32
_H3cDot11WIDSAtkHisRSSI_Object=MibTableColumn
h3cDot11WIDSAtkHisRSSI=_H3cDot11WIDSAtkHisRSSI_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,5),_H3cDot11WIDSAtkHisRSSI_Type())
h3cDot11WIDSAtkHisRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisRSSI.setStatus(_A)
_H3cDot11WIDSAtkHisDctTime_Type=DateAndTime
_H3cDot11WIDSAtkHisDctTime_Object=MibTableColumn
h3cDot11WIDSAtkHisDctTime=_H3cDot11WIDSAtkHisDctTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,6),_H3cDot11WIDSAtkHisDctTime_Type())
h3cDot11WIDSAtkHisDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisDctTime.setStatus(_A)
_H3cDot11WIDSAtkHisAPName_Type=OctetString
_H3cDot11WIDSAtkHisAPName_Object=MibTableColumn
h3cDot11WIDSAtkHisAPName=_H3cDot11WIDSAtkHisAPName_Object((1,3,6,1,4,1,2011,10,2,75,5,2,9,1,7),_H3cDot11WIDSAtkHisAPName_Type())
h3cDot11WIDSAtkHisAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkHisAPName.setStatus(_A)
_H3cDot11WIDSAtkStatis_ObjectIdentity=ObjectIdentity
h3cDot11WIDSAtkStatis=_H3cDot11WIDSAtkStatis_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,2,10))
_H3cDot11WIDSAtkStasStartTime_Type=DateAndTime
_H3cDot11WIDSAtkStasStartTime_Object=MibScalar
h3cDot11WIDSAtkStasStartTime=_H3cDot11WIDSAtkStasStartTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,1),_H3cDot11WIDSAtkStasStartTime_Type())
h3cDot11WIDSAtkStasStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasStartTime.setStatus(_A)
_H3cDot11WIDSAtkStasTable_Object=MibTable
h3cDot11WIDSAtkStasTable=_H3cDot11WIDSAtkStasTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,2))
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasTable.setStatus(_A)
_H3cDot11WIDSAtkStasEntry_Object=MibTableRow
h3cDot11WIDSAtkStasEntry=_H3cDot11WIDSAtkStasEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,2,1))
h3cDot11WIDSAtkStasEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasEntry.setStatus(_A)
_H3cDot11WIDSAtkStasType_Type=H3cDot11WIDSAtkType
_H3cDot11WIDSAtkStasType_Object=MibTableColumn
h3cDot11WIDSAtkStasType=_H3cDot11WIDSAtkStasType_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,2,1,1),_H3cDot11WIDSAtkStasType_Type())
h3cDot11WIDSAtkStasType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasType.setStatus(_A)
_H3cDot11WIDSAtkStasCurCnt_Type=Unsigned32
_H3cDot11WIDSAtkStasCurCnt_Object=MibTableColumn
h3cDot11WIDSAtkStasCurCnt=_H3cDot11WIDSAtkStasCurCnt_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,2,1,2),_H3cDot11WIDSAtkStasCurCnt_Type())
h3cDot11WIDSAtkStasCurCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasCurCnt.setStatus(_A)
_H3cDot11WIDSAtkStasTotalCnt_Type=Unsigned32
_H3cDot11WIDSAtkStasTotalCnt_Object=MibTableColumn
h3cDot11WIDSAtkStasTotalCnt=_H3cDot11WIDSAtkStasTotalCnt_Object((1,3,6,1,4,1,2011,10,2,75,5,2,10,2,1,3),_H3cDot11WIDSAtkStasTotalCnt_Type())
h3cDot11WIDSAtkStasTotalCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WIDSAtkStasTotalCnt.setStatus(_A)
_H3cDot11BlackListTable_Object=MibTable
h3cDot11BlackListTable=_H3cDot11BlackListTable_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11))
if mibBuilder.loadTexts:h3cDot11BlackListTable.setStatus(_A)
_H3cDot11BlackListEntry_Object=MibTableRow
h3cDot11BlackListEntry=_H3cDot11BlackListEntry_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1))
h3cDot11BlackListEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:h3cDot11BlackListEntry.setStatus(_A)
_H3cDot11BlackListMAC_Type=MacAddress
_H3cDot11BlackListMAC_Object=MibTableColumn
h3cDot11BlackListMAC=_H3cDot11BlackListMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1,1),_H3cDot11BlackListMAC_Type())
h3cDot11BlackListMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDot11BlackListMAC.setStatus(_A)
_H3cDot11BlackListTime_Type=Unsigned32
_H3cDot11BlackListTime_Object=MibTableColumn
h3cDot11BlackListTime=_H3cDot11BlackListTime_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1,2),_H3cDot11BlackListTime_Type())
h3cDot11BlackListTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BlackListTime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11BlackListTime.setUnits('minutes')
_H3cDot11BlackListReason_Type=OctetString
_H3cDot11BlackListReason_Object=MibTableColumn
h3cDot11BlackListReason=_H3cDot11BlackListReason_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1,3),_H3cDot11BlackListReason_Type())
h3cDot11BlackListReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BlackListReason.setStatus(_A)
_H3cDot11BlackListRowStatus_Type=RowStatus
_H3cDot11BlackListRowStatus_Object=MibTableColumn
h3cDot11BlackListRowStatus=_H3cDot11BlackListRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1,4),_H3cDot11BlackListRowStatus_Type())
h3cDot11BlackListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11BlackListRowStatus.setStatus(_A)
_H3cDot11BlackListTimeTicks_Type=TimeTicks
_H3cDot11BlackListTimeTicks_Object=MibTableColumn
h3cDot11BlackListTimeTicks=_H3cDot11BlackListTimeTicks_Object((1,3,6,1,4,1,2011,10,2,75,5,2,11,1,5),_H3cDot11BlackListTimeTicks_Type())
h3cDot11BlackListTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BlackListTimeTicks.setStatus(_A)
_H3cDot11WIDSNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11WIDSNotifyGroup=_H3cDot11WIDSNotifyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,3))
_H3cDot11WIDSTraps_ObjectIdentity=ObjectIdentity
h3cDot11WIDSTraps=_H3cDot11WIDSTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,3,1))
_H3cDot11WIDSTrapVarObjects_ObjectIdentity=ObjectIdentity
h3cDot11WIDSTrapVarObjects=_H3cDot11WIDSTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,5,3,2))
_H3cDot11WIDSRogueMAC_Type=MacAddress
_H3cDot11WIDSRogueMAC_Object=MibScalar
h3cDot11WIDSRogueMAC=_H3cDot11WIDSRogueMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,1),_H3cDot11WIDSRogueMAC_Type())
h3cDot11WIDSRogueMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSRogueMAC.setStatus(_A)
class _H3cDot11WIDSRogueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rogueAp',1),('rogueStation',2)))
_H3cDot11WIDSRogueType_Type.__name__=_H
_H3cDot11WIDSRogueType_Object=MibScalar
h3cDot11WIDSRogueType=_H3cDot11WIDSRogueType_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,2),_H3cDot11WIDSRogueType_Type())
h3cDot11WIDSRogueType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSRogueType.setStatus(_A)
_H3cDot11WIDSMonitorMAC_Type=MacAddress
_H3cDot11WIDSMonitorMAC_Object=MibScalar
h3cDot11WIDSMonitorMAC=_H3cDot11WIDSMonitorMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,3),_H3cDot11WIDSMonitorMAC_Type())
h3cDot11WIDSMonitorMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSMonitorMAC.setStatus(_A)
_H3cDot11WIDSAdHocMAC_Type=MacAddress
_H3cDot11WIDSAdHocMAC_Object=MibScalar
h3cDot11WIDSAdHocMAC=_H3cDot11WIDSAdHocMAC_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,4),_H3cDot11WIDSAdHocMAC_Type())
h3cDot11WIDSAdHocMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAdHocMAC.setStatus(_A)
_H3cDot11UnauthorSSIDName_Type=H3cDot11SSIDStringType
_H3cDot11UnauthorSSIDName_Object=MibScalar
h3cDot11UnauthorSSIDName=_H3cDot11UnauthorSSIDName_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,5),_H3cDot11UnauthorSSIDName_Type())
h3cDot11UnauthorSSIDName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11UnauthorSSIDName.setStatus(_A)
_H3cDot11MonitorAPID_Type=H3cDot11ObjectIDType
_H3cDot11MonitorAPID_Object=MibScalar
h3cDot11MonitorAPID=_H3cDot11MonitorAPID_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,6),_H3cDot11MonitorAPID_Type())
h3cDot11MonitorAPID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11MonitorAPID.setStatus(_A)
_H3cDot11MonitorApRadioID_Type=H3cDot11RadioScopeType
_H3cDot11MonitorApRadioID_Object=MibScalar
h3cDot11MonitorApRadioID=_H3cDot11MonitorApRadioID_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,7),_H3cDot11MonitorApRadioID_Type())
h3cDot11MonitorApRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11MonitorApRadioID.setStatus(_A)
_H3cDot11WIDSAtkMac_Type=MacAddress
_H3cDot11WIDSAtkMac_Object=MibScalar
h3cDot11WIDSAtkMac=_H3cDot11WIDSAtkMac_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,8),_H3cDot11WIDSAtkMac_Type())
h3cDot11WIDSAtkMac.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAtkMac.setStatus(_A)
_H3cDot11WIDSAtkFrameType_Type=OctetString
_H3cDot11WIDSAtkFrameType_Object=MibScalar
h3cDot11WIDSAtkFrameType=_H3cDot11WIDSAtkFrameType_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,9),_H3cDot11WIDSAtkFrameType_Type())
h3cDot11WIDSAtkFrameType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAtkFrameType.setStatus(_A)
_H3cDot11WIDSAtkChannel_Type=H3cDot11ChannelScopeType
_H3cDot11WIDSAtkChannel_Object=MibScalar
h3cDot11WIDSAtkChannel=_H3cDot11WIDSAtkChannel_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,10),_H3cDot11WIDSAtkChannel_Type())
h3cDot11WIDSAtkChannel.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAtkChannel.setStatus(_A)
_H3cDot11WIDSAtkTime_Type=OctetString
_H3cDot11WIDSAtkTime_Object=MibScalar
h3cDot11WIDSAtkTime=_H3cDot11WIDSAtkTime_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,11),_H3cDot11WIDSAtkTime_Type())
h3cDot11WIDSAtkTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAtkTime.setStatus(_A)
_H3cDot11WIDSAtkDestMac_Type=MacAddress
_H3cDot11WIDSAtkDestMac_Object=MibScalar
h3cDot11WIDSAtkDestMac=_H3cDot11WIDSAtkDestMac_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,12),_H3cDot11WIDSAtkDestMac_Type())
h3cDot11WIDSAtkDestMac.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSAtkDestMac.setStatus(_A)
_H3cDot11WIDSFirstTrapTime_Type=TimeTicks
_H3cDot11WIDSFirstTrapTime_Object=MibScalar
h3cDot11WIDSFirstTrapTime=_H3cDot11WIDSFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,75,5,3,2,13),_H3cDot11WIDSFirstTrapTime_Type())
h3cDot11WIDSFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WIDSFirstTrapTime.setStatus(_A)
h3cDot11WIDSDetectRogueTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,1))
h3cDot11WIDSDetectRogueTrap.setObjects(*((_C,_U),(_C,_q),(_C,_L),(_C,_V),(_C,_W)))
if mibBuilder.loadTexts:h3cDot11WIDSDetectRogueTrap.setStatus(_A)
h3cDot11WIDSAdHocTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,2))
h3cDot11WIDSAdHocTrap.setObjects(*((_C,_r),(_C,_L)))
if mibBuilder.loadTexts:h3cDot11WIDSAdHocTrap.setStatus(_A)
h3cDot11WIDSUnauthorSSIDTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,3))
h3cDot11WIDSUnauthorSSIDTrap.setObjects(*((_C,_s),(_C,_L),(_C,_V),(_C,_W)))
if mibBuilder.loadTexts:h3cDot11WIDSUnauthorSSIDTrap.setStatus(_A)
h3cDot11WIDSDisappearRogueTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,4))
h3cDot11WIDSDisappearRogueTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:h3cDot11WIDSDisappearRogueTrap.setStatus(_A)
h3cDot11WIDSDetectAttack=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,5))
h3cDot11WIDSDetectAttack.setObjects(*((_C,_t),(_C,_u),(_C,_v),(_C,_w)))
if mibBuilder.loadTexts:h3cDot11WIDSDetectAttack.setStatus(_A)
h3cDot11WIDSDetectWBridge=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,6))
h3cDot11WIDSDetectWBridge.setObjects(*((_C,_x),(_C,_y),(_C,_z)))
if mibBuilder.loadTexts:h3cDot11WIDSDetectWBridge.setStatus(_A)
h3cDot11WIDSFloodTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,7))
h3cDot11WIDSFloodTrap.setObjects(*((_C,_M),(_C,_X),(_C,_N)))
if mibBuilder.loadTexts:h3cDot11WIDSFloodTrap.setStatus(_A)
h3cDot11WIDSSpoofTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,8))
h3cDot11WIDSSpoofTrap.setObjects(*((_C,_M),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_N)))
if mibBuilder.loadTexts:h3cDot11WIDSSpoofTrap.setStatus(_A)
h3cDot11WIDSWeakIVTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,5,3,1,9))
h3cDot11WIDSWeakIVTrap.setObjects(*((_C,_M),(_C,_Y),(_C,_Z),(_C,_a),(_C,_N)))
if mibBuilder.loadTexts:h3cDot11WIDSWeakIVTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'H3cDot11WIDSDevType':H3cDot11WIDSDevType,'H3cDot11WIDSDevPermitType':H3cDot11WIDSDevPermitType,'H3cDot11WIDSAtkType':H3cDot11WIDSAtkType,'h3cDot11WIDS':h3cDot11WIDS,'h3cDot11WIDSConfigGroup':h3cDot11WIDSConfigGroup,'h3cDot11WIDSGlobalConfigGroup':h3cDot11WIDSGlobalConfigGroup,'h3cDot11WIDSScanMode':h3cDot11WIDSScanMode,'h3cDot11WIDSScanChannelList':h3cDot11WIDSScanChannelList,'h3cDot11CntMsrMode':h3cDot11CntMsrMode,'h3cDot11DevAgingTime':h3cDot11DevAgingTime,'h3cDot11DynBlkListEnable':h3cDot11DynBlkListEnable,'h3cDot11DynBlkListLifeTime':h3cDot11DynBlkListLifeTime,'h3cDot11FloodAtkDctEnable':h3cDot11FloodAtkDctEnable,'h3cDot11SpoofAtkDctEnable':h3cDot11SpoofAtkDctEnable,'h3cDot11WeakIVAtkDctEnable':h3cDot11WeakIVAtkDctEnable,'h3cDot11ResetWIDSRogueHistory':h3cDot11ResetWIDSRogueHistory,'h3cDot11ResetWIDSHistroy':h3cDot11ResetWIDSHistroy,'h3cDot11ResetWIDSStatistics':h3cDot11ResetWIDSStatistics,'h3cDot11ResetAllDynBlkList':h3cDot11ResetAllDynBlkList,'h3cDot11ResetAllStcBlkList':h3cDot11ResetAllStcBlkList,'h3cDot11ResetAllWhtBlkList':h3cDot11ResetAllWhtBlkList,'h3cDot11ResetAllDctRogueAP':h3cDot11ResetAllDctRogueAP,'h3cDot11ResetAllDctRogueSta':h3cDot11ResetAllDctRogueSta,'h3cDot11ResetAllDctAdhoc':h3cDot11ResetAllDctAdhoc,'h3cDot11ResetAllDctDevice':h3cDot11ResetAllDctDevice,'h3cDot11ResetAllDctSSID':h3cDot11ResetAllDctSSID,'h3cDot11WidsFloodInterval':h3cDot11WidsFloodInterval,'h3cDot11WidsBlackListThreshold':h3cDot11WidsBlackListThreshold,'h3cDot11SSIDFilterOnOff':h3cDot11SSIDFilterOnOff,'h3cDot11BSSIDFilterOnOff':h3cDot11BSSIDFilterOnOff,'h3cDot11WIDSPermitVendorTable':h3cDot11WIDSPermitVendorTable,'h3cDot11WIDSPermitVendorEntry':h3cDot11WIDSPermitVendorEntry,_d:h3cDot11VendorOUI,'h3cDot11PermitVendorRowStatus':h3cDot11PermitVendorRowStatus,'h3cDot11VendorName':h3cDot11VendorName,'h3cDot11WIDSPermitSSIDTable':h3cDot11WIDSPermitSSIDTable,'h3cDot11WIDSPermitSSIDEntry':h3cDot11WIDSPermitSSIDEntry,_e:h3cDot11PermitSSID,'h3cDot11PermitSSIDRowStatus':h3cDot11PermitSSIDRowStatus,'h3cDot11PermitSSIDDetected':h3cDot11PermitSSIDDetected,'h3cDot11WIDSIgnoreListTable':h3cDot11WIDSIgnoreListTable,'h3cDot11WIDSIgnoreListEntry':h3cDot11WIDSIgnoreListEntry,_f:h3cDot11IgnoreMAC,'h3cDot11IgnoreListRowStatus':h3cDot11IgnoreListRowStatus,'h3cDot11IgnoreMACDetected':h3cDot11IgnoreMACDetected,'h3cDot11IgnoreDevType':h3cDot11IgnoreDevType,'h3cDot11WIDSAttackListTable':h3cDot11WIDSAttackListTable,'h3cDot11WIDSAttackListEntry':h3cDot11WIDSAttackListEntry,_g:h3cDot11AttackDeviceMac,'h3cDot11AttackListRowStatus':h3cDot11AttackListRowStatus,'h3cDot11AttackDevDetected':h3cDot11AttackDevDetected,'h3cDot11AttackDevType':h3cDot11AttackDevType,'h3cDot11StaticWhiteListTable':h3cDot11StaticWhiteListTable,'h3cDot11StaticWhiteListEntry':h3cDot11StaticWhiteListEntry,_h:h3cDot11StaticWhiteListMAC,'h3cDot11StaticWhiteListRowStatus':h3cDot11StaticWhiteListRowStatus,'h3cDot11StaticBlackListTable':h3cDot11StaticBlackListTable,'h3cDot11StaticBlackListEntry':h3cDot11StaticBlackListEntry,_i:h3cDot11StaticBlackListMAC,'h3cDot11StaticBlackListRowStatus':h3cDot11StaticBlackListRowStatus,'h3cDot11WIDSPermitBSSIDTable':h3cDot11WIDSPermitBSSIDTable,'h3cDot11WIDSPermitBSSIDEntry':h3cDot11WIDSPermitBSSIDEntry,_j:h3cDot11PermitBSSID,'h3cDot11PermitBSSIDDetected':h3cDot11PermitBSSIDDetected,'h3cDot11PermitBSSIDRowStatus':h3cDot11PermitBSSIDRowStatus,'h3cDot11WIDSDetectGroup':h3cDot11WIDSDetectGroup,'h3cDot11WIDSRogueAPTable':h3cDot11WIDSRogueAPTable,'h3cDot11WIDSRogueAPEntry':h3cDot11WIDSRogueAPEntry,_Q:h3cDot11RogueAPBSSMAC,'h3cDot11RogueAPVendorName':h3cDot11RogueAPVendorName,'h3cDot11RogueAPMonitorNum':h3cDot11RogueAPMonitorNum,'h3cDot11RogueAPFirstDetectTm':h3cDot11RogueAPFirstDetectTm,'h3cDot11RogueAPLastDetectTm':h3cDot11RogueAPLastDetectTm,'h3cDot11RogueAPSSID':h3cDot11RogueAPSSID,'h3cDot11RogueAPMaxSigStrength':h3cDot11RogueAPMaxSigStrength,'h3cDot11RogueAPChannel':h3cDot11RogueAPChannel,'h3cDot11RogueAPBeaconInterval':h3cDot11RogueAPBeaconInterval,'h3cDot11RogueAPAttackedStatus':h3cDot11RogueAPAttackedStatus,'h3cDot11RogueAPToIgnore':h3cDot11RogueAPToIgnore,'h3cDot11RogueAPEncryptStatus':h3cDot11RogueAPEncryptStatus,'h3cDot11RogueAPReset':h3cDot11RogueAPReset,'h3cDot11RogueAPFirstDetectTmStr':h3cDot11RogueAPFirstDetectTmStr,'h3cDot11RogueAPLastDetectTmStr':h3cDot11RogueAPLastDetectTmStr,'h3cDot11WIDSRogueAPExtTable':h3cDot11WIDSRogueAPExtTable,'h3cDot11WIDSRogueAPExtEntry':h3cDot11WIDSRogueAPExtEntry,_R:h3cDot11WIDSAPID,'h3cDot11DetectCurAPSigStrength':h3cDot11DetectCurAPSigStrength,'h3cDot11DetectAPByChannel':h3cDot11DetectAPByChannel,'h3cDot11DetectAPByRadioID':h3cDot11DetectAPByRadioID,'h3cDot11AttackAPStatus':h3cDot11AttackAPStatus,'h3cDot11DetectAPFirstTm':h3cDot11DetectAPFirstTm,'h3cDot11DetectAPLastTm':h3cDot11DetectAPLastTm,'h3cDot11WIDSRogueStaTable':h3cDot11WIDSRogueStaTable,'h3cDot11WIDSRogueStaEntry':h3cDot11WIDSRogueStaEntry,_S:h3cDot11RogueStaMAC,'h3cDot11RogueStaVendorName':h3cDot11RogueStaVendorName,'h3cDot11RogueStaMonitorNum':h3cDot11RogueStaMonitorNum,'h3cDot11RogueStaFirstDetectTm':h3cDot11RogueStaFirstDetectTm,'h3cDot11RogueStaLastDetectTm':h3cDot11RogueStaLastDetectTm,'h3cDot11RogueStaAccessBSSID':h3cDot11RogueStaAccessBSSID,'h3cDot11RogueStaMaxSigStrength':h3cDot11RogueStaMaxSigStrength,'h3cDot11RogueStaChannel':h3cDot11RogueStaChannel,'h3cDot11RogueStaAttackedStatus':h3cDot11RogueStaAttackedStatus,'h3cDot11RogueStaToIgnore':h3cDot11RogueStaToIgnore,'h3cDot11RogueStaAdHocStatus':h3cDot11RogueStaAdHocStatus,'h3cDot11RogueStaReset':h3cDot11RogueStaReset,'h3cDot11RogueStaFirstDetectTmStr':h3cDot11RogueStaFirstDetectTmStr,'h3cDot11RogueStaLastDetectTmStr':h3cDot11RogueStaLastDetectTmStr,'h3cDot11WIDSRogueStaExtTable':h3cDot11WIDSRogueStaExtTable,'h3cDot11WIDSRogueStaExtEntry':h3cDot11WIDSRogueStaExtEntry,'h3cDot11DetectCurStaSigStrength':h3cDot11DetectCurStaSigStrength,'h3cDot11DetectStaByChannel':h3cDot11DetectStaByChannel,'h3cDot11DetectStaByRadioID':h3cDot11DetectStaByRadioID,'h3cDot11AttackStaStatus':h3cDot11AttackStaStatus,'h3cDot11DetectStaFirstTm':h3cDot11DetectStaFirstTm,'h3cDot11DetectStaLastTm':h3cDot11DetectStaLastTm,'h3cDot11WIDSDetectedDevTable':h3cDot11WIDSDetectedDevTable,'h3cDot11WIDSDetectedDevEntry':h3cDot11WIDSDetectedDevEntry,_T:h3cDot11WIDSDevMAC,'h3cDot11WIDSDevType':h3cDot11WIDSDevType,'h3cDot11WIDSDevPermitType':h3cDot11WIDSDevPermitType,'h3cDot11WIDSDevVendor':h3cDot11WIDSDevVendor,'h3cDot11WIDSDevMonitorNum':h3cDot11WIDSDevMonitorNum,'h3cDot11WIDSDevSSID':h3cDot11WIDSDevSSID,'h3cDot11WIDSDevBSSID':h3cDot11WIDSDevBSSID,'h3cDot11WIDSDevChannel':h3cDot11WIDSDevChannel,'h3cDot11WIDSDevMaxRSSI':h3cDot11WIDSDevMaxRSSI,'h3cDot11WIDSDevBeaconIntvl':h3cDot11WIDSDevBeaconIntvl,'h3cDot11WIDSDevFstDctTime':h3cDot11WIDSDevFstDctTime,'h3cDot11WIDSDevLstDctTime':h3cDot11WIDSDevLstDctTime,'h3cDot11WIDSDevReset':h3cDot11WIDSDevReset,'h3cDot11WIDSDevSnr':h3cDot11WIDSDevSnr,'h3cDot11WIDSRptAPTable':h3cDot11WIDSRptAPTable,'h3cDot11WIDSRptAPEntry':h3cDot11WIDSRptAPEntry,_k:h3cDot11WIDSRptAPMAC,_x:h3cDot11WIDSRptAPName,_y:h3cDot11WIDSRptAPRadioID,'h3cDot11WIDSRptAPMaxRSSI':h3cDot11WIDSRptAPMaxRSSI,'h3cDot11WIDSRptAPFstDctTime':h3cDot11WIDSRptAPFstDctTime,_z:h3cDot11WIDSRptAPLstDctTime,'h3cDot11DynBlackListTable':h3cDot11DynBlackListTable,'h3cDot11DynBlackListEntry':h3cDot11DynBlackListEntry,_l:h3cDot11DynBlackListMAC,'h3cDot11DynBlackListTime':h3cDot11DynBlackListTime,'h3cDot11DynBlackListReason':h3cDot11DynBlackListReason,'h3cDot11DynBlackListReset':h3cDot11DynBlackListReset,'h3cDot11DynBlackListTimeTicks':h3cDot11DynBlackListTimeTicks,'h3cDot11WIDSRogueHistoryTable':h3cDot11WIDSRogueHistoryTable,'h3cDot11WIDSRogueHistoryEntry':h3cDot11WIDSRogueHistoryEntry,_m:h3cDot11WIDSRogueHisIndex,'h3cDot11WIDSRogueHisMAC':h3cDot11WIDSRogueHisMAC,'h3cDot11WIDSRogueHisVendor':h3cDot11WIDSRogueHisVendor,'h3cDot11WIDSRogueHisType':h3cDot11WIDSRogueHisType,'h3cDot11WIDSRogueHisChl':h3cDot11WIDSRogueHisChl,'h3cDot11WIDSRogueHisSSID':h3cDot11WIDSRogueHisSSID,'h3cDot11WIDSRogueHisLastDctTime':h3cDot11WIDSRogueHisLastDctTime,'h3cDot11WIDSAtkHistroyTable':h3cDot11WIDSAtkHistroyTable,'h3cDot11WIDSAtkHistroyEntry':h3cDot11WIDSAtkHistroyEntry,_n:h3cDot11WIDSAtkHisIndex,'h3cDot11WIDSAtkHisMAC':h3cDot11WIDSAtkHisMAC,_t:h3cDot11WIDSAtkHisType,_u:h3cDot11WIDSAtkHisChl,'h3cDot11WIDSAtkHisRSSI':h3cDot11WIDSAtkHisRSSI,_v:h3cDot11WIDSAtkHisDctTime,_w:h3cDot11WIDSAtkHisAPName,'h3cDot11WIDSAtkStatis':h3cDot11WIDSAtkStatis,'h3cDot11WIDSAtkStasStartTime':h3cDot11WIDSAtkStasStartTime,'h3cDot11WIDSAtkStasTable':h3cDot11WIDSAtkStasTable,'h3cDot11WIDSAtkStasEntry':h3cDot11WIDSAtkStasEntry,_o:h3cDot11WIDSAtkStasType,'h3cDot11WIDSAtkStasCurCnt':h3cDot11WIDSAtkStasCurCnt,'h3cDot11WIDSAtkStasTotalCnt':h3cDot11WIDSAtkStasTotalCnt,'h3cDot11BlackListTable':h3cDot11BlackListTable,'h3cDot11BlackListEntry':h3cDot11BlackListEntry,_p:h3cDot11BlackListMAC,'h3cDot11BlackListTime':h3cDot11BlackListTime,'h3cDot11BlackListReason':h3cDot11BlackListReason,'h3cDot11BlackListRowStatus':h3cDot11BlackListRowStatus,'h3cDot11BlackListTimeTicks':h3cDot11BlackListTimeTicks,'h3cDot11WIDSNotifyGroup':h3cDot11WIDSNotifyGroup,'h3cDot11WIDSTraps':h3cDot11WIDSTraps,'h3cDot11WIDSDetectRogueTrap':h3cDot11WIDSDetectRogueTrap,'h3cDot11WIDSAdHocTrap':h3cDot11WIDSAdHocTrap,'h3cDot11WIDSUnauthorSSIDTrap':h3cDot11WIDSUnauthorSSIDTrap,'h3cDot11WIDSDisappearRogueTrap':h3cDot11WIDSDisappearRogueTrap,'h3cDot11WIDSDetectAttack':h3cDot11WIDSDetectAttack,'h3cDot11WIDSDetectWBridge':h3cDot11WIDSDetectWBridge,'h3cDot11WIDSFloodTrap':h3cDot11WIDSFloodTrap,'h3cDot11WIDSSpoofTrap':h3cDot11WIDSSpoofTrap,'h3cDot11WIDSWeakIVTrap':h3cDot11WIDSWeakIVTrap,'h3cDot11WIDSTrapVarObjects':h3cDot11WIDSTrapVarObjects,_U:h3cDot11WIDSRogueMAC,_q:h3cDot11WIDSRogueType,_L:h3cDot11WIDSMonitorMAC,_r:h3cDot11WIDSAdHocMAC,_s:h3cDot11UnauthorSSIDName,_V:h3cDot11MonitorAPID,_W:h3cDot11MonitorApRadioID,_M:h3cDot11WIDSAtkMac,_X:h3cDot11WIDSAtkFrameType,_Y:h3cDot11WIDSAtkChannel,_Z:h3cDot11WIDSAtkTime,_a:h3cDot11WIDSAtkDestMac,_N:h3cDot11WIDSFirstTrapTime})