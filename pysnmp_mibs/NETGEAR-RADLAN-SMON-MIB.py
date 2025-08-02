_G='read-only'
_F='Integer32'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='read-write'
_B='TruthValue'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_B)
rlSmon=ModuleIdentity((1,3,6,1,4,1,4526,17,84))
if mibBuilder.loadTexts:rlSmon.setRevisions(('2007-01-02 00:00',))
class CopyModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('monitor-only',1),('network',2)))
_RlPortCopyMibVersion_Type=Integer32
_RlPortCopyMibVersion_Object=MibScalar
rlPortCopyMibVersion=_RlPortCopyMibVersion_Object((1,3,6,1,4,1,4526,17,84,1),_RlPortCopyMibVersion_Type())
rlPortCopyMibVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPortCopyMibVersion.setStatus(_A)
class _RlPortCopySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('notSupported',2)))
_RlPortCopySupport_Type.__name__=_F
_RlPortCopySupport_Object=MibScalar
rlPortCopySupport=_RlPortCopySupport_Object((1,3,6,1,4,1,4526,17,84,2),_RlPortCopySupport_Type())
rlPortCopySupport.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPortCopySupport.setStatus(_A)
_RlPortCopyVlanTaggingTable_Object=MibTable
rlPortCopyVlanTaggingTable=_RlPortCopyVlanTaggingTable_Object((1,3,6,1,4,1,4526,17,84,3))
if mibBuilder.loadTexts:rlPortCopyVlanTaggingTable.setStatus(_A)
_RlPortCopyVlanTaggingEntry_Object=MibTableRow
rlPortCopyVlanTaggingEntry=_RlPortCopyVlanTaggingEntry_Object((1,3,6,1,4,1,4526,17,84,3,1))
rlPortCopyVlanTaggingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortCopyVlanTaggingEntry.setStatus(_A)
class _RlPortCopyVlanTagging_Type(TruthValue):defaultValue=2
_RlPortCopyVlanTagging_Type.__name__=_B
_RlPortCopyVlanTagging_Object=MibTableColumn
rlPortCopyVlanTagging=_RlPortCopyVlanTagging_Object((1,3,6,1,4,1,4526,17,84,3,1,1),_RlPortCopyVlanTagging_Type())
rlPortCopyVlanTagging.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortCopyVlanTagging.setStatus(_A)
_RlPortCopyMode_Type=CopyModeType
_RlPortCopyMode_Object=MibScalar
rlPortCopyMode=_RlPortCopyMode_Object((1,3,6,1,4,1,4526,17,84,4),_RlPortCopyMode_Type())
rlPortCopyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortCopyMode.setStatus(_A)
class _RlPortCopySessionsEnabled_Type(TruthValue):defaultValue=1
_RlPortCopySessionsEnabled_Type.__name__=_B
_RlPortCopySessionsEnabled_Object=MibScalar
rlPortCopySessionsEnabled=_RlPortCopySessionsEnabled_Object((1,3,6,1,4,1,4526,17,84,5),_RlPortCopySessionsEnabled_Type())
rlPortCopySessionsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortCopySessionsEnabled.setStatus(_A)
mibBuilder.exportSymbols('NETGEAR-RADLAN-SMON-MIB',**{'CopyModeType':CopyModeType,'rlSmon':rlSmon,'rlPortCopyMibVersion':rlPortCopyMibVersion,'rlPortCopySupport':rlPortCopySupport,'rlPortCopyVlanTaggingTable':rlPortCopyVlanTaggingTable,'rlPortCopyVlanTaggingEntry':rlPortCopyVlanTaggingEntry,'rlPortCopyVlanTagging':rlPortCopyVlanTagging,'rlPortCopyMode':rlPortCopyMode,'rlPortCopySessionsEnabled':rlPortCopySessionsEnabled})