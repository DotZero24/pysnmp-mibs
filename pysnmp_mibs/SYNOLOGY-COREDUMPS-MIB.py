_H='synologyCoredumpGroup'
_G='coredumpTimestamp'
_F='coredumpFilePath'
_E='read-only'
_D='coredumpInfoIndex'
_C='Integer32'
_B='SYNOLOGY-COREDUMPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyCoredump=ModuleIdentity((1,3,6,1,4,1,6574,201))
if mibBuilder.loadTexts:synologyCoredump.setRevisions(('2016-05-24 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_CoredumpTable_Object=MibTable
coredumpTable=_CoredumpTable_Object((1,3,6,1,4,1,6574,201,1))
if mibBuilder.loadTexts:coredumpTable.setStatus(_A)
_CoredumpEntry_Object=MibTableRow
coredumpEntry=_CoredumpEntry_Object((1,3,6,1,4,1,6574,201,1,1))
coredumpEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:coredumpEntry.setStatus(_A)
class _CoredumpInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CoredumpInfoIndex_Type.__name__=_C
_CoredumpInfoIndex_Object=MibTableColumn
coredumpInfoIndex=_CoredumpInfoIndex_Object((1,3,6,1,4,1,6574,201,1,1,1),_CoredumpInfoIndex_Type())
coredumpInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coredumpInfoIndex.setStatus(_A)
_CoredumpFilePath_Type=OctetString
_CoredumpFilePath_Object=MibTableColumn
coredumpFilePath=_CoredumpFilePath_Object((1,3,6,1,4,1,6574,201,1,1,2),_CoredumpFilePath_Type())
coredumpFilePath.setMaxAccess(_E)
if mibBuilder.loadTexts:coredumpFilePath.setStatus(_A)
_CoredumpTimestamp_Type=Integer32
_CoredumpTimestamp_Object=MibTableColumn
coredumpTimestamp=_CoredumpTimestamp_Object((1,3,6,1,4,1,6574,201,1,1,3),_CoredumpTimestamp_Type())
coredumpTimestamp.setMaxAccess(_E)
if mibBuilder.loadTexts:coredumpTimestamp.setStatus(_A)
_SynologyCoredumpConformance_ObjectIdentity=ObjectIdentity
synologyCoredumpConformance=_SynologyCoredumpConformance_ObjectIdentity((1,3,6,1,4,1,6574,201,2))
_SynologyCoredumpCompliances_ObjectIdentity=ObjectIdentity
synologyCoredumpCompliances=_SynologyCoredumpCompliances_ObjectIdentity((1,3,6,1,4,1,6574,201,2,1))
_SynologyCoredumpGroups_ObjectIdentity=ObjectIdentity
synologyCoredumpGroups=_SynologyCoredumpGroups_ObjectIdentity((1,3,6,1,4,1,6574,201,2,2))
synologyCoredumpGroup=ObjectGroup((1,3,6,1,4,1,6574,201,2,2,1))
synologyCoredumpGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:synologyCoredumpGroup.setStatus(_A)
synologyCoredumpCompliance=ModuleCompliance((1,3,6,1,4,1,6574,201,2,1,1))
synologyCoredumpCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:synologyCoredumpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyCoredump':synologyCoredump,'coredumpTable':coredumpTable,'coredumpEntry':coredumpEntry,_D:coredumpInfoIndex,_F:coredumpFilePath,_G:coredumpTimestamp,'synologyCoredumpConformance':synologyCoredumpConformance,'synologyCoredumpCompliances':synologyCoredumpCompliances,'synologyCoredumpCompliance':synologyCoredumpCompliance,'synologyCoredumpGroups':synologyCoredumpGroups,_H:synologyCoredumpGroup})