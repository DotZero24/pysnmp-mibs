_AV='ciscoAtmIfNotifyGroup'
_AU='ciscoAtmIfMIBGroup10'
_AT='ciscoAtmIfMIBGroup9'
_AS='ciscoAtmIfEvent'
_AR='ciscoAtmIfNotifsEnabled'
_AQ='ciscoAtmIfSvcUpcIntentUbr'
_AP='ciscoAtmIfSvcUpcIntentAbr'
_AO='ciscoAtmIfSvcUpcIntentVbrNrt'
_AN='ciscoAtmIfSvcUpcIntentVbrRt'
_AM='ciscoAtmIfSvcUpcIntentCbr'
_AL='ciscoAtmIfSscopUpDownChanges'
_AK='ciscoAtmIfIlmiUpDownChanges'
_AJ='ciscoAtmIfRxCellDiscards'
_AI='ciscoAtmIfRxCellUpcViolations'
_AH='ciscoAtmIfE164AutoConversionOnly'
_AG='ciscoAtmIfE164Address'
_AF='ciscoAtmIfDerivedAESA'
_AE='ciscoAtmIfConfigAESA'
_AD='ciscoAtmIfIlmiAccessFilter'
_AC='ciscoAtmIfIlmiAccessGlobalDefaultFilter'
_AB='ciscoAtmIfAddress'
_AA='ciscoAtmIfAddressType'
_A9='ciscoAtmIfSvcUpcIntent'
_A8='ciscoAtmIfSvcMinVci'
_A7='ciscoAtmIfEntry'
_A6='permitPrefixAndAllGroups'
_A5='permitPrefixAndWellknownGroups'
_A4='permitPrefix'
_A3='permitAll'
_A2='flashYellow'
_A1='flashGreen'
_A0='steadyRed'
_z='steadyYellow'
_y='notApplicable'
_x='dropping'
_w='tagging'
_v='passing'
_u='TruthValue'
_t='ciscoAtmIfMIBGroup8'
_s='ciscoAtmIfSscopFSMState'
_r='ciscoAtmIfIlmiFSMState'
_q='ciscoAtmIfSignallingAdminStatus'
_p='ciscoAtmIfWellKnownVcMode'
_o='ciscoAtmIfUniSignallingVersion'
_n='ciscoAtmIfCdLed'
_m='ciscoAtmIfSoftVcDestAddress'
_l='ciscoAtmIfIlmiKeepAlive'
_k='ciscoAtmIfIlmiAutoConfiguration'
_j='ciscoAtmIfIlmiAddressRegistration'
_i='ciscoAtmIfIlmiConfiguration'
_h='ciscoAtmIfRecvCells'
_g='ciscoAtmIfXmitCells'
_f='ciscoAtmIfRecvLed'
_e='ciscoAtmIfXmitLed'
_d='ciscoAtmIfPortType'
_c='ciscoAtmIfConfVplIf'
_b='ciscoAtmIfTotalConnections'
_a='ciscoAtmIfActiveSVCs'
_Z='ciscoAtmIfActiveSVPs'
_Y='ciscoAtmIfPVCs'
_X='ciscoAtmIfPVPs'
_W='ciscoAtmIfUniType'
_V='ciscoAtmIfSide'
_U='ciscoAtmIfType'
_T='steadyGreen'
_S='off'
_R='OctetString'
_Q='ciscoAtmIfMIBGroup7'
_P='ciscoAtmIfMIBGroup6'
_O='ciscoAtmIfMIBGroup3'
_N='disabled'
_M='enabled'
_L='ciscoAtmIfMIBGroup5'
_K='deprecated'
_J='ciscoAtmIfMIBGroup4'
_I='ciscoAtmIfMIBGroup2'
_H='UpcMethod'
_G='ciscoAtmIfMIBGroup'
_F='obsolete'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='CISCO-ATM-IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmInterfaceConfEntry,=mibBuilder.importSymbols('ATM-MIB','atmInterfaceConfEntry')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_u)
ciscoAtmIfMIB=ModuleIdentity((1,3,6,1,4,1,9,10,14))
if mibBuilder.loadTexts:ciscoAtmIfMIB.setRevisions(('2002-02-13 00:00','2001-08-08 00:00','2001-05-21 00:00','2000-04-11 00:00','1999-03-11 00:00','1997-11-30 00:00','1997-09-10 00:00','1996-11-01 00:00','1996-10-14 00:00'))
class NsapAtmAddr(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class AtmAddr(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(13,13),ValueSizeConstraint(20,20))
class UpcMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_CiscoAtmIfMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoAtmIfMIBNotifications=_CiscoAtmIfMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,14,0))
_CiscoAtmIfMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmIfMIBObjects=_CiscoAtmIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,14,1))
_CiscoAtmIfTable_Object=MibTable
ciscoAtmIfTable=_CiscoAtmIfTable_Object((1,3,6,1,4,1,9,10,14,1,1))
if mibBuilder.loadTexts:ciscoAtmIfTable.setStatus(_B)
_CiscoAtmIfEntry_Object=MibTableRow
ciscoAtmIfEntry=_CiscoAtmIfEntry_Object((1,3,6,1,4,1,9,10,14,1,1,1))
if mibBuilder.loadTexts:ciscoAtmIfEntry.setStatus(_B)
class _CiscoAtmIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('uni',2),('pnni',3),('iisp',4),('nniPvcOnly',5),('aini',6)))
_CiscoAtmIfType_Type.__name__=_C
_CiscoAtmIfType_Object=MibTableColumn
ciscoAtmIfType=_CiscoAtmIfType_Object((1,3,6,1,4,1,9,10,14,1,1,1,1),_CiscoAtmIfType_Type())
ciscoAtmIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfType.setStatus(_B)
class _CiscoAtmIfSide_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('user',1),('network',2),(_y,3)))
_CiscoAtmIfSide_Type.__name__=_C
_CiscoAtmIfSide_Object=MibTableColumn
ciscoAtmIfSide=_CiscoAtmIfSide_Object((1,3,6,1,4,1,9,10,14,1,1,1,2),_CiscoAtmIfSide_Type())
ciscoAtmIfSide.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSide.setStatus(_B)
class _CiscoAtmIfUniType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('public',1),('private',2)))
_CiscoAtmIfUniType_Type.__name__=_C
_CiscoAtmIfUniType_Object=MibTableColumn
ciscoAtmIfUniType=_CiscoAtmIfUniType_Object((1,3,6,1,4,1,9,10,14,1,1,1,3),_CiscoAtmIfUniType_Type())
ciscoAtmIfUniType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfUniType.setStatus(_B)
class _CiscoAtmIfPVPs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoAtmIfPVPs_Type.__name__=_C
_CiscoAtmIfPVPs_Object=MibTableColumn
ciscoAtmIfPVPs=_CiscoAtmIfPVPs_Object((1,3,6,1,4,1,9,10,14,1,1,1,4),_CiscoAtmIfPVPs_Type())
ciscoAtmIfPVPs.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPVPs.setStatus(_B)
class _CiscoAtmIfPVCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoAtmIfPVCs_Type.__name__=_C
_CiscoAtmIfPVCs_Object=MibTableColumn
ciscoAtmIfPVCs=_CiscoAtmIfPVCs_Object((1,3,6,1,4,1,9,10,14,1,1,1,5),_CiscoAtmIfPVCs_Type())
ciscoAtmIfPVCs.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPVCs.setStatus(_B)
_CiscoAtmIfActiveSVPs_Type=Gauge32
_CiscoAtmIfActiveSVPs_Object=MibTableColumn
ciscoAtmIfActiveSVPs=_CiscoAtmIfActiveSVPs_Object((1,3,6,1,4,1,9,10,14,1,1,1,6),_CiscoAtmIfActiveSVPs_Type())
ciscoAtmIfActiveSVPs.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfActiveSVPs.setStatus(_B)
_CiscoAtmIfActiveSVCs_Type=Gauge32
_CiscoAtmIfActiveSVCs_Object=MibTableColumn
ciscoAtmIfActiveSVCs=_CiscoAtmIfActiveSVCs_Object((1,3,6,1,4,1,9,10,14,1,1,1,7),_CiscoAtmIfActiveSVCs_Type())
ciscoAtmIfActiveSVCs.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfActiveSVCs.setStatus(_B)
_CiscoAtmIfTotalConnections_Type=Gauge32
_CiscoAtmIfTotalConnections_Object=MibTableColumn
ciscoAtmIfTotalConnections=_CiscoAtmIfTotalConnections_Object((1,3,6,1,4,1,9,10,14,1,1,1,8),_CiscoAtmIfTotalConnections_Type())
ciscoAtmIfTotalConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfTotalConnections.setStatus(_B)
class _CiscoAtmIfConfVplIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoAtmIfConfVplIf_Type.__name__=_C
_CiscoAtmIfConfVplIf_Object=MibTableColumn
ciscoAtmIfConfVplIf=_CiscoAtmIfConfVplIf_Object((1,3,6,1,4,1,9,10,14,1,1,1,9),_CiscoAtmIfConfVplIf_Type())
ciscoAtmIfConfVplIf.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfConfVplIf.setStatus(_B)
class _CiscoAtmIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('other',1),('cpu',2),('ethernet',3),('oc3Utp',4),('oc3SingleModeFiber',5),('oc3MultiModeFiber',6),('oc12SingleModeFiber',7),('ds3',8),('e3',9),('ds1',10),('e1',11),('oc3Utp3',12),('oc3Utp5',13),('oc3SmIr',14),('oc3SmIrPlus',15),('oc3SmLr',16),('oc3Pof',17),('oc12MultiModeFiber',18),('oc12SmIr',19),('oc12SmIrPlus',20),('oc12SmLr',21),('oc12Pof',22),('oc12SmLr2',23),('oc12SmLr3',24),('atm25',25)))
_CiscoAtmIfPortType_Type.__name__=_C
_CiscoAtmIfPortType_Object=MibTableColumn
ciscoAtmIfPortType=_CiscoAtmIfPortType_Object((1,3,6,1,4,1,9,10,14,1,1,1,10),_CiscoAtmIfPortType_Type())
ciscoAtmIfPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPortType.setStatus(_B)
class _CiscoAtmIfXmitLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,1),(_T,2),(_z,3),(_A0,4),(_A1,5),(_A2,6),('flashRed',7)))
_CiscoAtmIfXmitLed_Type.__name__=_C
_CiscoAtmIfXmitLed_Object=MibTableColumn
ciscoAtmIfXmitLed=_CiscoAtmIfXmitLed_Object((1,3,6,1,4,1,9,10,14,1,1,1,11),_CiscoAtmIfXmitLed_Type())
ciscoAtmIfXmitLed.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfXmitLed.setStatus(_B)
class _CiscoAtmIfRecvLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,1),(_T,2),(_z,3),(_A0,4),(_A1,5),(_A2,6),('flashRed',7)))
_CiscoAtmIfRecvLed_Type.__name__=_C
_CiscoAtmIfRecvLed_Object=MibTableColumn
ciscoAtmIfRecvLed=_CiscoAtmIfRecvLed_Object((1,3,6,1,4,1,9,10,14,1,1,1,12),_CiscoAtmIfRecvLed_Type())
ciscoAtmIfRecvLed.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfRecvLed.setStatus(_B)
_CiscoAtmIfXmitCells_Type=Counter32
_CiscoAtmIfXmitCells_Object=MibTableColumn
ciscoAtmIfXmitCells=_CiscoAtmIfXmitCells_Object((1,3,6,1,4,1,9,10,14,1,1,1,13),_CiscoAtmIfXmitCells_Type())
ciscoAtmIfXmitCells.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfXmitCells.setStatus(_B)
_CiscoAtmIfRecvCells_Type=Counter32
_CiscoAtmIfRecvCells_Object=MibTableColumn
ciscoAtmIfRecvCells=_CiscoAtmIfRecvCells_Object((1,3,6,1,4,1,9,10,14,1,1,1,14),_CiscoAtmIfRecvCells_Type())
ciscoAtmIfRecvCells.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfRecvCells.setStatus(_B)
class _CiscoAtmIfSvcMinVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiscoAtmIfSvcMinVci_Type.__name__=_C
_CiscoAtmIfSvcMinVci_Object=MibTableColumn
ciscoAtmIfSvcMinVci=_CiscoAtmIfSvcMinVci_Object((1,3,6,1,4,1,9,10,14,1,1,1,15),_CiscoAtmIfSvcMinVci_Type())
ciscoAtmIfSvcMinVci.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfSvcMinVci.setStatus(_K)
class _CiscoAtmIfIlmiConfiguration_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CiscoAtmIfIlmiConfiguration_Type.__name__=_C
_CiscoAtmIfIlmiConfiguration_Object=MibTableColumn
ciscoAtmIfIlmiConfiguration=_CiscoAtmIfIlmiConfiguration_Object((1,3,6,1,4,1,9,10,14,1,1,1,16),_CiscoAtmIfIlmiConfiguration_Type())
ciscoAtmIfIlmiConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiConfiguration.setStatus(_B)
class _CiscoAtmIfIlmiAddressRegistration_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CiscoAtmIfIlmiAddressRegistration_Type.__name__=_C
_CiscoAtmIfIlmiAddressRegistration_Object=MibTableColumn
ciscoAtmIfIlmiAddressRegistration=_CiscoAtmIfIlmiAddressRegistration_Object((1,3,6,1,4,1,9,10,14,1,1,1,17),_CiscoAtmIfIlmiAddressRegistration_Type())
ciscoAtmIfIlmiAddressRegistration.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiAddressRegistration.setStatus(_B)
class _CiscoAtmIfIlmiAutoConfiguration_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CiscoAtmIfIlmiAutoConfiguration_Type.__name__=_C
_CiscoAtmIfIlmiAutoConfiguration_Object=MibTableColumn
ciscoAtmIfIlmiAutoConfiguration=_CiscoAtmIfIlmiAutoConfiguration_Object((1,3,6,1,4,1,9,10,14,1,1,1,18),_CiscoAtmIfIlmiAutoConfiguration_Type())
ciscoAtmIfIlmiAutoConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiAutoConfiguration.setStatus(_B)
class _CiscoAtmIfIlmiKeepAlive_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoAtmIfIlmiKeepAlive_Type.__name__=_C
_CiscoAtmIfIlmiKeepAlive_Object=MibTableColumn
ciscoAtmIfIlmiKeepAlive=_CiscoAtmIfIlmiKeepAlive_Object((1,3,6,1,4,1,9,10,14,1,1,1,19),_CiscoAtmIfIlmiKeepAlive_Type())
ciscoAtmIfIlmiKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:ciscoAtmIfIlmiKeepAlive.setUnits('seconds')
_CiscoAtmIfSoftVcDestAddress_Type=NsapAtmAddr
_CiscoAtmIfSoftVcDestAddress_Object=MibTableColumn
ciscoAtmIfSoftVcDestAddress=_CiscoAtmIfSoftVcDestAddress_Object((1,3,6,1,4,1,9,10,14,1,1,1,20),_CiscoAtmIfSoftVcDestAddress_Type())
ciscoAtmIfSoftVcDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfSoftVcDestAddress.setStatus(_B)
class _CiscoAtmIfUniSignallingVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_y,1),('atmfUni3Dot0',2),('atmfUni3Dot1',3),('atmfUni4Dot0',4)))
_CiscoAtmIfUniSignallingVersion_Type.__name__=_C
_CiscoAtmIfUniSignallingVersion_Object=MibTableColumn
ciscoAtmIfUniSignallingVersion=_CiscoAtmIfUniSignallingVersion_Object((1,3,6,1,4,1,9,10,14,1,1,1,21),_CiscoAtmIfUniSignallingVersion_Type())
ciscoAtmIfUniSignallingVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfUniSignallingVersion.setStatus(_B)
class _CiscoAtmIfSvcUpcIntent_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_CiscoAtmIfSvcUpcIntent_Type.__name__=_C
_CiscoAtmIfSvcUpcIntent_Object=MibTableColumn
ciscoAtmIfSvcUpcIntent=_CiscoAtmIfSvcUpcIntent_Object((1,3,6,1,4,1,9,10,14,1,1,1,22),_CiscoAtmIfSvcUpcIntent_Type())
ciscoAtmIfSvcUpcIntent.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntent.setStatus(_K)
class _CiscoAtmIfAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nsap',1),('esi',2),('e164',3),('null',4)))
_CiscoAtmIfAddressType_Type.__name__=_C
_CiscoAtmIfAddressType_Object=MibTableColumn
ciscoAtmIfAddressType=_CiscoAtmIfAddressType_Object((1,3,6,1,4,1,9,10,14,1,1,1,23),_CiscoAtmIfAddressType_Type())
ciscoAtmIfAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfAddressType.setStatus(_F)
class _CiscoAtmIfAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6),ValueSizeConstraint(8,8),ValueSizeConstraint(20,20))
_CiscoAtmIfAddress_Type.__name__=_R
_CiscoAtmIfAddress_Object=MibTableColumn
ciscoAtmIfAddress=_CiscoAtmIfAddress_Object((1,3,6,1,4,1,9,10,14,1,1,1,24),_CiscoAtmIfAddress_Type())
ciscoAtmIfAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfAddress.setStatus(_F)
class _CiscoAtmIfWellKnownVcMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('automatic',1),('manual',2),('manualDeleteUponEntry',3)))
_CiscoAtmIfWellKnownVcMode_Type.__name__=_C
_CiscoAtmIfWellKnownVcMode_Object=MibTableColumn
ciscoAtmIfWellKnownVcMode=_CiscoAtmIfWellKnownVcMode_Object((1,3,6,1,4,1,9,10,14,1,1,1,31),_CiscoAtmIfWellKnownVcMode_Type())
ciscoAtmIfWellKnownVcMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfWellKnownVcMode.setStatus(_B)
class _CiscoAtmIfSignallingAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_CiscoAtmIfSignallingAdminStatus_Type.__name__=_C
_CiscoAtmIfSignallingAdminStatus_Object=MibTableColumn
ciscoAtmIfSignallingAdminStatus=_CiscoAtmIfSignallingAdminStatus_Object((1,3,6,1,4,1,9,10,14,1,1,1,32),_CiscoAtmIfSignallingAdminStatus_Type())
ciscoAtmIfSignallingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSignallingAdminStatus.setStatus(_B)
class _CiscoAtmIfCdLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_CiscoAtmIfCdLed_Type.__name__=_C
_CiscoAtmIfCdLed_Object=MibTableColumn
ciscoAtmIfCdLed=_CiscoAtmIfCdLed_Object((1,3,6,1,4,1,9,10,14,1,1,1,33),_CiscoAtmIfCdLed_Type())
ciscoAtmIfCdLed.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfCdLed.setStatus(_B)
class _CiscoAtmIfIlmiAccessFilter_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3),(_A6,4),('useGlobalDefaultFilter',5)))
_CiscoAtmIfIlmiAccessFilter_Type.__name__=_C
_CiscoAtmIfIlmiAccessFilter_Object=MibTableColumn
ciscoAtmIfIlmiAccessFilter=_CiscoAtmIfIlmiAccessFilter_Object((1,3,6,1,4,1,9,10,14,1,1,1,34),_CiscoAtmIfIlmiAccessFilter_Type())
ciscoAtmIfIlmiAccessFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiAccessFilter.setStatus(_B)
class _CiscoAtmIfConfigAESA_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(7,7),ValueSizeConstraint(20,20))
_CiscoAtmIfConfigAESA_Type.__name__=_R
_CiscoAtmIfConfigAESA_Object=MibTableColumn
ciscoAtmIfConfigAESA=_CiscoAtmIfConfigAESA_Object((1,3,6,1,4,1,9,10,14,1,1,1,35),_CiscoAtmIfConfigAESA_Type())
ciscoAtmIfConfigAESA.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfConfigAESA.setStatus(_B)
_CiscoAtmIfDerivedAESA_Type=AtmAddr
_CiscoAtmIfDerivedAESA_Object=MibTableColumn
ciscoAtmIfDerivedAESA=_CiscoAtmIfDerivedAESA_Object((1,3,6,1,4,1,9,10,14,1,1,1,36),_CiscoAtmIfDerivedAESA_Type())
ciscoAtmIfDerivedAESA.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfDerivedAESA.setStatus(_B)
_CiscoAtmIfE164Address_Type=AtmAddr
_CiscoAtmIfE164Address_Object=MibTableColumn
ciscoAtmIfE164Address=_CiscoAtmIfE164Address_Object((1,3,6,1,4,1,9,10,14,1,1,1,37),_CiscoAtmIfE164Address_Type())
ciscoAtmIfE164Address.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfE164Address.setStatus(_B)
_CiscoAtmIfE164AutoConversionOnly_Type=TruthValue
_CiscoAtmIfE164AutoConversionOnly_Object=MibTableColumn
ciscoAtmIfE164AutoConversionOnly=_CiscoAtmIfE164AutoConversionOnly_Object((1,3,6,1,4,1,9,10,14,1,1,1,38),_CiscoAtmIfE164AutoConversionOnly_Type())
ciscoAtmIfE164AutoConversionOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfE164AutoConversionOnly.setStatus(_B)
_CiscoAtmIfRxCellUpcViolations_Type=Counter32
_CiscoAtmIfRxCellUpcViolations_Object=MibTableColumn
ciscoAtmIfRxCellUpcViolations=_CiscoAtmIfRxCellUpcViolations_Object((1,3,6,1,4,1,9,10,14,1,1,1,39),_CiscoAtmIfRxCellUpcViolations_Type())
ciscoAtmIfRxCellUpcViolations.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfRxCellUpcViolations.setStatus(_B)
_CiscoAtmIfRxCellDiscards_Type=Counter32
_CiscoAtmIfRxCellDiscards_Object=MibTableColumn
ciscoAtmIfRxCellDiscards=_CiscoAtmIfRxCellDiscards_Object((1,3,6,1,4,1,9,10,14,1,1,1,40),_CiscoAtmIfRxCellDiscards_Type())
ciscoAtmIfRxCellDiscards.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfRxCellDiscards.setStatus(_B)
class _CiscoAtmIfIlmiFSMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('down',1),('restarting',2),('waitDevType',3),('deviceAndPortTypeComplete',4),('awaitPnniConfig',5),('pnniConfigComplete',6),('awaitRestartAck',7),('upAndNormal',8)))
_CiscoAtmIfIlmiFSMState_Type.__name__=_C
_CiscoAtmIfIlmiFSMState_Object=MibTableColumn
ciscoAtmIfIlmiFSMState=_CiscoAtmIfIlmiFSMState_Object((1,3,6,1,4,1,9,10,14,1,1,1,41),_CiscoAtmIfIlmiFSMState_Type())
ciscoAtmIfIlmiFSMState.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfIlmiFSMState.setStatus(_B)
_CiscoAtmIfIlmiUpDownChanges_Type=Counter32
_CiscoAtmIfIlmiUpDownChanges_Object=MibTableColumn
ciscoAtmIfIlmiUpDownChanges=_CiscoAtmIfIlmiUpDownChanges_Object((1,3,6,1,4,1,9,10,14,1,1,1,42),_CiscoAtmIfIlmiUpDownChanges_Type())
ciscoAtmIfIlmiUpDownChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfIlmiUpDownChanges.setStatus(_B)
class _CiscoAtmIfSscopFSMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('idle',1),('outgoingConnectionPending',2),('incomingConnectionPending',3),('dataTransferReady',4),('outgoingDisconnectionPending',5),('outgoingResyncPending',6),('incomingResyncPending',7),('outgoingRecoveryPending',8),('incomingRecoveryPending',9),('concurrentResyncPending',10)))
_CiscoAtmIfSscopFSMState_Type.__name__=_C
_CiscoAtmIfSscopFSMState_Object=MibTableColumn
ciscoAtmIfSscopFSMState=_CiscoAtmIfSscopFSMState_Object((1,3,6,1,4,1,9,10,14,1,1,1,43),_CiscoAtmIfSscopFSMState_Type())
ciscoAtmIfSscopFSMState.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfSscopFSMState.setStatus(_B)
_CiscoAtmIfSscopUpDownChanges_Type=Counter32
_CiscoAtmIfSscopUpDownChanges_Object=MibTableColumn
ciscoAtmIfSscopUpDownChanges=_CiscoAtmIfSscopUpDownChanges_Object((1,3,6,1,4,1,9,10,14,1,1,1,44),_CiscoAtmIfSscopUpDownChanges_Type())
ciscoAtmIfSscopUpDownChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfSscopUpDownChanges.setStatus(_B)
class _CiscoAtmIfSvcUpcIntentCbr_Type(UpcMethod):defaultValue=1
_CiscoAtmIfSvcUpcIntentCbr_Type.__name__=_H
_CiscoAtmIfSvcUpcIntentCbr_Object=MibTableColumn
ciscoAtmIfSvcUpcIntentCbr=_CiscoAtmIfSvcUpcIntentCbr_Object((1,3,6,1,4,1,9,10,14,1,1,1,45),_CiscoAtmIfSvcUpcIntentCbr_Type())
ciscoAtmIfSvcUpcIntentCbr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntentCbr.setStatus(_B)
class _CiscoAtmIfSvcUpcIntentVbrRt_Type(UpcMethod):defaultValue=1
_CiscoAtmIfSvcUpcIntentVbrRt_Type.__name__=_H
_CiscoAtmIfSvcUpcIntentVbrRt_Object=MibTableColumn
ciscoAtmIfSvcUpcIntentVbrRt=_CiscoAtmIfSvcUpcIntentVbrRt_Object((1,3,6,1,4,1,9,10,14,1,1,1,46),_CiscoAtmIfSvcUpcIntentVbrRt_Type())
ciscoAtmIfSvcUpcIntentVbrRt.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntentVbrRt.setStatus(_B)
class _CiscoAtmIfSvcUpcIntentVbrNrt_Type(UpcMethod):defaultValue=1
_CiscoAtmIfSvcUpcIntentVbrNrt_Type.__name__=_H
_CiscoAtmIfSvcUpcIntentVbrNrt_Object=MibTableColumn
ciscoAtmIfSvcUpcIntentVbrNrt=_CiscoAtmIfSvcUpcIntentVbrNrt_Object((1,3,6,1,4,1,9,10,14,1,1,1,47),_CiscoAtmIfSvcUpcIntentVbrNrt_Type())
ciscoAtmIfSvcUpcIntentVbrNrt.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntentVbrNrt.setStatus(_B)
class _CiscoAtmIfSvcUpcIntentAbr_Type(UpcMethod):defaultValue=1
_CiscoAtmIfSvcUpcIntentAbr_Type.__name__=_H
_CiscoAtmIfSvcUpcIntentAbr_Object=MibTableColumn
ciscoAtmIfSvcUpcIntentAbr=_CiscoAtmIfSvcUpcIntentAbr_Object((1,3,6,1,4,1,9,10,14,1,1,1,48),_CiscoAtmIfSvcUpcIntentAbr_Type())
ciscoAtmIfSvcUpcIntentAbr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntentAbr.setStatus(_B)
class _CiscoAtmIfSvcUpcIntentUbr_Type(UpcMethod):defaultValue=1
_CiscoAtmIfSvcUpcIntentUbr_Type.__name__=_H
_CiscoAtmIfSvcUpcIntentUbr_Object=MibTableColumn
ciscoAtmIfSvcUpcIntentUbr=_CiscoAtmIfSvcUpcIntentUbr_Object((1,3,6,1,4,1,9,10,14,1,1,1,49),_CiscoAtmIfSvcUpcIntentUbr_Type())
ciscoAtmIfSvcUpcIntentUbr.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfSvcUpcIntentUbr.setStatus(_B)
class _CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A3,1),(_A4,2),(_A5,3),(_A6,4)))
_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type.__name__=_C
_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Object=MibScalar
ciscoAtmIfIlmiAccessGlobalDefaultFilter=_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Object((1,3,6,1,4,1,9,10,14,1,2),_CiscoAtmIfIlmiAccessGlobalDefaultFilter_Type())
ciscoAtmIfIlmiAccessGlobalDefaultFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfIlmiAccessGlobalDefaultFilter.setStatus(_B)
class _CiscoAtmIfNotifsEnabled_Type(TruthValue):defaultValue=2
_CiscoAtmIfNotifsEnabled_Type.__name__=_u
_CiscoAtmIfNotifsEnabled_Object=MibScalar
ciscoAtmIfNotifsEnabled=_CiscoAtmIfNotifsEnabled_Object((1,3,6,1,4,1,9,10,14,1,3),_CiscoAtmIfNotifsEnabled_Type())
ciscoAtmIfNotifsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoAtmIfNotifsEnabled.setStatus(_B)
_CiscoAtmIfMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmIfMIBConformance=_CiscoAtmIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,14,3))
_CiscoAtmIfMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmIfMIBCompliances=_CiscoAtmIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,14,3,1))
_CiscoAtmIfMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmIfMIBGroups=_CiscoAtmIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,14,3,2))
atmInterfaceConfEntry.registerAugmentions((_A,_A7))
ciscoAtmIfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
ciscoAtmIfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,1))
ciscoAtmIfMIBGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_A8),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup.setStatus(_K)
ciscoAtmIfMIBGroup2=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,2))
ciscoAtmIfMIBGroup2.setObjects(*((_A,_o),(_A,_A9)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup2.setStatus(_K)
ciscoAtmIfMIBGroup3=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,3))
ciscoAtmIfMIBGroup3.setObjects(*((_A,_AA),(_A,_AB),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup3.setStatus(_F)
ciscoAtmIfMIBGroup4=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,4))
ciscoAtmIfMIBGroup4.setObjects(*((_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup4.setStatus(_B)
ciscoAtmIfMIBGroup5=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,5))
ciscoAtmIfMIBGroup5.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup5.setStatus(_B)
ciscoAtmIfMIBGroup6=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,6))
ciscoAtmIfMIBGroup6.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup6.setStatus(_B)
ciscoAtmIfMIBGroup7=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,7))
ciscoAtmIfMIBGroup7.setObjects(*((_A,_AI),(_A,_AJ),(_A,_r),(_A,_AK),(_A,_s),(_A,_AL)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup7.setStatus(_B)
ciscoAtmIfMIBGroup8=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,8))
ciscoAtmIfMIBGroup8.setObjects(*((_A,_o),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup8.setStatus(_B)
ciscoAtmIfMIBGroup9=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,9))
ciscoAtmIfMIBGroup9.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup9.setStatus(_B)
ciscoAtmIfMIBGroup10=ObjectGroup((1,3,6,1,4,1,9,10,14,3,2,10))
ciscoAtmIfMIBGroup10.setObjects((_A,_AR))
if mibBuilder.loadTexts:ciscoAtmIfMIBGroup10.setStatus(_B)
ciscoAtmIfEvent=NotificationType((1,3,6,1,4,1,9,10,14,0,1))
ciscoAtmIfEvent.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ciscoAtmIfEvent.setStatus(_B)
ciscoAtmIfNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,10,14,3,2,11))
ciscoAtmIfNotifyGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:ciscoAtmIfNotifyGroup.setStatus(_B)
ciscoAtmIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,1))
ciscoAtmIfMIBCompliance.setObjects((_A,_G))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance.setStatus(_F)
ciscoAtmIfMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,2))
ciscoAtmIfMIBCompliance2.setObjects(*((_A,_G),(_A,_I)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance2.setStatus(_F)
ciscoAtmIfMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,3))
ciscoAtmIfMIBCompliance3.setObjects(*((_A,_G),(_A,_I),(_A,_O)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance3.setStatus(_F)
ciscoAtmIfMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,4))
ciscoAtmIfMIBCompliance4.setObjects(*((_A,_G),(_A,_I),(_A,_O),(_A,_J)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance4.setStatus(_F)
ciscoAtmIfMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,5))
ciscoAtmIfMIBCompliance5.setObjects(*((_A,_G),(_A,_I),(_A,_O),(_A,_J),(_A,_L)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance5.setStatus(_F)
ciscoAtmIfMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,6))
ciscoAtmIfMIBCompliance6.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_L),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance6.setStatus(_F)
ciscoAtmIfMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,7))
ciscoAtmIfMIBCompliance7.setObjects(*((_A,_G),(_A,_J),(_A,_L),(_A,_P),(_A,_Q),(_A,_t)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance7.setStatus(_K)
ciscoAtmIfMIBCompliance8=ModuleCompliance((1,3,6,1,4,1,9,10,14,3,1,8))
ciscoAtmIfMIBCompliance8.setObjects(*((_A,_J),(_A,_L),(_A,_P),(_A,_Q),(_A,_t),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:ciscoAtmIfMIBCompliance8.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NsapAtmAddr':NsapAtmAddr,'AtmAddr':AtmAddr,_H:UpcMethod,'ciscoAtmIfMIB':ciscoAtmIfMIB,'ciscoAtmIfMIBNotifications':ciscoAtmIfMIBNotifications,_AS:ciscoAtmIfEvent,'ciscoAtmIfMIBObjects':ciscoAtmIfMIBObjects,'ciscoAtmIfTable':ciscoAtmIfTable,_A7:ciscoAtmIfEntry,_U:ciscoAtmIfType,_V:ciscoAtmIfSide,_W:ciscoAtmIfUniType,_X:ciscoAtmIfPVPs,_Y:ciscoAtmIfPVCs,_Z:ciscoAtmIfActiveSVPs,_a:ciscoAtmIfActiveSVCs,_b:ciscoAtmIfTotalConnections,_c:ciscoAtmIfConfVplIf,_d:ciscoAtmIfPortType,_e:ciscoAtmIfXmitLed,_f:ciscoAtmIfRecvLed,_g:ciscoAtmIfXmitCells,_h:ciscoAtmIfRecvCells,_A8:ciscoAtmIfSvcMinVci,_i:ciscoAtmIfIlmiConfiguration,_j:ciscoAtmIfIlmiAddressRegistration,_k:ciscoAtmIfIlmiAutoConfiguration,_l:ciscoAtmIfIlmiKeepAlive,_m:ciscoAtmIfSoftVcDestAddress,_o:ciscoAtmIfUniSignallingVersion,_A9:ciscoAtmIfSvcUpcIntent,_AA:ciscoAtmIfAddressType,_AB:ciscoAtmIfAddress,_p:ciscoAtmIfWellKnownVcMode,_q:ciscoAtmIfSignallingAdminStatus,_n:ciscoAtmIfCdLed,_AD:ciscoAtmIfIlmiAccessFilter,_AE:ciscoAtmIfConfigAESA,_AF:ciscoAtmIfDerivedAESA,_AG:ciscoAtmIfE164Address,_AH:ciscoAtmIfE164AutoConversionOnly,_AI:ciscoAtmIfRxCellUpcViolations,_AJ:ciscoAtmIfRxCellDiscards,_r:ciscoAtmIfIlmiFSMState,_AK:ciscoAtmIfIlmiUpDownChanges,_s:ciscoAtmIfSscopFSMState,_AL:ciscoAtmIfSscopUpDownChanges,_AM:ciscoAtmIfSvcUpcIntentCbr,_AN:ciscoAtmIfSvcUpcIntentVbrRt,_AO:ciscoAtmIfSvcUpcIntentVbrNrt,_AP:ciscoAtmIfSvcUpcIntentAbr,_AQ:ciscoAtmIfSvcUpcIntentUbr,_AC:ciscoAtmIfIlmiAccessGlobalDefaultFilter,_AR:ciscoAtmIfNotifsEnabled,'ciscoAtmIfMIBConformance':ciscoAtmIfMIBConformance,'ciscoAtmIfMIBCompliances':ciscoAtmIfMIBCompliances,'ciscoAtmIfMIBCompliance':ciscoAtmIfMIBCompliance,'ciscoAtmIfMIBCompliance2':ciscoAtmIfMIBCompliance2,'ciscoAtmIfMIBCompliance3':ciscoAtmIfMIBCompliance3,'ciscoAtmIfMIBCompliance4':ciscoAtmIfMIBCompliance4,'ciscoAtmIfMIBCompliance5':ciscoAtmIfMIBCompliance5,'ciscoAtmIfMIBCompliance6':ciscoAtmIfMIBCompliance6,'ciscoAtmIfMIBCompliance7':ciscoAtmIfMIBCompliance7,'ciscoAtmIfMIBCompliance8':ciscoAtmIfMIBCompliance8,'ciscoAtmIfMIBGroups':ciscoAtmIfMIBGroups,_G:ciscoAtmIfMIBGroup,_I:ciscoAtmIfMIBGroup2,_O:ciscoAtmIfMIBGroup3,_J:ciscoAtmIfMIBGroup4,_L:ciscoAtmIfMIBGroup5,_P:ciscoAtmIfMIBGroup6,_Q:ciscoAtmIfMIBGroup7,_t:ciscoAtmIfMIBGroup8,_AT:ciscoAtmIfMIBGroup9,_AU:ciscoAtmIfMIBGroup10,_AV:ciscoAtmIfNotifyGroup})