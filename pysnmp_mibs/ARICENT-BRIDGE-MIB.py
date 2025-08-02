_S='dot1dMlistNumber'
_R='dot1dMcastMacaddress'
_Q='invalid'
_P='FFFFFFFFFFFF'
_O='dot1dFilterDstAddress'
_N='dot1dFilterSrcAddress'
_M='dot1dFilterNumber'
_L='dot1dFutureTpPort'
_K='dot1dFutureBasePort'
_J='MacAddress'
_I='down'
_H='up'
_G='read-write'
_F='read-only'
_E='not-accessible'
_D='ARICENT-BRIDGE-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_J,'PhysAddress','TextualConvention','TruthValue')
futureBridgeMIB=ModuleIdentity((1,3,6,1,4,1,2076,26))
if mibBuilder.loadTexts:futureBridgeMIB.setRevisions(('2012-09-05 00:00',))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Dot1dFutureBridge_ObjectIdentity=ObjectIdentity
dot1dFutureBridge=_Dot1dFutureBridge_ObjectIdentity((1,3,6,1,4,1,2076,26,1))
_Dot1dFutureBase_ObjectIdentity=ObjectIdentity
dot1dFutureBase=_Dot1dFutureBase_ObjectIdentity((1,3,6,1,4,1,2076,26,1,1))
class _Dot1dBridgeSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_Dot1dBridgeSystemControl_Type.__name__=_B
_Dot1dBridgeSystemControl_Object=MibScalar
dot1dBridgeSystemControl=_Dot1dBridgeSystemControl_Object((1,3,6,1,4,1,2076,26,1,1,1),_Dot1dBridgeSystemControl_Type())
dot1dBridgeSystemControl.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1dBridgeSystemControl.setStatus(_A)
class _Dot1dBaseBridgeStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('downwithallinterfacesdown',3)))
_Dot1dBaseBridgeStatus_Type.__name__=_B
_Dot1dBaseBridgeStatus_Object=MibScalar
dot1dBaseBridgeStatus=_Dot1dBaseBridgeStatus_Object((1,3,6,1,4,1,2076,26,1,1,2),_Dot1dBaseBridgeStatus_Type())
dot1dBaseBridgeStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1dBaseBridgeStatus.setStatus(_A)
class _Dot1dBaseBridgeCRCStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('withCRC',1),('withoutCRC',2)))
_Dot1dBaseBridgeCRCStatus_Type.__name__=_B
_Dot1dBaseBridgeCRCStatus_Object=MibScalar
dot1dBaseBridgeCRCStatus=_Dot1dBaseBridgeCRCStatus_Object((1,3,6,1,4,1,2076,26,1,1,3),_Dot1dBaseBridgeCRCStatus_Type())
dot1dBaseBridgeCRCStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1dBaseBridgeCRCStatus.setStatus(_A)
class _Dot1dBaseBridgeDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot1dBaseBridgeDebug_Type.__name__=_B
_Dot1dBaseBridgeDebug_Object=MibScalar
dot1dBaseBridgeDebug=_Dot1dBaseBridgeDebug_Object((1,3,6,1,4,1,2076,26,1,1,4),_Dot1dBaseBridgeDebug_Type())
dot1dBaseBridgeDebug.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1dBaseBridgeDebug.setStatus(_A)
class _Dot1dBaseBridgeTrace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot1dBaseBridgeTrace_Type.__name__=_B
_Dot1dBaseBridgeTrace_Object=MibScalar
dot1dBaseBridgeTrace=_Dot1dBaseBridgeTrace_Object((1,3,6,1,4,1,2076,26,1,1,5),_Dot1dBaseBridgeTrace_Type())
dot1dBaseBridgeTrace.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1dBaseBridgeTrace.setStatus(_A)
class _Dot1dBaseBridgeMaxFwdDbEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dBaseBridgeMaxFwdDbEntries_Type.__name__=_B
_Dot1dBaseBridgeMaxFwdDbEntries_Object=MibScalar
dot1dBaseBridgeMaxFwdDbEntries=_Dot1dBaseBridgeMaxFwdDbEntries_Object((1,3,6,1,4,1,2076,26,1,1,6),_Dot1dBaseBridgeMaxFwdDbEntries_Type())
dot1dBaseBridgeMaxFwdDbEntries.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dBaseBridgeMaxFwdDbEntries.setStatus(_A)
_Dot1dFutureBasePortTable_Object=MibTable
dot1dFutureBasePortTable=_Dot1dFutureBasePortTable_Object((1,3,6,1,4,1,2076,26,1,1,7))
if mibBuilder.loadTexts:dot1dFutureBasePortTable.setStatus(_A)
_Dot1dFutureBasePortEntry_Object=MibTableRow
dot1dFutureBasePortEntry=_Dot1dFutureBasePortEntry_Object((1,3,6,1,4,1,2076,26,1,1,7,1))
dot1dFutureBasePortEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:dot1dFutureBasePortEntry.setStatus(_A)
class _Dot1dFutureBasePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dFutureBasePort_Type.__name__=_B
_Dot1dFutureBasePort_Object=MibTableColumn
dot1dFutureBasePort=_Dot1dFutureBasePort_Object((1,3,6,1,4,1,2076,26,1,1,7,1,1),_Dot1dFutureBasePort_Type())
dot1dFutureBasePort.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dFutureBasePort.setStatus(_A)
class _Dot1dBasePortAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Dot1dBasePortAdminStatus_Type.__name__=_B
_Dot1dBasePortAdminStatus_Object=MibTableColumn
dot1dBasePortAdminStatus=_Dot1dBasePortAdminStatus_Object((1,3,6,1,4,1,2076,26,1,1,7,1,2),_Dot1dBasePortAdminStatus_Type())
dot1dBasePortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dBasePortAdminStatus.setStatus(_A)
class _Dot1dBasePortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Dot1dBasePortOperStatus_Type.__name__=_B
_Dot1dBasePortOperStatus_Object=MibTableColumn
dot1dBasePortOperStatus=_Dot1dBasePortOperStatus_Object((1,3,6,1,4,1,2076,26,1,1,7,1,3),_Dot1dBasePortOperStatus_Type())
dot1dBasePortOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dBasePortOperStatus.setStatus(_A)
class _Dot1dBasePortBcastStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Dot1dBasePortBcastStatus_Type.__name__=_B
_Dot1dBasePortBcastStatus_Object=MibTableColumn
dot1dBasePortBcastStatus=_Dot1dBasePortBcastStatus_Object((1,3,6,1,4,1,2076,26,1,1,7,1,4),_Dot1dBasePortBcastStatus_Type())
dot1dBasePortBcastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dBasePortBcastStatus.setStatus(_A)
class _Dot1dBasePortFilterNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_Dot1dBasePortFilterNumber_Type.__name__=_B
_Dot1dBasePortFilterNumber_Object=MibTableColumn
dot1dBasePortFilterNumber=_Dot1dBasePortFilterNumber_Object((1,3,6,1,4,1,2076,26,1,1,7,1,5),_Dot1dBasePortFilterNumber_Type())
dot1dBasePortFilterNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dBasePortFilterNumber.setStatus(_A)
class _Dot1dBasePortMcastNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_Dot1dBasePortMcastNumber_Type.__name__=_B
_Dot1dBasePortMcastNumber_Object=MibTableColumn
dot1dBasePortMcastNumber=_Dot1dBasePortMcastNumber_Object((1,3,6,1,4,1,2076,26,1,1,7,1,6),_Dot1dBasePortMcastNumber_Type())
dot1dBasePortMcastNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dBasePortMcastNumber.setStatus(_A)
_Dot1dBasePortBcastOutFrames_Type=Counter32
_Dot1dBasePortBcastOutFrames_Object=MibTableColumn
dot1dBasePortBcastOutFrames=_Dot1dBasePortBcastOutFrames_Object((1,3,6,1,4,1,2076,26,1,1,7,1,7),_Dot1dBasePortBcastOutFrames_Type())
dot1dBasePortBcastOutFrames.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dBasePortBcastOutFrames.setStatus(_A)
_Dot1dBasePortMcastOutFrames_Type=Counter32
_Dot1dBasePortMcastOutFrames_Object=MibTableColumn
dot1dBasePortMcastOutFrames=_Dot1dBasePortMcastOutFrames_Object((1,3,6,1,4,1,2076,26,1,1,7,1,8),_Dot1dBasePortMcastOutFrames_Type())
dot1dBasePortMcastOutFrames.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dBasePortMcastOutFrames.setStatus(_A)
_Dot1dFutureTp_ObjectIdentity=ObjectIdentity
dot1dFutureTp=_Dot1dFutureTp_ObjectIdentity((1,3,6,1,4,1,2076,26,1,2))
_Dot1dFutureTpPortTable_Object=MibTable
dot1dFutureTpPortTable=_Dot1dFutureTpPortTable_Object((1,3,6,1,4,1,2076,26,1,2,1))
if mibBuilder.loadTexts:dot1dFutureTpPortTable.setStatus(_A)
_Dot1dFutureTpPortEntry_Object=MibTableRow
dot1dFutureTpPortEntry=_Dot1dFutureTpPortEntry_Object((1,3,6,1,4,1,2076,26,1,2,1,1))
dot1dFutureTpPortEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:dot1dFutureTpPortEntry.setStatus(_A)
class _Dot1dFutureTpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dFutureTpPort_Type.__name__=_B
_Dot1dFutureTpPort_Object=MibTableColumn
dot1dFutureTpPort=_Dot1dFutureTpPort_Object((1,3,6,1,4,1,2076,26,1,2,1,1,1),_Dot1dFutureTpPort_Type())
dot1dFutureTpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dFutureTpPort.setStatus(_A)
_Dot1dTpPortInProtoDiscards_Type=Counter32
_Dot1dTpPortInProtoDiscards_Object=MibTableColumn
dot1dTpPortInProtoDiscards=_Dot1dTpPortInProtoDiscards_Object((1,3,6,1,4,1,2076,26,1,2,1,1,2),_Dot1dTpPortInProtoDiscards_Type())
dot1dTpPortInProtoDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dTpPortInProtoDiscards.setStatus(_A)
_Dot1dTpPortInFilterDiscards_Type=Counter32
_Dot1dTpPortInFilterDiscards_Object=MibTableColumn
dot1dTpPortInFilterDiscards=_Dot1dTpPortInFilterDiscards_Object((1,3,6,1,4,1,2076,26,1,2,1,1,3),_Dot1dTpPortInFilterDiscards_Type())
dot1dTpPortInFilterDiscards.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1dTpPortInFilterDiscards.setStatus(_A)
class _Dot1dTpPortProtocolFilterMask_Type(Integer32):defaultValue=0
_Dot1dTpPortProtocolFilterMask_Type.__name__=_B
_Dot1dTpPortProtocolFilterMask_Object=MibTableColumn
dot1dTpPortProtocolFilterMask=_Dot1dTpPortProtocolFilterMask_Object((1,3,6,1,4,1,2076,26,1,2,1,1,4),_Dot1dTpPortProtocolFilterMask_Type())
dot1dTpPortProtocolFilterMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dTpPortProtocolFilterMask.setStatus(_A)
_Dot1dFilter_ObjectIdentity=ObjectIdentity
dot1dFilter=_Dot1dFilter_ObjectIdentity((1,3,6,1,4,1,2076,26,1,3))
_Dot1dFilterTable_Object=MibTable
dot1dFilterTable=_Dot1dFilterTable_Object((1,3,6,1,4,1,2076,26,1,3,1))
if mibBuilder.loadTexts:dot1dFilterTable.setStatus(_A)
_Dot1dFilterEntry_Object=MibTableRow
dot1dFilterEntry=_Dot1dFilterEntry_Object((1,3,6,1,4,1,2076,26,1,3,1,1))
dot1dFilterEntry.setIndexNames((0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:dot1dFilterEntry.setStatus(_A)
class _Dot1dFilterNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_Dot1dFilterNumber_Type.__name__=_B
_Dot1dFilterNumber_Object=MibTableColumn
dot1dFilterNumber=_Dot1dFilterNumber_Object((1,3,6,1,4,1,2076,26,1,3,1,1,1),_Dot1dFilterNumber_Type())
dot1dFilterNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dFilterNumber.setStatus(_A)
_Dot1dFilterSrcAddress_Type=MacAddress
_Dot1dFilterSrcAddress_Object=MibTableColumn
dot1dFilterSrcAddress=_Dot1dFilterSrcAddress_Object((1,3,6,1,4,1,2076,26,1,3,1,1,2),_Dot1dFilterSrcAddress_Type())
dot1dFilterSrcAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dFilterSrcAddress.setStatus(_A)
class _Dot1dFilterSrcMask_Type(MacAddress):defaultHexValue=_P
_Dot1dFilterSrcMask_Type.__name__=_J
_Dot1dFilterSrcMask_Object=MibTableColumn
dot1dFilterSrcMask=_Dot1dFilterSrcMask_Object((1,3,6,1,4,1,2076,26,1,3,1,1,3),_Dot1dFilterSrcMask_Type())
dot1dFilterSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dFilterSrcMask.setStatus(_A)
_Dot1dFilterDstAddress_Type=MacAddress
_Dot1dFilterDstAddress_Object=MibTableColumn
dot1dFilterDstAddress=_Dot1dFilterDstAddress_Object((1,3,6,1,4,1,2076,26,1,3,1,1,4),_Dot1dFilterDstAddress_Type())
dot1dFilterDstAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dFilterDstAddress.setStatus(_A)
class _Dot1dFilterDstMask_Type(MacAddress):defaultHexValue=_P
_Dot1dFilterDstMask_Type.__name__=_J
_Dot1dFilterDstMask_Object=MibTableColumn
dot1dFilterDstMask=_Dot1dFilterDstMask_Object((1,3,6,1,4,1,2076,26,1,3,1,1,5),_Dot1dFilterDstMask_Type())
dot1dFilterDstMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dFilterDstMask.setStatus(_A)
class _Dot1dFilterPermiss_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('block',1),('allow',2),(_Q,3)))
_Dot1dFilterPermiss_Type.__name__=_B
_Dot1dFilterPermiss_Object=MibTableColumn
dot1dFilterPermiss=_Dot1dFilterPermiss_Object((1,3,6,1,4,1,2076,26,1,3,1,1,6),_Dot1dFilterPermiss_Type())
dot1dFilterPermiss.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dFilterPermiss.setStatus(_A)
_Dot1dMcast_ObjectIdentity=ObjectIdentity
dot1dMcast=_Dot1dMcast_ObjectIdentity((1,3,6,1,4,1,2076,26,1,4))
_Dot1dMcastTable_Object=MibTable
dot1dMcastTable=_Dot1dMcastTable_Object((1,3,6,1,4,1,2076,26,1,4,1))
if mibBuilder.loadTexts:dot1dMcastTable.setStatus(_A)
_Dot1dMcastEntry_Object=MibTableRow
dot1dMcastEntry=_Dot1dMcastEntry_Object((1,3,6,1,4,1,2076,26,1,4,1,1))
dot1dMcastEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:dot1dMcastEntry.setStatus(_A)
class _Dot1dMlistNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_Dot1dMlistNumber_Type.__name__=_B
_Dot1dMlistNumber_Object=MibTableColumn
dot1dMlistNumber=_Dot1dMlistNumber_Object((1,3,6,1,4,1,2076,26,1,4,1,1,1),_Dot1dMlistNumber_Type())
dot1dMlistNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dMlistNumber.setStatus(_A)
_Dot1dMcastMacaddress_Type=MacAddress
_Dot1dMcastMacaddress_Object=MibTableColumn
dot1dMcastMacaddress=_Dot1dMcastMacaddress_Object((1,3,6,1,4,1,2076,26,1,4,1,1,2),_Dot1dMcastMacaddress_Type())
dot1dMcastMacaddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1dMcastMacaddress.setStatus(_A)
class _Dot1dMcastPermiss_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('block',1),('allow',2),(_Q,3)))
_Dot1dMcastPermiss_Type.__name__=_B
_Dot1dMcastPermiss_Object=MibTableColumn
dot1dMcastPermiss=_Dot1dMcastPermiss_Object((1,3,6,1,4,1,2076,26,1,4,1,1,3),_Dot1dMcastPermiss_Type())
dot1dMcastPermiss.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dMcastPermiss.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'BridgeId':BridgeId,'futureBridgeMIB':futureBridgeMIB,'dot1dFutureBridge':dot1dFutureBridge,'dot1dFutureBase':dot1dFutureBase,'dot1dBridgeSystemControl':dot1dBridgeSystemControl,'dot1dBaseBridgeStatus':dot1dBaseBridgeStatus,'dot1dBaseBridgeCRCStatus':dot1dBaseBridgeCRCStatus,'dot1dBaseBridgeDebug':dot1dBaseBridgeDebug,'dot1dBaseBridgeTrace':dot1dBaseBridgeTrace,'dot1dBaseBridgeMaxFwdDbEntries':dot1dBaseBridgeMaxFwdDbEntries,'dot1dFutureBasePortTable':dot1dFutureBasePortTable,'dot1dFutureBasePortEntry':dot1dFutureBasePortEntry,_K:dot1dFutureBasePort,'dot1dBasePortAdminStatus':dot1dBasePortAdminStatus,'dot1dBasePortOperStatus':dot1dBasePortOperStatus,'dot1dBasePortBcastStatus':dot1dBasePortBcastStatus,'dot1dBasePortFilterNumber':dot1dBasePortFilterNumber,'dot1dBasePortMcastNumber':dot1dBasePortMcastNumber,'dot1dBasePortBcastOutFrames':dot1dBasePortBcastOutFrames,'dot1dBasePortMcastOutFrames':dot1dBasePortMcastOutFrames,'dot1dFutureTp':dot1dFutureTp,'dot1dFutureTpPortTable':dot1dFutureTpPortTable,'dot1dFutureTpPortEntry':dot1dFutureTpPortEntry,_L:dot1dFutureTpPort,'dot1dTpPortInProtoDiscards':dot1dTpPortInProtoDiscards,'dot1dTpPortInFilterDiscards':dot1dTpPortInFilterDiscards,'dot1dTpPortProtocolFilterMask':dot1dTpPortProtocolFilterMask,'dot1dFilter':dot1dFilter,'dot1dFilterTable':dot1dFilterTable,'dot1dFilterEntry':dot1dFilterEntry,_M:dot1dFilterNumber,_N:dot1dFilterSrcAddress,'dot1dFilterSrcMask':dot1dFilterSrcMask,_O:dot1dFilterDstAddress,'dot1dFilterDstMask':dot1dFilterDstMask,'dot1dFilterPermiss':dot1dFilterPermiss,'dot1dMcast':dot1dMcast,'dot1dMcastTable':dot1dMcastTable,'dot1dMcastEntry':dot1dMcastEntry,_S:dot1dMlistNumber,_R:dot1dMcastMacaddress,'dot1dMcastPermiss':dot1dMcastPermiss})