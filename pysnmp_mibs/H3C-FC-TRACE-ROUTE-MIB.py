_P='h3cFcTraceRouteOperStatus'
_O='h3cFcTraceRouteAddress'
_N='h3cFcTraceRouteAddressType'
_M='h3cFcTraceRouteVsan'
_L='h3cFcTraceRouteHopsIndex'
_K='read-only'
_J='seconds'
_I='TruthValue'
_H='Integer32'
_G='H3cFcStartOper'
_F='H3cFcAddressType'
_E='h3cFcTraceRouteIndex'
_D='Unsigned32'
_C='read-create'
_B='H3C-FC-TRACE-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcAddress,H3cFcAddressType,H3cFcNameId,H3cFcStartOper,H3cFcVsanIndex=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcAddress',_F,'H3cFcNameId',_G,'H3cFcVsanIndex')
h3cSan,=mibBuilder.importSymbols('H3C-VSAN-MIB','h3cSan')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
h3cFcTraceRoute=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,4))
if mibBuilder.loadTexts:h3cFcTraceRoute.setRevisions(('2013-02-27 00:00',))
_H3cFcTraceRouteObjects_ObjectIdentity=ObjectIdentity
h3cFcTraceRouteObjects=_H3cFcTraceRouteObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,4,1))
_H3cFcTraceRouteConfigurations_ObjectIdentity=ObjectIdentity
h3cFcTraceRouteConfigurations=_H3cFcTraceRouteConfigurations_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,4,1,1))
_H3cFcTraceRouteTable_Object=MibTable
h3cFcTraceRouteTable=_H3cFcTraceRouteTable_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1))
if mibBuilder.loadTexts:h3cFcTraceRouteTable.setStatus(_A)
_H3cFcTraceRouteEntry_Object=MibTableRow
h3cFcTraceRouteEntry=_H3cFcTraceRouteEntry_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1))
h3cFcTraceRouteEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cFcTraceRouteEntry.setStatus(_A)
class _H3cFcTraceRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cFcTraceRouteIndex_Type.__name__=_D
_H3cFcTraceRouteIndex_Object=MibTableColumn
h3cFcTraceRouteIndex=_H3cFcTraceRouteIndex_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,1),_H3cFcTraceRouteIndex_Type())
h3cFcTraceRouteIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cFcTraceRouteIndex.setStatus(_A)
_H3cFcTraceRouteVsan_Type=H3cFcVsanIndex
_H3cFcTraceRouteVsan_Object=MibTableColumn
h3cFcTraceRouteVsan=_H3cFcTraceRouteVsan_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,2),_H3cFcTraceRouteVsan_Type())
h3cFcTraceRouteVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteVsan.setStatus(_A)
class _H3cFcTraceRouteAddressType_Type(H3cFcAddressType):defaultValue=2
_H3cFcTraceRouteAddressType_Type.__name__=_F
_H3cFcTraceRouteAddressType_Object=MibTableColumn
h3cFcTraceRouteAddressType=_H3cFcTraceRouteAddressType_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,3),_H3cFcTraceRouteAddressType_Type())
h3cFcTraceRouteAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteAddressType.setStatus(_A)
_H3cFcTraceRouteAddress_Type=H3cFcAddress
_H3cFcTraceRouteAddress_Object=MibTableColumn
h3cFcTraceRouteAddress=_H3cFcTraceRouteAddress_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,4),_H3cFcTraceRouteAddress_Type())
h3cFcTraceRouteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteAddress.setStatus(_A)
class _H3cFcTraceRouteTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cFcTraceRouteTimeout_Type.__name__=_D
_H3cFcTraceRouteTimeout_Object=MibTableColumn
h3cFcTraceRouteTimeout=_H3cFcTraceRouteTimeout_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,5),_H3cFcTraceRouteTimeout_Type())
h3cFcTraceRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cFcTraceRouteTimeout.setUnits(_J)
class _H3cFcTraceRouteAdminStatus_Type(H3cFcStartOper):defaultValue=2
_H3cFcTraceRouteAdminStatus_Type.__name__=_G
_H3cFcTraceRouteAdminStatus_Object=MibTableColumn
h3cFcTraceRouteAdminStatus=_H3cFcTraceRouteAdminStatus_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,6),_H3cFcTraceRouteAdminStatus_Type())
h3cFcTraceRouteAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteAdminStatus.setStatus(_A)
class _H3cFcTraceRouteOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inProgress',1),('success',2),('partialSuccess',3),('failure',4),('disabled',5)))
_H3cFcTraceRouteOperStatus_Type.__name__=_H
_H3cFcTraceRouteOperStatus_Object=MibTableColumn
h3cFcTraceRouteOperStatus=_H3cFcTraceRouteOperStatus_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,7),_H3cFcTraceRouteOperStatus_Type())
h3cFcTraceRouteOperStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcTraceRouteOperStatus.setStatus(_A)
class _H3cFcTraceRouteAgeInterval_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,900))
_H3cFcTraceRouteAgeInterval_Type.__name__=_D
_H3cFcTraceRouteAgeInterval_Object=MibTableColumn
h3cFcTraceRouteAgeInterval=_H3cFcTraceRouteAgeInterval_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,8),_H3cFcTraceRouteAgeInterval_Type())
h3cFcTraceRouteAgeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteAgeInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cFcTraceRouteAgeInterval.setUnits(_J)
class _H3cFcTraceRouteTrapOnCompletion_Type(TruthValue):defaultValue=2
_H3cFcTraceRouteTrapOnCompletion_Type.__name__=_I
_H3cFcTraceRouteTrapOnCompletion_Object=MibTableColumn
h3cFcTraceRouteTrapOnCompletion=_H3cFcTraceRouteTrapOnCompletion_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,9),_H3cFcTraceRouteTrapOnCompletion_Type())
h3cFcTraceRouteTrapOnCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteTrapOnCompletion.setStatus(_A)
_H3cFcTraceRouteRowStatus_Type=RowStatus
_H3cFcTraceRouteRowStatus_Object=MibTableColumn
h3cFcTraceRouteRowStatus=_H3cFcTraceRouteRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,4,1,1,1,1,10),_H3cFcTraceRouteRowStatus_Type())
h3cFcTraceRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cFcTraceRouteRowStatus.setStatus(_A)
_H3cFcTraceRouteResults_ObjectIdentity=ObjectIdentity
h3cFcTraceRouteResults=_H3cFcTraceRouteResults_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,4,1,2))
_H3cFcTraceRouteHopsTable_Object=MibTable
h3cFcTraceRouteHopsTable=_H3cFcTraceRouteHopsTable_Object((1,3,6,1,4,1,2011,10,2,127,4,1,2,1))
if mibBuilder.loadTexts:h3cFcTraceRouteHopsTable.setStatus(_A)
_H3cFcTraceRouteHopsEntry_Object=MibTableRow
h3cFcTraceRouteHopsEntry=_H3cFcTraceRouteHopsEntry_Object((1,3,6,1,4,1,2011,10,2,127,4,1,2,1,1))
h3cFcTraceRouteHopsEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:h3cFcTraceRouteHopsEntry.setStatus(_A)
class _H3cFcTraceRouteHopsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cFcTraceRouteHopsIndex_Type.__name__=_D
_H3cFcTraceRouteHopsIndex_Object=MibTableColumn
h3cFcTraceRouteHopsIndex=_H3cFcTraceRouteHopsIndex_Object((1,3,6,1,4,1,2011,10,2,127,4,1,2,1,1,1),_H3cFcTraceRouteHopsIndex_Type())
h3cFcTraceRouteHopsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cFcTraceRouteHopsIndex.setStatus(_A)
_H3cFcTraceRouteHopsAddr_Type=H3cFcNameId
_H3cFcTraceRouteHopsAddr_Object=MibTableColumn
h3cFcTraceRouteHopsAddr=_H3cFcTraceRouteHopsAddr_Object((1,3,6,1,4,1,2011,10,2,127,4,1,2,1,1,2),_H3cFcTraceRouteHopsAddr_Type())
h3cFcTraceRouteHopsAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFcTraceRouteHopsAddr.setStatus(_A)
_H3cFcTraceRouteNotifications_ObjectIdentity=ObjectIdentity
h3cFcTraceRouteNotifications=_H3cFcTraceRouteNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,4,1,3))
_H3cFcTraceRouteNotifyPrefix_ObjectIdentity=ObjectIdentity
h3cFcTraceRouteNotifyPrefix=_H3cFcTraceRouteNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,4,1,3,0))
h3cFcTraceRouteCompletionNotify=NotificationType((1,3,6,1,4,1,2011,10,2,127,4,1,3,0,1))
h3cFcTraceRouteCompletionNotify.setObjects(*((_B,_E),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:h3cFcTraceRouteCompletionNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cFcTraceRoute':h3cFcTraceRoute,'h3cFcTraceRouteObjects':h3cFcTraceRouteObjects,'h3cFcTraceRouteConfigurations':h3cFcTraceRouteConfigurations,'h3cFcTraceRouteTable':h3cFcTraceRouteTable,'h3cFcTraceRouteEntry':h3cFcTraceRouteEntry,_E:h3cFcTraceRouteIndex,_M:h3cFcTraceRouteVsan,_N:h3cFcTraceRouteAddressType,_O:h3cFcTraceRouteAddress,'h3cFcTraceRouteTimeout':h3cFcTraceRouteTimeout,'h3cFcTraceRouteAdminStatus':h3cFcTraceRouteAdminStatus,_P:h3cFcTraceRouteOperStatus,'h3cFcTraceRouteAgeInterval':h3cFcTraceRouteAgeInterval,'h3cFcTraceRouteTrapOnCompletion':h3cFcTraceRouteTrapOnCompletion,'h3cFcTraceRouteRowStatus':h3cFcTraceRouteRowStatus,'h3cFcTraceRouteResults':h3cFcTraceRouteResults,'h3cFcTraceRouteHopsTable':h3cFcTraceRouteHopsTable,'h3cFcTraceRouteHopsEntry':h3cFcTraceRouteHopsEntry,_L:h3cFcTraceRouteHopsIndex,'h3cFcTraceRouteHopsAddr':h3cFcTraceRouteHopsAddr,'h3cFcTraceRouteNotifications':h3cFcTraceRouteNotifications,'h3cFcTraceRouteNotifyPrefix':h3cFcTraceRouteNotifyPrefix,'h3cFcTraceRouteCompletionNotify':h3cFcTraceRouteCompletionNotify})