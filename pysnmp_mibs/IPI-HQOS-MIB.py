_H='not-accessible'
_G='hqosCmapId'
_F='hqosDirection'
_E='ifIndex'
_D='IF-MIB'
_C='IPI-HQOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipiHqosMib=ModuleIdentity((1,3,6,1,4,1,36673,107))
_IpiHqosTable_ObjectIdentity=ObjectIdentity
ipiHqosTable=_IpiHqosTable_ObjectIdentity((1,3,6,1,4,1,36673,107,1))
_IpiHqosCmapTable_Object=MibTable
ipiHqosCmapTable=_IpiHqosCmapTable_Object((1,3,6,1,4,1,36673,107,1,1))
if mibBuilder.loadTexts:ipiHqosCmapTable.setStatus(_A)
_IpiHqosCmapEntry_Object=MibTableRow
ipiHqosCmapEntry=_IpiHqosCmapEntry_Object((1,3,6,1,4,1,36673,107,1,1,1))
ipiHqosCmapEntry.setIndexNames((0,_D,_E),(0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ipiHqosCmapEntry.setStatus(_A)
_HqosDirection_Type=Unsigned32
_HqosDirection_Object=MibTableColumn
hqosDirection=_HqosDirection_Object((1,3,6,1,4,1,36673,107,1,1,1,1),_HqosDirection_Type())
hqosDirection.setMaxAccess(_H)
if mibBuilder.loadTexts:hqosDirection.setStatus(_A)
_HqosCmapId_Type=Unsigned32
_HqosCmapId_Object=MibTableColumn
hqosCmapId=_HqosCmapId_Object((1,3,6,1,4,1,36673,107,1,1,1,2),_HqosCmapId_Type())
hqosCmapId.setMaxAccess(_H)
if mibBuilder.loadTexts:hqosCmapId.setStatus(_A)
_HqosCmapMatchPkts_Type=Counter64
_HqosCmapMatchPkts_Object=MibTableColumn
hqosCmapMatchPkts=_HqosCmapMatchPkts_Object((1,3,6,1,4,1,36673,107,1,1,1,3),_HqosCmapMatchPkts_Type())
hqosCmapMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosCmapMatchPkts.setStatus(_A)
_HqosCmapMatchBytes_Type=Counter64
_HqosCmapMatchBytes_Object=MibTableColumn
hqosCmapMatchBytes=_HqosCmapMatchBytes_Object((1,3,6,1,4,1,36673,107,1,1,1,4),_HqosCmapMatchBytes_Type())
hqosCmapMatchBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosCmapMatchBytes.setStatus(_A)
_HqosCmapDropPkts_Type=Counter64
_HqosCmapDropPkts_Object=MibTableColumn
hqosCmapDropPkts=_HqosCmapDropPkts_Object((1,3,6,1,4,1,36673,107,1,1,1,5),_HqosCmapDropPkts_Type())
hqosCmapDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosCmapDropPkts.setStatus(_A)
_HqosCmapDropBytes_Type=Counter64
_HqosCmapDropBytes_Object=MibTableColumn
hqosCmapDropBytes=_HqosCmapDropBytes_Object((1,3,6,1,4,1,36673,107,1,1,1,6),_HqosCmapDropBytes_Type())
hqosCmapDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hqosCmapDropBytes.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ipiHqosMib':ipiHqosMib,'ipiHqosTable':ipiHqosTable,'ipiHqosCmapTable':ipiHqosCmapTable,'ipiHqosCmapEntry':ipiHqosCmapEntry,_F:hqosDirection,_G:hqosCmapId,'hqosCmapMatchPkts':hqosCmapMatchPkts,'hqosCmapMatchBytes':hqosCmapMatchBytes,'hqosCmapDropPkts':hqosCmapDropPkts,'hqosCmapDropBytes':hqosCmapDropBytes})