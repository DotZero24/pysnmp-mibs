_E='swCPUProtectProtocolType'
_D='CPU-PROTECT-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
swCPUProtectMIB=ModuleIdentity((1,3,6,1,4,1,171,12,106))
_SwCPUProtectGlobalMgmt_ObjectIdentity=ObjectIdentity
swCPUProtectGlobalMgmt=_SwCPUProtectGlobalMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,106,1))
class _SwCPUProtectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwCPUProtectState_Type.__name__=_B
_SwCPUProtectState_Object=MibScalar
swCPUProtectState=_SwCPUProtectState_Object((1,3,6,1,4,1,171,12,106,1,1),_SwCPUProtectState_Type())
swCPUProtectState.setMaxAccess(_C)
if mibBuilder.loadTexts:swCPUProtectState.setStatus(_A)
_SwCPUProtectProtocolTable_Object=MibTable
swCPUProtectProtocolTable=_SwCPUProtectProtocolTable_Object((1,3,6,1,4,1,171,12,106,2))
if mibBuilder.loadTexts:swCPUProtectProtocolTable.setStatus(_A)
_SwCPUProtectProtocolEntry_Object=MibTableRow
swCPUProtectProtocolEntry=_SwCPUProtectProtocolEntry_Object((1,3,6,1,4,1,171,12,106,2,1))
swCPUProtectProtocolEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swCPUProtectProtocolEntry.setStatus(_A)
class _SwCPUProtectProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('arp',1),('bpdu',2),('icmp',3),('igmp',4),('snmp',5)))
_SwCPUProtectProtocolType_Type.__name__=_B
_SwCPUProtectProtocolType_Object=MibTableColumn
swCPUProtectProtocolType=_SwCPUProtectProtocolType_Object((1,3,6,1,4,1,171,12,106,2,1,1),_SwCPUProtectProtocolType_Type())
swCPUProtectProtocolType.setMaxAccess('read-only')
if mibBuilder.loadTexts:swCPUProtectProtocolType.setStatus(_A)
_SwCPUProtectProtocolRate_Type=Integer32
_SwCPUProtectProtocolRate_Object=MibTableColumn
swCPUProtectProtocolRate=_SwCPUProtectProtocolRate_Object((1,3,6,1,4,1,171,12,106,2,1,2),_SwCPUProtectProtocolRate_Type())
swCPUProtectProtocolRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swCPUProtectProtocolRate.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swCPUProtectMIB':swCPUProtectMIB,'swCPUProtectGlobalMgmt':swCPUProtectGlobalMgmt,'swCPUProtectState':swCPUProtectState,'swCPUProtectProtocolTable':swCPUProtectProtocolTable,'swCPUProtectProtocolEntry':swCPUProtectProtocolEntry,_E:swCPUProtectProtocolType,'swCPUProtectProtocolRate':swCPUProtectProtocolRate})