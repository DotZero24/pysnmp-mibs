_c='fsEcfmTrapType'
_b='fsEcfmLtmSeqNumber'
_a='fsEcfmRMepIdentifier'
_Z='fsEcfmMipCcmSrcAddr'
_Y='fsEcfmMipCcmFid'
_X='fsEcfmPortIndex'
_W='trapRemoteCCM'
_V='trapRDICCM'
_U='RowStatus'
_T='LldpChassisIdSubtype'
_S='Dot1agCfmPortStatus'
_R='Dot1agCfmInterfaceStatus'
_Q='fsEcfmMipVid'
_P='fsEcfmMipMdLevel'
_O='fsEcfmMipIfIndex'
_N='fsEcfmMepIdentifier'
_M='TruthValue'
_L='fsEcfmMaIndex'
_K='read-only'
_J='fsEcfmMdIndex'
_I='disabled'
_H='enabled'
_G='read-create'
_F='not-accessible'
_E='Unsigned32'
_D='Integer32'
_C='ARICENT-ECFM-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmInterfaceStatus,Dot1agCfmPortStatus=mibBuilder.importSymbols('IEEE8021-CFM-MIB',_R,_S)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
LldpChassisId,LldpChassisIdSubtype=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId',_T)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TAddress,TDomain,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress',_U,'TAddress','TDomain','TextualConvention',_M)
fsecfm=ModuleIdentity((1,3,6,1,4,1,2076,150))
if mibBuilder.loadTexts:fsecfm.setRevisions(('2012-09-05 00:00',))
class FsEcfmOuiType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class FsEcfmSetTraps(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('trapUnUsedbit',0),(_V,1),('trapMACstatus',2),(_W,3),('trapErrorCCM',4),('trapXconCCM',5)))
_FsEcfmSystem_ObjectIdentity=ObjectIdentity
fsEcfmSystem=_FsEcfmSystem_ObjectIdentity((1,3,6,1,4,1,2076,150,1))
class _FsEcfmSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsEcfmSystemControl_Type.__name__=_D
_FsEcfmSystemControl_Object=MibScalar
fsEcfmSystemControl=_FsEcfmSystemControl_Object((1,3,6,1,4,1,2076,150,1,1),_FsEcfmSystemControl_Type())
fsEcfmSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmSystemControl.setStatus(_A)
class _FsEcfmModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmModuleStatus_Type.__name__=_D
_FsEcfmModuleStatus_Object=MibScalar
fsEcfmModuleStatus=_FsEcfmModuleStatus_Object((1,3,6,1,4,1,2076,150,1,2),_FsEcfmModuleStatus_Type())
fsEcfmModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmModuleStatus.setStatus(_A)
_FsEcfmOui_Type=FsEcfmOuiType
_FsEcfmOui_Object=MibScalar
fsEcfmOui=_FsEcfmOui_Object((1,3,6,1,4,1,2076,150,1,3),_FsEcfmOui_Type())
fsEcfmOui.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmOui.setStatus(_A)
class _FsEcfmTraceOption_Type(Integer32):defaultValue=262144
_FsEcfmTraceOption_Type.__name__=_D
_FsEcfmTraceOption_Object=MibScalar
fsEcfmTraceOption=_FsEcfmTraceOption_Object((1,3,6,1,4,1,2076,150,1,4),_FsEcfmTraceOption_Type())
fsEcfmTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmTraceOption.setStatus(_A)
class _FsEcfmLtrCacheStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmLtrCacheStatus_Type.__name__=_D
_FsEcfmLtrCacheStatus_Object=MibScalar
fsEcfmLtrCacheStatus=_FsEcfmLtrCacheStatus_Object((1,3,6,1,4,1,2076,150,1,5),_FsEcfmLtrCacheStatus_Type())
fsEcfmLtrCacheStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmLtrCacheStatus.setStatus(_A)
class _FsEcfmLtrCacheClear_Type(TruthValue):defaultValue=2
_FsEcfmLtrCacheClear_Type.__name__=_M
_FsEcfmLtrCacheClear_Object=MibScalar
fsEcfmLtrCacheClear=_FsEcfmLtrCacheClear_Object((1,3,6,1,4,1,2076,150,1,6),_FsEcfmLtrCacheClear_Type())
fsEcfmLtrCacheClear.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmLtrCacheClear.setStatus(_A)
class _FsEcfmLtrCacheHoldTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10080))
_FsEcfmLtrCacheHoldTime_Type.__name__=_D
_FsEcfmLtrCacheHoldTime_Object=MibScalar
fsEcfmLtrCacheHoldTime=_FsEcfmLtrCacheHoldTime_Object((1,3,6,1,4,1,2076,150,1,7),_FsEcfmLtrCacheHoldTime_Type())
fsEcfmLtrCacheHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmLtrCacheHoldTime.setStatus(_A)
class _FsEcfmLtrCacheSize_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FsEcfmLtrCacheSize_Type.__name__=_D
_FsEcfmLtrCacheSize_Object=MibScalar
fsEcfmLtrCacheSize=_FsEcfmLtrCacheSize_Object((1,3,6,1,4,1,2076,150,1,8),_FsEcfmLtrCacheSize_Type())
fsEcfmLtrCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmLtrCacheSize.setStatus(_A)
_FsEcfmPortTable_Object=MibTable
fsEcfmPortTable=_FsEcfmPortTable_Object((1,3,6,1,4,1,2076,150,1,9))
if mibBuilder.loadTexts:fsEcfmPortTable.setStatus(_A)
_FsEcfmPortEntry_Object=MibTableRow
fsEcfmPortEntry=_FsEcfmPortEntry_Object((1,3,6,1,4,1,2076,150,1,9,1))
fsEcfmPortEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:fsEcfmPortEntry.setStatus(_A)
class _FsEcfmPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsEcfmPortIndex_Type.__name__=_E
_FsEcfmPortIndex_Object=MibTableColumn
fsEcfmPortIndex=_FsEcfmPortIndex_Object((1,3,6,1,4,1,2076,150,1,9,1,1),_FsEcfmPortIndex_Type())
fsEcfmPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmPortIndex.setStatus(_A)
class _FsEcfmPortLLCEncapStatus_Type(TruthValue):defaultValue=2
_FsEcfmPortLLCEncapStatus_Type.__name__=_M
_FsEcfmPortLLCEncapStatus_Object=MibTableColumn
fsEcfmPortLLCEncapStatus=_FsEcfmPortLLCEncapStatus_Object((1,3,6,1,4,1,2076,150,1,9,1,2),_FsEcfmPortLLCEncapStatus_Type())
fsEcfmPortLLCEncapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortLLCEncapStatus.setStatus(_A)
class _FsEcfmPortModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmPortModuleStatus_Type.__name__=_D
_FsEcfmPortModuleStatus_Object=MibTableColumn
fsEcfmPortModuleStatus=_FsEcfmPortModuleStatus_Object((1,3,6,1,4,1,2076,150,1,9,1,3),_FsEcfmPortModuleStatus_Type())
fsEcfmPortModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortModuleStatus.setStatus(_A)
_FsEcfmPortTxCfmPduCount_Type=Unsigned32
_FsEcfmPortTxCfmPduCount_Object=MibTableColumn
fsEcfmPortTxCfmPduCount=_FsEcfmPortTxCfmPduCount_Object((1,3,6,1,4,1,2076,150,1,9,1,4),_FsEcfmPortTxCfmPduCount_Type())
fsEcfmPortTxCfmPduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxCfmPduCount.setStatus(_A)
_FsEcfmPortTxCcmCount_Type=Unsigned32
_FsEcfmPortTxCcmCount_Object=MibTableColumn
fsEcfmPortTxCcmCount=_FsEcfmPortTxCcmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,5),_FsEcfmPortTxCcmCount_Type())
fsEcfmPortTxCcmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxCcmCount.setStatus(_A)
_FsEcfmPortTxLbmCount_Type=Unsigned32
_FsEcfmPortTxLbmCount_Object=MibTableColumn
fsEcfmPortTxLbmCount=_FsEcfmPortTxLbmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,6),_FsEcfmPortTxLbmCount_Type())
fsEcfmPortTxLbmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxLbmCount.setStatus(_A)
_FsEcfmPortTxLbrCount_Type=Unsigned32
_FsEcfmPortTxLbrCount_Object=MibTableColumn
fsEcfmPortTxLbrCount=_FsEcfmPortTxLbrCount_Object((1,3,6,1,4,1,2076,150,1,9,1,7),_FsEcfmPortTxLbrCount_Type())
fsEcfmPortTxLbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxLbrCount.setStatus(_A)
_FsEcfmPortTxLtmCount_Type=Unsigned32
_FsEcfmPortTxLtmCount_Object=MibTableColumn
fsEcfmPortTxLtmCount=_FsEcfmPortTxLtmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,8),_FsEcfmPortTxLtmCount_Type())
fsEcfmPortTxLtmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxLtmCount.setStatus(_A)
_FsEcfmPortTxLtrCount_Type=Unsigned32
_FsEcfmPortTxLtrCount_Object=MibTableColumn
fsEcfmPortTxLtrCount=_FsEcfmPortTxLtrCount_Object((1,3,6,1,4,1,2076,150,1,9,1,9),_FsEcfmPortTxLtrCount_Type())
fsEcfmPortTxLtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxLtrCount.setStatus(_A)
_FsEcfmPortTxFailedCount_Type=Unsigned32
_FsEcfmPortTxFailedCount_Object=MibTableColumn
fsEcfmPortTxFailedCount=_FsEcfmPortTxFailedCount_Object((1,3,6,1,4,1,2076,150,1,9,1,10),_FsEcfmPortTxFailedCount_Type())
fsEcfmPortTxFailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortTxFailedCount.setStatus(_A)
_FsEcfmPortRxCfmPduCount_Type=Unsigned32
_FsEcfmPortRxCfmPduCount_Object=MibTableColumn
fsEcfmPortRxCfmPduCount=_FsEcfmPortRxCfmPduCount_Object((1,3,6,1,4,1,2076,150,1,9,1,11),_FsEcfmPortRxCfmPduCount_Type())
fsEcfmPortRxCfmPduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxCfmPduCount.setStatus(_A)
_FsEcfmPortRxCcmCount_Type=Unsigned32
_FsEcfmPortRxCcmCount_Object=MibTableColumn
fsEcfmPortRxCcmCount=_FsEcfmPortRxCcmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,12),_FsEcfmPortRxCcmCount_Type())
fsEcfmPortRxCcmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxCcmCount.setStatus(_A)
_FsEcfmPortRxLbmCount_Type=Unsigned32
_FsEcfmPortRxLbmCount_Object=MibTableColumn
fsEcfmPortRxLbmCount=_FsEcfmPortRxLbmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,13),_FsEcfmPortRxLbmCount_Type())
fsEcfmPortRxLbmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxLbmCount.setStatus(_A)
_FsEcfmPortRxLbrCount_Type=Unsigned32
_FsEcfmPortRxLbrCount_Object=MibTableColumn
fsEcfmPortRxLbrCount=_FsEcfmPortRxLbrCount_Object((1,3,6,1,4,1,2076,150,1,9,1,14),_FsEcfmPortRxLbrCount_Type())
fsEcfmPortRxLbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxLbrCount.setStatus(_A)
_FsEcfmPortRxLtmCount_Type=Unsigned32
_FsEcfmPortRxLtmCount_Object=MibTableColumn
fsEcfmPortRxLtmCount=_FsEcfmPortRxLtmCount_Object((1,3,6,1,4,1,2076,150,1,9,1,15),_FsEcfmPortRxLtmCount_Type())
fsEcfmPortRxLtmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxLtmCount.setStatus(_A)
_FsEcfmPortRxLtrCount_Type=Unsigned32
_FsEcfmPortRxLtrCount_Object=MibTableColumn
fsEcfmPortRxLtrCount=_FsEcfmPortRxLtrCount_Object((1,3,6,1,4,1,2076,150,1,9,1,16),_FsEcfmPortRxLtrCount_Type())
fsEcfmPortRxLtrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxLtrCount.setStatus(_A)
_FsEcfmPortRxBadCfmPduCount_Type=Unsigned32
_FsEcfmPortRxBadCfmPduCount_Object=MibTableColumn
fsEcfmPortRxBadCfmPduCount=_FsEcfmPortRxBadCfmPduCount_Object((1,3,6,1,4,1,2076,150,1,9,1,17),_FsEcfmPortRxBadCfmPduCount_Type())
fsEcfmPortRxBadCfmPduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortRxBadCfmPduCount.setStatus(_A)
_FsEcfmPortFrwdCfmPduCount_Type=Unsigned32
_FsEcfmPortFrwdCfmPduCount_Object=MibTableColumn
fsEcfmPortFrwdCfmPduCount=_FsEcfmPortFrwdCfmPduCount_Object((1,3,6,1,4,1,2076,150,1,9,1,18),_FsEcfmPortFrwdCfmPduCount_Type())
fsEcfmPortFrwdCfmPduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortFrwdCfmPduCount.setStatus(_A)
_FsEcfmPortDsrdCfmPduCount_Type=Unsigned32
_FsEcfmPortDsrdCfmPduCount_Object=MibTableColumn
fsEcfmPortDsrdCfmPduCount=_FsEcfmPortDsrdCfmPduCount_Object((1,3,6,1,4,1,2076,150,1,9,1,19),_FsEcfmPortDsrdCfmPduCount_Type())
fsEcfmPortDsrdCfmPduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmPortDsrdCfmPduCount.setStatus(_A)
class _FsEcfmMipCcmDbStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmMipCcmDbStatus_Type.__name__=_D
_FsEcfmMipCcmDbStatus_Object=MibScalar
fsEcfmMipCcmDbStatus=_FsEcfmMipCcmDbStatus_Object((1,3,6,1,4,1,2076,150,1,10),_FsEcfmMipCcmDbStatus_Type())
fsEcfmMipCcmDbStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMipCcmDbStatus.setStatus(_A)
class _FsEcfmMipCcmDbClear_Type(TruthValue):defaultValue=2
_FsEcfmMipCcmDbClear_Type.__name__=_M
_FsEcfmMipCcmDbClear_Object=MibScalar
fsEcfmMipCcmDbClear=_FsEcfmMipCcmDbClear_Object((1,3,6,1,4,1,2076,150,1,11),_FsEcfmMipCcmDbClear_Type())
fsEcfmMipCcmDbClear.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMipCcmDbClear.setStatus(_A)
class _FsEcfmMipCcmDbSize_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_FsEcfmMipCcmDbSize_Type.__name__=_D
_FsEcfmMipCcmDbSize_Object=MibScalar
fsEcfmMipCcmDbSize=_FsEcfmMipCcmDbSize_Object((1,3,6,1,4,1,2076,150,1,12),_FsEcfmMipCcmDbSize_Type())
fsEcfmMipCcmDbSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMipCcmDbSize.setStatus(_A)
class _FsEcfmMipCcmDbHoldTime_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(24,48))
_FsEcfmMipCcmDbHoldTime_Type.__name__=_D
_FsEcfmMipCcmDbHoldTime_Object=MibScalar
fsEcfmMipCcmDbHoldTime=_FsEcfmMipCcmDbHoldTime_Object((1,3,6,1,4,1,2076,150,1,13),_FsEcfmMipCcmDbHoldTime_Type())
fsEcfmMipCcmDbHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMipCcmDbHoldTime.setStatus(_A)
_FsEcfmMemoryFailureCount_Type=Unsigned32
_FsEcfmMemoryFailureCount_Object=MibScalar
fsEcfmMemoryFailureCount=_FsEcfmMemoryFailureCount_Object((1,3,6,1,4,1,2076,150,1,14),_FsEcfmMemoryFailureCount_Type())
fsEcfmMemoryFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMemoryFailureCount.setStatus(_A)
_FsEcfmBufferFailureCount_Type=Unsigned32
_FsEcfmBufferFailureCount_Object=MibScalar
fsEcfmBufferFailureCount=_FsEcfmBufferFailureCount_Object((1,3,6,1,4,1,2076,150,1,15),_FsEcfmBufferFailureCount_Type())
fsEcfmBufferFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmBufferFailureCount.setStatus(_A)
_FsEcfmUpCount_Type=Unsigned32
_FsEcfmUpCount_Object=MibScalar
fsEcfmUpCount=_FsEcfmUpCount_Object((1,3,6,1,4,1,2076,150,1,16),_FsEcfmUpCount_Type())
fsEcfmUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmUpCount.setStatus(_A)
_FsEcfmDownCount_Type=Unsigned32
_FsEcfmDownCount_Object=MibScalar
fsEcfmDownCount=_FsEcfmDownCount_Object((1,3,6,1,4,1,2076,150,1,17),_FsEcfmDownCount_Type())
fsEcfmDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmDownCount.setStatus(_A)
_FsEcfmNoDftCount_Type=Unsigned32
_FsEcfmNoDftCount_Object=MibScalar
fsEcfmNoDftCount=_FsEcfmNoDftCount_Object((1,3,6,1,4,1,2076,150,1,18),_FsEcfmNoDftCount_Type())
fsEcfmNoDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmNoDftCount.setStatus(_A)
_FsEcfmRdiDftCount_Type=Unsigned32
_FsEcfmRdiDftCount_Object=MibScalar
fsEcfmRdiDftCount=_FsEcfmRdiDftCount_Object((1,3,6,1,4,1,2076,150,1,19),_FsEcfmRdiDftCount_Type())
fsEcfmRdiDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRdiDftCount.setStatus(_A)
_FsEcfmMacStatusDftCount_Type=Unsigned32
_FsEcfmMacStatusDftCount_Object=MibScalar
fsEcfmMacStatusDftCount=_FsEcfmMacStatusDftCount_Object((1,3,6,1,4,1,2076,150,1,20),_FsEcfmMacStatusDftCount_Type())
fsEcfmMacStatusDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMacStatusDftCount.setStatus(_A)
_FsEcfmRemoteCcmDftCount_Type=Unsigned32
_FsEcfmRemoteCcmDftCount_Object=MibScalar
fsEcfmRemoteCcmDftCount=_FsEcfmRemoteCcmDftCount_Object((1,3,6,1,4,1,2076,150,1,21),_FsEcfmRemoteCcmDftCount_Type())
fsEcfmRemoteCcmDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRemoteCcmDftCount.setStatus(_A)
_FsEcfmErrorCcmDftCount_Type=Unsigned32
_FsEcfmErrorCcmDftCount_Object=MibScalar
fsEcfmErrorCcmDftCount=_FsEcfmErrorCcmDftCount_Object((1,3,6,1,4,1,2076,150,1,22),_FsEcfmErrorCcmDftCount_Type())
fsEcfmErrorCcmDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmErrorCcmDftCount.setStatus(_A)
_FsEcfmXconDftCount_Type=Unsigned32
_FsEcfmXconDftCount_Object=MibScalar
fsEcfmXconDftCount=_FsEcfmXconDftCount_Object((1,3,6,1,4,1,2076,150,1,23),_FsEcfmXconDftCount_Type())
fsEcfmXconDftCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmXconDftCount.setStatus(_A)
class _FsEcfmCrosscheckDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,100))
_FsEcfmCrosscheckDelay_Type.__name__=_D
_FsEcfmCrosscheckDelay_Object=MibScalar
fsEcfmCrosscheckDelay=_FsEcfmCrosscheckDelay_Object((1,3,6,1,4,1,2076,150,1,24),_FsEcfmCrosscheckDelay_Type())
fsEcfmCrosscheckDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmCrosscheckDelay.setStatus(_A)
_FsEcfmMipDynamicEvaluationStatus_Type=TruthValue
_FsEcfmMipDynamicEvaluationStatus_Object=MibScalar
fsEcfmMipDynamicEvaluationStatus=_FsEcfmMipDynamicEvaluationStatus_Object((1,3,6,1,4,1,2076,150,1,25),_FsEcfmMipDynamicEvaluationStatus_Type())
fsEcfmMipDynamicEvaluationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMipDynamicEvaluationStatus.setStatus(_A)
_FsEcfmMipTable_Object=MibTable
fsEcfmMipTable=_FsEcfmMipTable_Object((1,3,6,1,4,1,2076,150,1,26))
if mibBuilder.loadTexts:fsEcfmMipTable.setStatus(_A)
_FsEcfmMipEntry_Object=MibTableRow
fsEcfmMipEntry=_FsEcfmMipEntry_Object((1,3,6,1,4,1,2076,150,1,26,1))
fsEcfmMipEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsEcfmMipEntry.setStatus(_A)
_FsEcfmMipIfIndex_Type=InterfaceIndex
_FsEcfmMipIfIndex_Object=MibTableColumn
fsEcfmMipIfIndex=_FsEcfmMipIfIndex_Object((1,3,6,1,4,1,2076,150,1,26,1,1),_FsEcfmMipIfIndex_Type())
fsEcfmMipIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMipIfIndex.setStatus(_A)
class _FsEcfmMipMdLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsEcfmMipMdLevel_Type.__name__=_D
_FsEcfmMipMdLevel_Object=MibTableColumn
fsEcfmMipMdLevel=_FsEcfmMipMdLevel_Object((1,3,6,1,4,1,2076,150,1,26,1,2),_FsEcfmMipMdLevel_Type())
fsEcfmMipMdLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMipMdLevel.setStatus(_A)
_FsEcfmMipVid_Type=VlanId
_FsEcfmMipVid_Object=MibTableColumn
fsEcfmMipVid=_FsEcfmMipVid_Object((1,3,6,1,4,1,2076,150,1,26,1,3),_FsEcfmMipVid_Type())
fsEcfmMipVid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMipVid.setStatus(_A)
_FsEcfmMipActive_Type=TruthValue
_FsEcfmMipActive_Object=MibTableColumn
fsEcfmMipActive=_FsEcfmMipActive_Object((1,3,6,1,4,1,2076,150,1,26,1,4),_FsEcfmMipActive_Type())
fsEcfmMipActive.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMipActive.setStatus(_A)
_FsEcfmMipRowStatus_Type=RowStatus
_FsEcfmMipRowStatus_Object=MibTableColumn
fsEcfmMipRowStatus=_FsEcfmMipRowStatus_Object((1,3,6,1,4,1,2076,150,1,26,1,5),_FsEcfmMipRowStatus_Type())
fsEcfmMipRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMipRowStatus.setStatus(_A)
_FsEcfmMipCcmDbTable_Object=MibTable
fsEcfmMipCcmDbTable=_FsEcfmMipCcmDbTable_Object((1,3,6,1,4,1,2076,150,1,27))
if mibBuilder.loadTexts:fsEcfmMipCcmDbTable.setStatus(_A)
_FsEcfmMipCcmDbEntry_Object=MibTableRow
fsEcfmMipCcmDbEntry=_FsEcfmMipCcmDbEntry_Object((1,3,6,1,4,1,2076,150,1,27,1))
fsEcfmMipCcmDbEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:fsEcfmMipCcmDbEntry.setStatus(_A)
class _FsEcfmMipCcmFid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsEcfmMipCcmFid_Type.__name__=_E
_FsEcfmMipCcmFid_Object=MibTableColumn
fsEcfmMipCcmFid=_FsEcfmMipCcmFid_Object((1,3,6,1,4,1,2076,150,1,27,1,1),_FsEcfmMipCcmFid_Type())
fsEcfmMipCcmFid.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMipCcmFid.setStatus(_A)
_FsEcfmMipCcmSrcAddr_Type=MacAddress
_FsEcfmMipCcmSrcAddr_Object=MibTableColumn
fsEcfmMipCcmSrcAddr=_FsEcfmMipCcmSrcAddr_Object((1,3,6,1,4,1,2076,150,1,27,1,2),_FsEcfmMipCcmSrcAddr_Type())
fsEcfmMipCcmSrcAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMipCcmSrcAddr.setStatus(_A)
_FsEcfmMipCcmIfIndex_Type=InterfaceIndex
_FsEcfmMipCcmIfIndex_Object=MibTableColumn
fsEcfmMipCcmIfIndex=_FsEcfmMipCcmIfIndex_Object((1,3,6,1,4,1,2076,150,1,27,1,3),_FsEcfmMipCcmIfIndex_Type())
fsEcfmMipCcmIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsEcfmMipCcmIfIndex.setStatus(_A)
class _FsEcfmGlobalCcmOffload_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmGlobalCcmOffload_Type.__name__=_D
_FsEcfmGlobalCcmOffload_Object=MibScalar
fsEcfmGlobalCcmOffload=_FsEcfmGlobalCcmOffload_Object((1,3,6,1,4,1,2076,150,1,28),_FsEcfmGlobalCcmOffload_Type())
fsEcfmGlobalCcmOffload.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmGlobalCcmOffload.setStatus(_A)
_FsEcfmDynMipPreventionTable_Object=MibTable
fsEcfmDynMipPreventionTable=_FsEcfmDynMipPreventionTable_Object((1,3,6,1,4,1,2076,150,1,29))
if mibBuilder.loadTexts:fsEcfmDynMipPreventionTable.setStatus(_A)
_FsEcfmDynMipPreventionEntry_Object=MibTableRow
fsEcfmDynMipPreventionEntry=_FsEcfmDynMipPreventionEntry_Object((1,3,6,1,4,1,2076,150,1,29,1))
fsEcfmDynMipPreventionEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsEcfmDynMipPreventionEntry.setStatus(_A)
class _FsEcfmDynMipPreventionRowStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,6)));namedValues=NamedValues(*(('createAndGo',4),('destroy',6)))
_FsEcfmDynMipPreventionRowStatus_Type.__name__=_U
_FsEcfmDynMipPreventionRowStatus_Object=MibTableColumn
fsEcfmDynMipPreventionRowStatus=_FsEcfmDynMipPreventionRowStatus_Object((1,3,6,1,4,1,2076,150,1,29,1,1),_FsEcfmDynMipPreventionRowStatus_Type())
fsEcfmDynMipPreventionRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmDynMipPreventionRowStatus.setStatus(_A)
_FsEcfmExObjects_ObjectIdentity=ObjectIdentity
fsEcfmExObjects=_FsEcfmExObjects_ObjectIdentity((1,3,6,1,4,1,2076,150,2))
_FsEcfmRemoteMepDbExTable_Object=MibTable
fsEcfmRemoteMepDbExTable=_FsEcfmRemoteMepDbExTable_Object((1,3,6,1,4,1,2076,150,2,1))
if mibBuilder.loadTexts:fsEcfmRemoteMepDbExTable.setStatus(_A)
_FsEcfmRemoteMepDbExEntry_Object=MibTableRow
fsEcfmRemoteMepDbExEntry=_FsEcfmRemoteMepDbExEntry_Object((1,3,6,1,4,1,2076,150,2,1,1))
fsEcfmRemoteMepDbExEntry.setIndexNames((0,_C,_J),(0,_C,_L),(0,_C,_N),(0,_C,_a))
if mibBuilder.loadTexts:fsEcfmRemoteMepDbExEntry.setStatus(_A)
class _FsEcfmMdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsEcfmMdIndex_Type.__name__=_E
_FsEcfmMdIndex_Object=MibTableColumn
fsEcfmMdIndex=_FsEcfmMdIndex_Object((1,3,6,1,4,1,2076,150,2,1,1,1),_FsEcfmMdIndex_Type())
fsEcfmMdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMdIndex.setStatus(_A)
class _FsEcfmMaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsEcfmMaIndex_Type.__name__=_E
_FsEcfmMaIndex_Object=MibTableColumn
fsEcfmMaIndex=_FsEcfmMaIndex_Object((1,3,6,1,4,1,2076,150,2,1,1,2),_FsEcfmMaIndex_Type())
fsEcfmMaIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMaIndex.setStatus(_A)
class _FsEcfmMepIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_FsEcfmMepIdentifier_Type.__name__=_E
_FsEcfmMepIdentifier_Object=MibTableColumn
fsEcfmMepIdentifier=_FsEcfmMepIdentifier_Object((1,3,6,1,4,1,2076,150,2,1,1,3),_FsEcfmMepIdentifier_Type())
fsEcfmMepIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmMepIdentifier.setStatus(_A)
class _FsEcfmRMepIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_FsEcfmRMepIdentifier_Type.__name__=_E
_FsEcfmRMepIdentifier_Object=MibTableColumn
fsEcfmRMepIdentifier=_FsEcfmRMepIdentifier_Object((1,3,6,1,4,1,2076,150,2,1,1,4),_FsEcfmRMepIdentifier_Type())
fsEcfmRMepIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmRMepIdentifier.setStatus(_A)
_FsEcfmRMepCcmSequenceNum_Type=Unsigned32
_FsEcfmRMepCcmSequenceNum_Object=MibTableColumn
fsEcfmRMepCcmSequenceNum=_FsEcfmRMepCcmSequenceNum_Object((1,3,6,1,4,1,2076,150,2,1,1,5),_FsEcfmRMepCcmSequenceNum_Type())
fsEcfmRMepCcmSequenceNum.setMaxAccess(_K)
if mibBuilder.loadTexts:fsEcfmRMepCcmSequenceNum.setStatus(_A)
_FsEcfmRMepPortStatusDefect_Type=TruthValue
_FsEcfmRMepPortStatusDefect_Object=MibTableColumn
fsEcfmRMepPortStatusDefect=_FsEcfmRMepPortStatusDefect_Object((1,3,6,1,4,1,2076,150,2,1,1,6),_FsEcfmRMepPortStatusDefect_Type())
fsEcfmRMepPortStatusDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepPortStatusDefect.setStatus(_A)
_FsEcfmRMepInterfaceStatusDefect_Type=TruthValue
_FsEcfmRMepInterfaceStatusDefect_Object=MibTableColumn
fsEcfmRMepInterfaceStatusDefect=_FsEcfmRMepInterfaceStatusDefect_Object((1,3,6,1,4,1,2076,150,2,1,1,7),_FsEcfmRMepInterfaceStatusDefect_Type())
fsEcfmRMepInterfaceStatusDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepInterfaceStatusDefect.setStatus(_A)
_FsEcfmRMepCcmDefect_Type=TruthValue
_FsEcfmRMepCcmDefect_Object=MibTableColumn
fsEcfmRMepCcmDefect=_FsEcfmRMepCcmDefect_Object((1,3,6,1,4,1,2076,150,2,1,1,8),_FsEcfmRMepCcmDefect_Type())
fsEcfmRMepCcmDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepCcmDefect.setStatus(_A)
_FsEcfmRMepRDIDefect_Type=TruthValue
_FsEcfmRMepRDIDefect_Object=MibTableColumn
fsEcfmRMepRDIDefect=_FsEcfmRMepRDIDefect_Object((1,3,6,1,4,1,2076,150,2,1,1,9),_FsEcfmRMepRDIDefect_Type())
fsEcfmRMepRDIDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepRDIDefect.setStatus(_A)
_FsEcfmRMepMacAddress_Type=MacAddress
_FsEcfmRMepMacAddress_Object=MibTableColumn
fsEcfmRMepMacAddress=_FsEcfmRMepMacAddress_Object((1,3,6,1,4,1,2076,150,2,1,1,10),_FsEcfmRMepMacAddress_Type())
fsEcfmRMepMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepMacAddress.setStatus(_A)
_FsEcfmRMepRdi_Type=TruthValue
_FsEcfmRMepRdi_Object=MibTableColumn
fsEcfmRMepRdi=_FsEcfmRMepRdi_Object((1,3,6,1,4,1,2076,150,2,1,1,11),_FsEcfmRMepRdi_Type())
fsEcfmRMepRdi.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepRdi.setStatus(_A)
class _FsEcfmRMepPortStatusTlv_Type(Dot1agCfmPortStatus):defaultValue=0
_FsEcfmRMepPortStatusTlv_Type.__name__=_S
_FsEcfmRMepPortStatusTlv_Object=MibTableColumn
fsEcfmRMepPortStatusTlv=_FsEcfmRMepPortStatusTlv_Object((1,3,6,1,4,1,2076,150,2,1,1,12),_FsEcfmRMepPortStatusTlv_Type())
fsEcfmRMepPortStatusTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepPortStatusTlv.setStatus(_A)
class _FsEcfmRMepInterfaceStatusTlv_Type(Dot1agCfmInterfaceStatus):defaultValue=0
_FsEcfmRMepInterfaceStatusTlv_Type.__name__=_R
_FsEcfmRMepInterfaceStatusTlv_Object=MibTableColumn
fsEcfmRMepInterfaceStatusTlv=_FsEcfmRMepInterfaceStatusTlv_Object((1,3,6,1,4,1,2076,150,2,1,1,13),_FsEcfmRMepInterfaceStatusTlv_Type())
fsEcfmRMepInterfaceStatusTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepInterfaceStatusTlv.setStatus(_A)
class _FsEcfmRMepChassisIdSubtype_Type(LldpChassisIdSubtype):defaultValue=4
_FsEcfmRMepChassisIdSubtype_Type.__name__=_T
_FsEcfmRMepChassisIdSubtype_Object=MibTableColumn
fsEcfmRMepChassisIdSubtype=_FsEcfmRMepChassisIdSubtype_Object((1,3,6,1,4,1,2076,150,2,1,1,14),_FsEcfmRMepChassisIdSubtype_Type())
fsEcfmRMepChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepChassisIdSubtype.setStatus(_A)
_FsEcfmMepDbChassisId_Type=LldpChassisId
_FsEcfmMepDbChassisId_Object=MibTableColumn
fsEcfmMepDbChassisId=_FsEcfmMepDbChassisId_Object((1,3,6,1,4,1,2076,150,2,1,1,15),_FsEcfmMepDbChassisId_Type())
fsEcfmMepDbChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDbChassisId.setStatus(_A)
_FsEcfmRMepManAddressDomain_Type=TDomain
_FsEcfmRMepManAddressDomain_Object=MibTableColumn
fsEcfmRMepManAddressDomain=_FsEcfmRMepManAddressDomain_Object((1,3,6,1,4,1,2076,150,2,1,1,16),_FsEcfmRMepManAddressDomain_Type())
fsEcfmRMepManAddressDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepManAddressDomain.setStatus(_A)
_FsEcfmRMepManAddress_Type=TAddress
_FsEcfmRMepManAddress_Object=MibTableColumn
fsEcfmRMepManAddress=_FsEcfmRMepManAddress_Object((1,3,6,1,4,1,2076,150,2,1,1,17),_FsEcfmRMepManAddress_Type())
fsEcfmRMepManAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmRMepManAddress.setStatus(_A)
_FsEcfmLtmTable_Object=MibTable
fsEcfmLtmTable=_FsEcfmLtmTable_Object((1,3,6,1,4,1,2076,150,2,2))
if mibBuilder.loadTexts:fsEcfmLtmTable.setStatus(_A)
_FsEcfmLtmEntry_Object=MibTableRow
fsEcfmLtmEntry=_FsEcfmLtmEntry_Object((1,3,6,1,4,1,2076,150,2,2,1))
fsEcfmLtmEntry.setIndexNames((0,_C,_J),(0,_C,_L),(0,_C,_N),(0,_C,_b))
if mibBuilder.loadTexts:fsEcfmLtmEntry.setStatus(_A)
class _FsEcfmLtmSeqNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsEcfmLtmSeqNumber_Type.__name__=_E
_FsEcfmLtmSeqNumber_Object=MibTableColumn
fsEcfmLtmSeqNumber=_FsEcfmLtmSeqNumber_Object((1,3,6,1,4,1,2076,150,2,2,1,1),_FsEcfmLtmSeqNumber_Type())
fsEcfmLtmSeqNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEcfmLtmSeqNumber.setStatus(_A)
_FsEcfmLtmTargetMacAddress_Type=MacAddress
_FsEcfmLtmTargetMacAddress_Object=MibTableColumn
fsEcfmLtmTargetMacAddress=_FsEcfmLtmTargetMacAddress_Object((1,3,6,1,4,1,2076,150,2,2,1,2),_FsEcfmLtmTargetMacAddress_Type())
fsEcfmLtmTargetMacAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:fsEcfmLtmTargetMacAddress.setStatus(_A)
class _FsEcfmLtmTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsEcfmLtmTtl_Type.__name__=_E
_FsEcfmLtmTtl_Object=MibTableColumn
fsEcfmLtmTtl=_FsEcfmLtmTtl_Object((1,3,6,1,4,1,2076,150,2,2,1,3),_FsEcfmLtmTtl_Type())
fsEcfmLtmTtl.setMaxAccess(_K)
if mibBuilder.loadTexts:fsEcfmLtmTtl.setStatus(_A)
_FsEcfmMepExTable_Object=MibTable
fsEcfmMepExTable=_FsEcfmMepExTable_Object((1,3,6,1,4,1,2076,150,2,3))
if mibBuilder.loadTexts:fsEcfmMepExTable.setStatus(_A)
_FsEcfmMepExEntry_Object=MibTableRow
fsEcfmMepExEntry=_FsEcfmMepExEntry_Object((1,3,6,1,4,1,2076,150,2,3,1))
fsEcfmMepExEntry.setIndexNames((0,_C,_J),(0,_C,_L),(0,_C,_N))
if mibBuilder.loadTexts:fsEcfmMepExEntry.setStatus(_A)
class _FsEcfmXconnRMepId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_FsEcfmXconnRMepId_Type.__name__=_E
_FsEcfmXconnRMepId_Object=MibTableColumn
fsEcfmXconnRMepId=_FsEcfmXconnRMepId_Object((1,3,6,1,4,1,2076,150,2,3,1,1),_FsEcfmXconnRMepId_Type())
fsEcfmXconnRMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmXconnRMepId.setStatus(_A)
class _FsEcfmErrorRMepId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_FsEcfmErrorRMepId_Type.__name__=_E
_FsEcfmErrorRMepId_Object=MibTableColumn
fsEcfmErrorRMepId=_FsEcfmErrorRMepId_Object((1,3,6,1,4,1,2076,150,2,3,1,2),_FsEcfmErrorRMepId_Type())
fsEcfmErrorRMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmErrorRMepId.setStatus(_A)
_FsEcfmMepDefectRDICcm_Type=TruthValue
_FsEcfmMepDefectRDICcm_Object=MibTableColumn
fsEcfmMepDefectRDICcm=_FsEcfmMepDefectRDICcm_Object((1,3,6,1,4,1,2076,150,2,3,1,3),_FsEcfmMepDefectRDICcm_Type())
fsEcfmMepDefectRDICcm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDefectRDICcm.setStatus(_A)
_FsEcfmMepDefectMacStatus_Type=TruthValue
_FsEcfmMepDefectMacStatus_Object=MibTableColumn
fsEcfmMepDefectMacStatus=_FsEcfmMepDefectMacStatus_Object((1,3,6,1,4,1,2076,150,2,3,1,4),_FsEcfmMepDefectMacStatus_Type())
fsEcfmMepDefectMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDefectMacStatus.setStatus(_A)
_FsEcfmMepDefectRemoteCcm_Type=TruthValue
_FsEcfmMepDefectRemoteCcm_Object=MibTableColumn
fsEcfmMepDefectRemoteCcm=_FsEcfmMepDefectRemoteCcm_Object((1,3,6,1,4,1,2076,150,2,3,1,5),_FsEcfmMepDefectRemoteCcm_Type())
fsEcfmMepDefectRemoteCcm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDefectRemoteCcm.setStatus(_A)
_FsEcfmMepDefectErrorCcm_Type=TruthValue
_FsEcfmMepDefectErrorCcm_Object=MibTableColumn
fsEcfmMepDefectErrorCcm=_FsEcfmMepDefectErrorCcm_Object((1,3,6,1,4,1,2076,150,2,3,1,6),_FsEcfmMepDefectErrorCcm_Type())
fsEcfmMepDefectErrorCcm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDefectErrorCcm.setStatus(_A)
_FsEcfmMepDefectXconnCcm_Type=TruthValue
_FsEcfmMepDefectXconnCcm_Object=MibTableColumn
fsEcfmMepDefectXconnCcm=_FsEcfmMepDefectXconnCcm_Object((1,3,6,1,4,1,2076,150,2,3,1,7),_FsEcfmMepDefectXconnCcm_Type())
fsEcfmMepDefectXconnCcm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepDefectXconnCcm.setStatus(_A)
class _FsEcfmMepCcmOffload_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmMepCcmOffload_Type.__name__=_D
_FsEcfmMepCcmOffload_Object=MibTableColumn
fsEcfmMepCcmOffload=_FsEcfmMepCcmOffload_Object((1,3,6,1,4,1,2076,150,2,3,1,8),_FsEcfmMepCcmOffload_Type())
fsEcfmMepCcmOffload.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepCcmOffload.setStatus(_A)
_FsEcfmMepLbrIn_Type=Unsigned32
_FsEcfmMepLbrIn_Object=MibTableColumn
fsEcfmMepLbrIn=_FsEcfmMepLbrIn_Object((1,3,6,1,4,1,2076,150,2,3,1,9),_FsEcfmMepLbrIn_Type())
fsEcfmMepLbrIn.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepLbrIn.setStatus(_A)
_FsEcfmMepLbrInOutOfOrder_Type=Unsigned32
_FsEcfmMepLbrInOutOfOrder_Object=MibTableColumn
fsEcfmMepLbrInOutOfOrder=_FsEcfmMepLbrInOutOfOrder_Object((1,3,6,1,4,1,2076,150,2,3,1,10),_FsEcfmMepLbrInOutOfOrder_Type())
fsEcfmMepLbrInOutOfOrder.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepLbrInOutOfOrder.setStatus(_A)
_FsEcfmMepLbrBadMsdu_Type=Unsigned32
_FsEcfmMepLbrBadMsdu_Object=MibTableColumn
fsEcfmMepLbrBadMsdu=_FsEcfmMepLbrBadMsdu_Object((1,3,6,1,4,1,2076,150,2,3,1,11),_FsEcfmMepLbrBadMsdu_Type())
fsEcfmMepLbrBadMsdu.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepLbrBadMsdu.setStatus(_A)
_FsEcfmMepUnexpLtrIn_Type=Unsigned32
_FsEcfmMepUnexpLtrIn_Object=MibTableColumn
fsEcfmMepUnexpLtrIn=_FsEcfmMepUnexpLtrIn_Object((1,3,6,1,4,1,2076,150,2,3,1,12),_FsEcfmMepUnexpLtrIn_Type())
fsEcfmMepUnexpLtrIn.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepUnexpLtrIn.setStatus(_A)
_FsEcfmMepLbrOut_Type=Unsigned32
_FsEcfmMepLbrOut_Object=MibTableColumn
fsEcfmMepLbrOut=_FsEcfmMepLbrOut_Object((1,3,6,1,4,1,2076,150,2,3,1,13),_FsEcfmMepLbrOut_Type())
fsEcfmMepLbrOut.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepLbrOut.setStatus(_A)
_FsEcfmMepCcmSequenceErrors_Type=Unsigned32
_FsEcfmMepCcmSequenceErrors_Object=MibTableColumn
fsEcfmMepCcmSequenceErrors=_FsEcfmMepCcmSequenceErrors_Object((1,3,6,1,4,1,2076,150,2,3,1,14),_FsEcfmMepCcmSequenceErrors_Type())
fsEcfmMepCcmSequenceErrors.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepCcmSequenceErrors.setStatus(_A)
_FsEcfmMepCciSentCcms_Type=Unsigned32
_FsEcfmMepCciSentCcms_Object=MibTableColumn
fsEcfmMepCciSentCcms=_FsEcfmMepCciSentCcms_Object((1,3,6,1,4,1,2076,150,2,3,1,15),_FsEcfmMepCciSentCcms_Type())
fsEcfmMepCciSentCcms.setMaxAccess(_G)
if mibBuilder.loadTexts:fsEcfmMepCciSentCcms.setStatus(_A)
_FsEcfmMdExTable_Object=MibTable
fsEcfmMdExTable=_FsEcfmMdExTable_Object((1,3,6,1,4,1,2076,150,2,4))
if mibBuilder.loadTexts:fsEcfmMdExTable.setStatus(_A)
_FsEcfmMdExEntry_Object=MibTableRow
fsEcfmMdExEntry=_FsEcfmMdExEntry_Object((1,3,6,1,4,1,2076,150,2,4,1))
fsEcfmMdExEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:fsEcfmMdExEntry.setStatus(_A)
class _FsEcfmMepArchiveHoldTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_FsEcfmMepArchiveHoldTime_Type.__name__=_D
_FsEcfmMepArchiveHoldTime_Object=MibTableColumn
fsEcfmMepArchiveHoldTime=_FsEcfmMepArchiveHoldTime_Object((1,3,6,1,4,1,2076,150,2,4,1,1),_FsEcfmMepArchiveHoldTime_Type())
fsEcfmMepArchiveHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMepArchiveHoldTime.setStatus(_A)
_FsEcfmMaExTable_Object=MibTable
fsEcfmMaExTable=_FsEcfmMaExTable_Object((1,3,6,1,4,1,2076,150,2,5))
if mibBuilder.loadTexts:fsEcfmMaExTable.setStatus(_A)
_FsEcfmMaExEntry_Object=MibTableRow
fsEcfmMaExEntry=_FsEcfmMaExEntry_Object((1,3,6,1,4,1,2076,150,2,5,1))
fsEcfmMaExEntry.setIndexNames((0,_C,_J),(0,_C,_L))
if mibBuilder.loadTexts:fsEcfmMaExEntry.setStatus(_A)
class _FsEcfmMaCrosscheckStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsEcfmMaCrosscheckStatus_Type.__name__=_D
_FsEcfmMaCrosscheckStatus_Object=MibTableColumn
fsEcfmMaCrosscheckStatus=_FsEcfmMaCrosscheckStatus_Object((1,3,6,1,4,1,2076,150,2,5,1,1),_FsEcfmMaCrosscheckStatus_Type())
fsEcfmMaCrosscheckStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmMaCrosscheckStatus.setStatus(_A)
_FsEcfmTrapsControl_ObjectIdentity=ObjectIdentity
fsEcfmTrapsControl=_FsEcfmTrapsControl_ObjectIdentity((1,3,6,1,4,1,2076,150,3))
_FsEcfmTrapControl_Type=FsEcfmSetTraps
_FsEcfmTrapControl_Object=MibScalar
fsEcfmTrapControl=_FsEcfmTrapControl_Object((1,3,6,1,4,1,2076,150,3,1),_FsEcfmTrapControl_Type())
fsEcfmTrapControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsEcfmTrapControl.setStatus(_A)
class _FsEcfmTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),(_V,2),('trapMACStatus',3),(_W,4),('trapErroredCCM',5),('trapXConnCCM',6)))
_FsEcfmTrapType_Type.__name__=_D
_FsEcfmTrapType_Object=MibScalar
fsEcfmTrapType=_FsEcfmTrapType_Object((1,3,6,1,4,1,2076,150,3,2),_FsEcfmTrapType_Type())
fsEcfmTrapType.setMaxAccess(_K)
if mibBuilder.loadTexts:fsEcfmTrapType.setStatus(_A)
_FsEcfmTraps_ObjectIdentity=ObjectIdentity
fsEcfmTraps=_FsEcfmTraps_ObjectIdentity((1,3,6,1,4,1,2076,150,4))
_FutureEcfmTraps_ObjectIdentity=ObjectIdentity
futureEcfmTraps=_FutureEcfmTraps_ObjectIdentity((1,3,6,1,4,1,2076,150,4,0))
fsEcfmMepDefectTrap=NotificationType((1,3,6,1,4,1,2076,150,4,0,1))
fsEcfmMepDefectTrap.setObjects((_C,_c))
if mibBuilder.loadTexts:fsEcfmMepDefectTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FsEcfmOuiType':FsEcfmOuiType,'FsEcfmSetTraps':FsEcfmSetTraps,'fsecfm':fsecfm,'fsEcfmSystem':fsEcfmSystem,'fsEcfmSystemControl':fsEcfmSystemControl,'fsEcfmModuleStatus':fsEcfmModuleStatus,'fsEcfmOui':fsEcfmOui,'fsEcfmTraceOption':fsEcfmTraceOption,'fsEcfmLtrCacheStatus':fsEcfmLtrCacheStatus,'fsEcfmLtrCacheClear':fsEcfmLtrCacheClear,'fsEcfmLtrCacheHoldTime':fsEcfmLtrCacheHoldTime,'fsEcfmLtrCacheSize':fsEcfmLtrCacheSize,'fsEcfmPortTable':fsEcfmPortTable,'fsEcfmPortEntry':fsEcfmPortEntry,_X:fsEcfmPortIndex,'fsEcfmPortLLCEncapStatus':fsEcfmPortLLCEncapStatus,'fsEcfmPortModuleStatus':fsEcfmPortModuleStatus,'fsEcfmPortTxCfmPduCount':fsEcfmPortTxCfmPduCount,'fsEcfmPortTxCcmCount':fsEcfmPortTxCcmCount,'fsEcfmPortTxLbmCount':fsEcfmPortTxLbmCount,'fsEcfmPortTxLbrCount':fsEcfmPortTxLbrCount,'fsEcfmPortTxLtmCount':fsEcfmPortTxLtmCount,'fsEcfmPortTxLtrCount':fsEcfmPortTxLtrCount,'fsEcfmPortTxFailedCount':fsEcfmPortTxFailedCount,'fsEcfmPortRxCfmPduCount':fsEcfmPortRxCfmPduCount,'fsEcfmPortRxCcmCount':fsEcfmPortRxCcmCount,'fsEcfmPortRxLbmCount':fsEcfmPortRxLbmCount,'fsEcfmPortRxLbrCount':fsEcfmPortRxLbrCount,'fsEcfmPortRxLtmCount':fsEcfmPortRxLtmCount,'fsEcfmPortRxLtrCount':fsEcfmPortRxLtrCount,'fsEcfmPortRxBadCfmPduCount':fsEcfmPortRxBadCfmPduCount,'fsEcfmPortFrwdCfmPduCount':fsEcfmPortFrwdCfmPduCount,'fsEcfmPortDsrdCfmPduCount':fsEcfmPortDsrdCfmPduCount,'fsEcfmMipCcmDbStatus':fsEcfmMipCcmDbStatus,'fsEcfmMipCcmDbClear':fsEcfmMipCcmDbClear,'fsEcfmMipCcmDbSize':fsEcfmMipCcmDbSize,'fsEcfmMipCcmDbHoldTime':fsEcfmMipCcmDbHoldTime,'fsEcfmMemoryFailureCount':fsEcfmMemoryFailureCount,'fsEcfmBufferFailureCount':fsEcfmBufferFailureCount,'fsEcfmUpCount':fsEcfmUpCount,'fsEcfmDownCount':fsEcfmDownCount,'fsEcfmNoDftCount':fsEcfmNoDftCount,'fsEcfmRdiDftCount':fsEcfmRdiDftCount,'fsEcfmMacStatusDftCount':fsEcfmMacStatusDftCount,'fsEcfmRemoteCcmDftCount':fsEcfmRemoteCcmDftCount,'fsEcfmErrorCcmDftCount':fsEcfmErrorCcmDftCount,'fsEcfmXconDftCount':fsEcfmXconDftCount,'fsEcfmCrosscheckDelay':fsEcfmCrosscheckDelay,'fsEcfmMipDynamicEvaluationStatus':fsEcfmMipDynamicEvaluationStatus,'fsEcfmMipTable':fsEcfmMipTable,'fsEcfmMipEntry':fsEcfmMipEntry,_O:fsEcfmMipIfIndex,_P:fsEcfmMipMdLevel,_Q:fsEcfmMipVid,'fsEcfmMipActive':fsEcfmMipActive,'fsEcfmMipRowStatus':fsEcfmMipRowStatus,'fsEcfmMipCcmDbTable':fsEcfmMipCcmDbTable,'fsEcfmMipCcmDbEntry':fsEcfmMipCcmDbEntry,_Y:fsEcfmMipCcmFid,_Z:fsEcfmMipCcmSrcAddr,'fsEcfmMipCcmIfIndex':fsEcfmMipCcmIfIndex,'fsEcfmGlobalCcmOffload':fsEcfmGlobalCcmOffload,'fsEcfmDynMipPreventionTable':fsEcfmDynMipPreventionTable,'fsEcfmDynMipPreventionEntry':fsEcfmDynMipPreventionEntry,'fsEcfmDynMipPreventionRowStatus':fsEcfmDynMipPreventionRowStatus,'fsEcfmExObjects':fsEcfmExObjects,'fsEcfmRemoteMepDbExTable':fsEcfmRemoteMepDbExTable,'fsEcfmRemoteMepDbExEntry':fsEcfmRemoteMepDbExEntry,_J:fsEcfmMdIndex,_L:fsEcfmMaIndex,_N:fsEcfmMepIdentifier,_a:fsEcfmRMepIdentifier,'fsEcfmRMepCcmSequenceNum':fsEcfmRMepCcmSequenceNum,'fsEcfmRMepPortStatusDefect':fsEcfmRMepPortStatusDefect,'fsEcfmRMepInterfaceStatusDefect':fsEcfmRMepInterfaceStatusDefect,'fsEcfmRMepCcmDefect':fsEcfmRMepCcmDefect,'fsEcfmRMepRDIDefect':fsEcfmRMepRDIDefect,'fsEcfmRMepMacAddress':fsEcfmRMepMacAddress,'fsEcfmRMepRdi':fsEcfmRMepRdi,'fsEcfmRMepPortStatusTlv':fsEcfmRMepPortStatusTlv,'fsEcfmRMepInterfaceStatusTlv':fsEcfmRMepInterfaceStatusTlv,'fsEcfmRMepChassisIdSubtype':fsEcfmRMepChassisIdSubtype,'fsEcfmMepDbChassisId':fsEcfmMepDbChassisId,'fsEcfmRMepManAddressDomain':fsEcfmRMepManAddressDomain,'fsEcfmRMepManAddress':fsEcfmRMepManAddress,'fsEcfmLtmTable':fsEcfmLtmTable,'fsEcfmLtmEntry':fsEcfmLtmEntry,_b:fsEcfmLtmSeqNumber,'fsEcfmLtmTargetMacAddress':fsEcfmLtmTargetMacAddress,'fsEcfmLtmTtl':fsEcfmLtmTtl,'fsEcfmMepExTable':fsEcfmMepExTable,'fsEcfmMepExEntry':fsEcfmMepExEntry,'fsEcfmXconnRMepId':fsEcfmXconnRMepId,'fsEcfmErrorRMepId':fsEcfmErrorRMepId,'fsEcfmMepDefectRDICcm':fsEcfmMepDefectRDICcm,'fsEcfmMepDefectMacStatus':fsEcfmMepDefectMacStatus,'fsEcfmMepDefectRemoteCcm':fsEcfmMepDefectRemoteCcm,'fsEcfmMepDefectErrorCcm':fsEcfmMepDefectErrorCcm,'fsEcfmMepDefectXconnCcm':fsEcfmMepDefectXconnCcm,'fsEcfmMepCcmOffload':fsEcfmMepCcmOffload,'fsEcfmMepLbrIn':fsEcfmMepLbrIn,'fsEcfmMepLbrInOutOfOrder':fsEcfmMepLbrInOutOfOrder,'fsEcfmMepLbrBadMsdu':fsEcfmMepLbrBadMsdu,'fsEcfmMepUnexpLtrIn':fsEcfmMepUnexpLtrIn,'fsEcfmMepLbrOut':fsEcfmMepLbrOut,'fsEcfmMepCcmSequenceErrors':fsEcfmMepCcmSequenceErrors,'fsEcfmMepCciSentCcms':fsEcfmMepCciSentCcms,'fsEcfmMdExTable':fsEcfmMdExTable,'fsEcfmMdExEntry':fsEcfmMdExEntry,'fsEcfmMepArchiveHoldTime':fsEcfmMepArchiveHoldTime,'fsEcfmMaExTable':fsEcfmMaExTable,'fsEcfmMaExEntry':fsEcfmMaExEntry,'fsEcfmMaCrosscheckStatus':fsEcfmMaCrosscheckStatus,'fsEcfmTrapsControl':fsEcfmTrapsControl,'fsEcfmTrapControl':fsEcfmTrapControl,_c:fsEcfmTrapType,'fsEcfmTraps':fsEcfmTraps,'futureEcfmTraps':futureEcfmTraps,'fsEcfmMepDefectTrap':fsEcfmMepDefectTrap})