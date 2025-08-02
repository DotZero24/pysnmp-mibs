_D='read-create'
_C='protocolsProtocolName'
_B='FUJITSU-PROTOCOLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fssProtocols,=mibBuilder.importSymbols('FSS-COMMON-SMI','fssProtocols')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fUJITSU_PROTOCOLS_MIB=ModuleIdentity((1,3,6,1,4,1,211,1,24,12,1100,1000))
if mibBuilder.loadTexts:fUJITSU_PROTOCOLS_MIB.setRevisions(('2016-04-01 00:00',))
class ConfdString(TextualConvention,OctetString):status=_A;displayHint='1t'
class String(TextualConvention,OctetString):status=_A;displayHint='1t'
_Protocols_ObjectIdentity=ObjectIdentity
protocols=_Protocols_ObjectIdentity((1,3,6,1,4,1,211,1,24,12,1100,1000,1))
_ProtocolsProtocolTable_Object=MibTable
protocolsProtocolTable=_ProtocolsProtocolTable_Object((1,3,6,1,4,1,211,1,24,12,1100,1000,1,1))
if mibBuilder.loadTexts:protocolsProtocolTable.setStatus(_A)
_ProtocolsProtocolEntry_Object=MibTableRow
protocolsProtocolEntry=_ProtocolsProtocolEntry_Object((1,3,6,1,4,1,211,1,24,12,1100,1000,1,1,1))
protocolsProtocolEntry.setIndexNames((1,_B,_C))
if mibBuilder.loadTexts:protocolsProtocolEntry.setStatus(_A)
_ProtocolsProtocolName_Type=String
_ProtocolsProtocolName_Object=MibTableColumn
protocolsProtocolName=_ProtocolsProtocolName_Object((1,3,6,1,4,1,211,1,24,12,1100,1000,1,1,1,1),_ProtocolsProtocolName_Type())
protocolsProtocolName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:protocolsProtocolName.setStatus(_A)
_ProtocolsProtocolType_Type=ConfdString
_ProtocolsProtocolType_Object=MibTableColumn
protocolsProtocolType=_ProtocolsProtocolType_Object((1,3,6,1,4,1,211,1,24,12,1100,1000,1,1,1,2),_ProtocolsProtocolType_Type())
protocolsProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:protocolsProtocolType.setStatus(_A)
_ProtocolsProtocolRowstatus_Type=RowStatus
_ProtocolsProtocolRowstatus_Object=MibTableColumn
protocolsProtocolRowstatus=_ProtocolsProtocolRowstatus_Object((1,3,6,1,4,1,211,1,24,12,1100,1000,1,1,1,3),_ProtocolsProtocolRowstatus_Type())
protocolsProtocolRowstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:protocolsProtocolRowstatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfdString':ConfdString,'String':String,'fUJITSU-PROTOCOLS-MIB':fUJITSU_PROTOCOLS_MIB,'protocols':protocols,'protocolsProtocolTable':protocolsProtocolTable,'protocolsProtocolEntry':protocolsProtocolEntry,_C:protocolsProtocolName,'protocolsProtocolType':protocolsProtocolType,'protocolsProtocolRowstatus':protocolsProtocolRowstatus})