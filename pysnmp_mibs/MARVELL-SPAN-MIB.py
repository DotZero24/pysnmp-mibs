_H='rlSpanSourceIndex'
_G='rlSpanSourceType'
_F='rlSpanSourceSessionId'
_E='rlSpanDestinationSessionId'
_D='not-accessible'
_C='MARVELL-SPAN-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
rnd,rndNotifications=mibBuilder.importSymbols('RADLAN-MIB','rnd','rndNotifications')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlSpan=ModuleIdentity((1,3,6,1,4,1,89,219))
if mibBuilder.loadTexts:rlSpan.setRevisions(('2015-03-25 00:00',))
class SpanDestinationPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('monitor-only',1),('network',2)))
class SpanSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('port',1),('vlan',2),('flow',3),('remote-vlan',4)))
class SpanSourceDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rx',1),('tx',2),('both',3)))
_RlSpanMibVersion_Type=Integer32
_RlSpanMibVersion_Object=MibScalar
rlSpanMibVersion=_RlSpanMibVersion_Object((1,3,6,1,4,1,89,219,1),_RlSpanMibVersion_Type())
rlSpanMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlSpanMibVersion.setStatus(_A)
_RlSpanDestinationTable_Object=MibTable
rlSpanDestinationTable=_RlSpanDestinationTable_Object((1,3,6,1,4,1,89,219,2))
if mibBuilder.loadTexts:rlSpanDestinationTable.setStatus(_A)
_RlSpanDestinationEntry_Object=MibTableRow
rlSpanDestinationEntry=_RlSpanDestinationEntry_Object((1,3,6,1,4,1,89,219,2,1))
rlSpanDestinationEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:rlSpanDestinationEntry.setStatus(_A)
_RlSpanDestinationSessionId_Type=Integer32
_RlSpanDestinationSessionId_Object=MibTableColumn
rlSpanDestinationSessionId=_RlSpanDestinationSessionId_Object((1,3,6,1,4,1,89,219,2,1,1),_RlSpanDestinationSessionId_Type())
rlSpanDestinationSessionId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpanDestinationSessionId.setStatus(_A)
_RlSpanDestinationIfIndex_Type=InterfaceIndex
_RlSpanDestinationIfIndex_Object=MibTableColumn
rlSpanDestinationIfIndex=_RlSpanDestinationIfIndex_Object((1,3,6,1,4,1,89,219,2,1,2),_RlSpanDestinationIfIndex_Type())
rlSpanDestinationIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanDestinationIfIndex.setStatus(_A)
_RlSpanDestinationIsReflector_Type=TruthValue
_RlSpanDestinationIsReflector_Object=MibTableColumn
rlSpanDestinationIsReflector=_RlSpanDestinationIsReflector_Object((1,3,6,1,4,1,89,219,2,1,3),_RlSpanDestinationIsReflector_Type())
rlSpanDestinationIsReflector.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanDestinationIsReflector.setStatus(_A)
_RlSpanDestinationPortType_Type=SpanDestinationPortType
_RlSpanDestinationPortType_Object=MibTableColumn
rlSpanDestinationPortType=_RlSpanDestinationPortType_Object((1,3,6,1,4,1,89,219,2,1,4),_RlSpanDestinationPortType_Type())
rlSpanDestinationPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanDestinationPortType.setStatus(_A)
_RlSpanDestinationRowStatus_Type=RowStatus
_RlSpanDestinationRowStatus_Object=MibTableColumn
rlSpanDestinationRowStatus=_RlSpanDestinationRowStatus_Object((1,3,6,1,4,1,89,219,2,1,5),_RlSpanDestinationRowStatus_Type())
rlSpanDestinationRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanDestinationRowStatus.setStatus(_A)
_RlSpanSourceTable_Object=MibTable
rlSpanSourceTable=_RlSpanSourceTable_Object((1,3,6,1,4,1,89,219,3))
if mibBuilder.loadTexts:rlSpanSourceTable.setStatus(_A)
_RlSpanSourceEntry_Object=MibTableRow
rlSpanSourceEntry=_RlSpanSourceEntry_Object((1,3,6,1,4,1,89,219,3,1))
rlSpanSourceEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:rlSpanSourceEntry.setStatus(_A)
_RlSpanSourceSessionId_Type=Integer32
_RlSpanSourceSessionId_Object=MibTableColumn
rlSpanSourceSessionId=_RlSpanSourceSessionId_Object((1,3,6,1,4,1,89,219,3,1,1),_RlSpanSourceSessionId_Type())
rlSpanSourceSessionId.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpanSourceSessionId.setStatus(_A)
_RlSpanSourceType_Type=SpanSourceType
_RlSpanSourceType_Object=MibTableColumn
rlSpanSourceType=_RlSpanSourceType_Object((1,3,6,1,4,1,89,219,3,1,2),_RlSpanSourceType_Type())
rlSpanSourceType.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpanSourceType.setStatus(_A)
_RlSpanSourceIndex_Type=Integer32
_RlSpanSourceIndex_Object=MibTableColumn
rlSpanSourceIndex=_RlSpanSourceIndex_Object((1,3,6,1,4,1,89,219,3,1,3),_RlSpanSourceIndex_Type())
rlSpanSourceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rlSpanSourceIndex.setStatus(_A)
_RlSpanSourceDirection_Type=SpanSourceDirection
_RlSpanSourceDirection_Object=MibTableColumn
rlSpanSourceDirection=_RlSpanSourceDirection_Object((1,3,6,1,4,1,89,219,3,1,4),_RlSpanSourceDirection_Type())
rlSpanSourceDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanSourceDirection.setStatus(_A)
_RlSpanSourceRowStatus_Type=RowStatus
_RlSpanSourceRowStatus_Object=MibTableColumn
rlSpanSourceRowStatus=_RlSpanSourceRowStatus_Object((1,3,6,1,4,1,89,219,3,1,5),_RlSpanSourceRowStatus_Type())
rlSpanSourceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSpanSourceRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SpanDestinationPortType':SpanDestinationPortType,'SpanSourceType':SpanSourceType,'SpanSourceDirection':SpanSourceDirection,'rlSpan':rlSpan,'rlSpanMibVersion':rlSpanMibVersion,'rlSpanDestinationTable':rlSpanDestinationTable,'rlSpanDestinationEntry':rlSpanDestinationEntry,_E:rlSpanDestinationSessionId,'rlSpanDestinationIfIndex':rlSpanDestinationIfIndex,'rlSpanDestinationIsReflector':rlSpanDestinationIsReflector,'rlSpanDestinationPortType':rlSpanDestinationPortType,'rlSpanDestinationRowStatus':rlSpanDestinationRowStatus,'rlSpanSourceTable':rlSpanSourceTable,'rlSpanSourceEntry':rlSpanSourceEntry,_F:rlSpanSourceSessionId,_G:rlSpanSourceType,_H:rlSpanSourceIndex,'rlSpanSourceDirection':rlSpanSourceDirection,'rlSpanSourceRowStatus':rlSpanSourceRowStatus})