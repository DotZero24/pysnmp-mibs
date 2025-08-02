_G='read-write'
_F='read-only'
_E='TruthValue'
_D='Integer32'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
rlSmon=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,84))
if mibBuilder.loadTexts:rlSmon.setRevisions(('2007-01-02 00:00',))
class CopyModeType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('monitor-only',1),('network',2)))
_RlPortCopyMibVersion_Type=Integer32
_RlPortCopyMibVersion_Object=MibScalar
rlPortCopyMibVersion=_RlPortCopyMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,84,1),_RlPortCopyMibVersion_Type())
rlPortCopyMibVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPortCopyMibVersion.setStatus(_A)
class _RlPortCopySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('notSupported',2)))
_RlPortCopySupport_Type.__name__=_D
_RlPortCopySupport_Object=MibScalar
rlPortCopySupport=_RlPortCopySupport_Object((1,3,6,1,4,1,259,10,1,14,89,84,2),_RlPortCopySupport_Type())
rlPortCopySupport.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPortCopySupport.setStatus(_A)
_RlPortCopyVlanTaggingTable_Object=MibTable
rlPortCopyVlanTaggingTable=_RlPortCopyVlanTaggingTable_Object((1,3,6,1,4,1,259,10,1,14,89,84,3))
if mibBuilder.loadTexts:rlPortCopyVlanTaggingTable.setStatus(_A)
_RlPortCopyVlanTaggingEntry_Object=MibTableRow
rlPortCopyVlanTaggingEntry=_RlPortCopyVlanTaggingEntry_Object((1,3,6,1,4,1,259,10,1,14,89,84,3,1))
rlPortCopyVlanTaggingEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rlPortCopyVlanTaggingEntry.setStatus(_A)
class _RlPortCopyVlanTagging_Type(TruthValue):defaultValue=1
_RlPortCopyVlanTagging_Type.__name__=_E
_RlPortCopyVlanTagging_Object=MibTableColumn
rlPortCopyVlanTagging=_RlPortCopyVlanTagging_Object((1,3,6,1,4,1,259,10,1,14,89,84,3,1,1),_RlPortCopyVlanTagging_Type())
rlPortCopyVlanTagging.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPortCopyVlanTagging.setStatus(_A)
_RlPortCopyMode_Type=CopyModeType
_RlPortCopyMode_Object=MibScalar
rlPortCopyMode=_RlPortCopyMode_Object((1,3,6,1,4,1,259,10,1,14,89,84,4),_RlPortCopyMode_Type())
rlPortCopyMode.setMaxAccess(_G)
if mibBuilder.loadTexts:rlPortCopyMode.setStatus(_A)
mibBuilder.exportSymbols('EDGECORE-SMON-MIB',**{'CopyModeType':CopyModeType,'rlSmon':rlSmon,'rlPortCopyMibVersion':rlPortCopyMibVersion,'rlPortCopySupport':rlPortCopySupport,'rlPortCopyVlanTaggingTable':rlPortCopyVlanTaggingTable,'rlPortCopyVlanTaggingEntry':rlPortCopyVlanTaggingEntry,'rlPortCopyVlanTagging':rlPortCopyVlanTagging,'rlPortCopyMode':rlPortCopyMode})