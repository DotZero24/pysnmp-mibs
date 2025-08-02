_D='atVlanStatCollectionName'
_C='AT-VLAN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
atVlanInfo=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,16))
if mibBuilder.loadTexts:atVlanInfo.setRevisions(('2010-09-07 00:00','2010-06-15 00:15','2009-06-30 00:00'))
_AtVlanStatistics_ObjectIdentity=ObjectIdentity
atVlanStatistics=_AtVlanStatistics_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,16,1))
_AtVlanStatNumCollections_Type=Integer32
_AtVlanStatNumCollections_Object=MibScalar
atVlanStatNumCollections=_AtVlanStatNumCollections_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,1),_AtVlanStatNumCollections_Type())
atVlanStatNumCollections.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatNumCollections.setStatus(_A)
_AtVlanStatCollectionTable_Object=MibTable
atVlanStatCollectionTable=_AtVlanStatCollectionTable_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2))
if mibBuilder.loadTexts:atVlanStatCollectionTable.setStatus(_A)
_AtVlanStatCollectionEntry_Object=MibTableRow
atVlanStatCollectionEntry=_AtVlanStatCollectionEntry_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1))
atVlanStatCollectionEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:atVlanStatCollectionEntry.setStatus(_A)
_AtVlanStatCollectionName_Type=DisplayString
_AtVlanStatCollectionName_Object=MibTableColumn
atVlanStatCollectionName=_AtVlanStatCollectionName_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,1),_AtVlanStatCollectionName_Type())
atVlanStatCollectionName.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatCollectionName.setStatus(_A)
_AtVlanStatCollectionVlanId_Type=Gauge32
_AtVlanStatCollectionVlanId_Object=MibTableColumn
atVlanStatCollectionVlanId=_AtVlanStatCollectionVlanId_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,2),_AtVlanStatCollectionVlanId_Type())
atVlanStatCollectionVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatCollectionVlanId.setStatus(_A)
_AtVlanStatCollectionPortMap_Type=OctetString
_AtVlanStatCollectionPortMap_Object=MibTableColumn
atVlanStatCollectionPortMap=_AtVlanStatCollectionPortMap_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,3),_AtVlanStatCollectionPortMap_Type())
atVlanStatCollectionPortMap.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatCollectionPortMap.setStatus(_A)
_AtVlanStatCollectionIngressPkts_Type=Counter64
_AtVlanStatCollectionIngressPkts_Object=MibTableColumn
atVlanStatCollectionIngressPkts=_AtVlanStatCollectionIngressPkts_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,4),_AtVlanStatCollectionIngressPkts_Type())
atVlanStatCollectionIngressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatCollectionIngressPkts.setStatus(_A)
_AtVlanStatCollectionIngressOctets_Type=Counter64
_AtVlanStatCollectionIngressOctets_Object=MibTableColumn
atVlanStatCollectionIngressOctets=_AtVlanStatCollectionIngressOctets_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,5),_AtVlanStatCollectionIngressOctets_Type())
atVlanStatCollectionIngressOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:atVlanStatCollectionIngressOctets.setStatus(_A)
_AtVlanStatCollectionResetStats_Type=TruthValue
_AtVlanStatCollectionResetStats_Object=MibTableColumn
atVlanStatCollectionResetStats=_AtVlanStatCollectionResetStats_Object((1,3,6,1,4,1,207,8,4,4,3,16,1,2,1,6),_AtVlanStatCollectionResetStats_Type())
atVlanStatCollectionResetStats.setMaxAccess('read-write')
if mibBuilder.loadTexts:atVlanStatCollectionResetStats.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'atVlanInfo':atVlanInfo,'atVlanStatistics':atVlanStatistics,'atVlanStatNumCollections':atVlanStatNumCollections,'atVlanStatCollectionTable':atVlanStatCollectionTable,'atVlanStatCollectionEntry':atVlanStatCollectionEntry,_D:atVlanStatCollectionName,'atVlanStatCollectionVlanId':atVlanStatCollectionVlanId,'atVlanStatCollectionPortMap':atVlanStatCollectionPortMap,'atVlanStatCollectionIngressPkts':atVlanStatCollectionIngressPkts,'atVlanStatCollectionIngressOctets':atVlanStatCollectionIngressOctets,'atVlanStatCollectionResetStats':atVlanStatCollectionResetStats})