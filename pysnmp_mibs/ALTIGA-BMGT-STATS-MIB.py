_R='alBwMgmtStatsGroup'
_Q='alBwMgmtStatOutDroppedBytes'
_P='alBwMgmtStatOutConformedBytes'
_O='alBwMgmtStatOutDroppedRate'
_N='alBwMgmtStatOutConformedRate'
_M='alBwMgmtStatInDroppedBytes'
_L='alBwMgmtStatInConformedBytes'
_K='alBwMgmtStatInDroppedRate'
_J='alBwMgmtStatInConformedRate'
_I='alBwMgmtStatGrpId'
_H='alBwMgmtStatRowStatus'
_G='alBwMgmtStatIntfId'
_F='Integer32'
_E='bytes'
_D='kbytes'
_C='read-only'
_B='ALTIGA-BMGT-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alBwMgmtMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alBwMgmtMibModule')
alBwMgmtGroup,alStatsBwMgmt=mibBuilder.importSymbols('ALTIGA-MIB','alBwMgmtGroup','alStatsBwMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaBwMgmMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,52,2))
if mibBuilder.loadTexts:altigaBwMgmMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaBwMgmMibConformance_ObjectIdentity=ObjectIdentity
altigaBwMgmMibConformance=_AltigaBwMgmMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,52,2,1))
_AltigaBwMgmMibCompliances_ObjectIdentity=ObjectIdentity
altigaBwMgmMibCompliances=_AltigaBwMgmMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,52,2,1,1))
_AlBwMgmtStatsGlobal_ObjectIdentity=ObjectIdentity
alBwMgmtStatsGlobal=_AlBwMgmtStatsGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,47,1))
_AlBwMgmtStatTable_Object=MibTable
alBwMgmtStatTable=_AlBwMgmtStatTable_Object((1,3,6,1,4,1,3076,2,1,2,47,2))
if mibBuilder.loadTexts:alBwMgmtStatTable.setStatus(_A)
_AlBwMgmtStatEntry_Object=MibTableRow
alBwMgmtStatEntry=_AlBwMgmtStatEntry_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1))
alBwMgmtStatEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:alBwMgmtStatEntry.setStatus(_A)
_AlBwMgmtStatRowStatus_Type=RowStatus
_AlBwMgmtStatRowStatus_Object=MibTableColumn
alBwMgmtStatRowStatus=_AlBwMgmtStatRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,1),_AlBwMgmtStatRowStatus_Type())
alBwMgmtStatRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatRowStatus.setStatus(_A)
class _AlBwMgmtStatIntfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AlBwMgmtStatIntfId_Type.__name__=_F
_AlBwMgmtStatIntfId_Object=MibTableColumn
alBwMgmtStatIntfId=_AlBwMgmtStatIntfId_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,2),_AlBwMgmtStatIntfId_Type())
alBwMgmtStatIntfId.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatIntfId.setStatus(_A)
class _AlBwMgmtStatGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AlBwMgmtStatGrpId_Type.__name__=_F
_AlBwMgmtStatGrpId_Object=MibTableColumn
alBwMgmtStatGrpId=_AlBwMgmtStatGrpId_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,3),_AlBwMgmtStatGrpId_Type())
alBwMgmtStatGrpId.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatGrpId.setStatus(_A)
_AlBwMgmtStatInConformedRate_Type=Unsigned32
_AlBwMgmtStatInConformedRate_Object=MibTableColumn
alBwMgmtStatInConformedRate=_AlBwMgmtStatInConformedRate_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,4),_AlBwMgmtStatInConformedRate_Type())
alBwMgmtStatInConformedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatInConformedRate.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatInConformedRate.setUnits(_D)
_AlBwMgmtStatInDroppedRate_Type=Unsigned32
_AlBwMgmtStatInDroppedRate_Object=MibTableColumn
alBwMgmtStatInDroppedRate=_AlBwMgmtStatInDroppedRate_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,5),_AlBwMgmtStatInDroppedRate_Type())
alBwMgmtStatInDroppedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatInDroppedRate.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatInDroppedRate.setUnits(_D)
_AlBwMgmtStatInConformedBytes_Type=Counter32
_AlBwMgmtStatInConformedBytes_Object=MibTableColumn
alBwMgmtStatInConformedBytes=_AlBwMgmtStatInConformedBytes_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,6),_AlBwMgmtStatInConformedBytes_Type())
alBwMgmtStatInConformedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatInConformedBytes.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatInConformedBytes.setUnits(_E)
_AlBwMgmtStatInDroppedBytes_Type=Counter32
_AlBwMgmtStatInDroppedBytes_Object=MibTableColumn
alBwMgmtStatInDroppedBytes=_AlBwMgmtStatInDroppedBytes_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,7),_AlBwMgmtStatInDroppedBytes_Type())
alBwMgmtStatInDroppedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatInDroppedBytes.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatInDroppedBytes.setUnits(_E)
_AlBwMgmtStatOutConformedRate_Type=Unsigned32
_AlBwMgmtStatOutConformedRate_Object=MibTableColumn
alBwMgmtStatOutConformedRate=_AlBwMgmtStatOutConformedRate_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,8),_AlBwMgmtStatOutConformedRate_Type())
alBwMgmtStatOutConformedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatOutConformedRate.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatOutConformedRate.setUnits(_D)
_AlBwMgmtStatOutDroppedRate_Type=Unsigned32
_AlBwMgmtStatOutDroppedRate_Object=MibTableColumn
alBwMgmtStatOutDroppedRate=_AlBwMgmtStatOutDroppedRate_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,9),_AlBwMgmtStatOutDroppedRate_Type())
alBwMgmtStatOutDroppedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatOutDroppedRate.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatOutDroppedRate.setUnits(_D)
_AlBwMgmtStatOutConformedBytes_Type=Counter32
_AlBwMgmtStatOutConformedBytes_Object=MibTableColumn
alBwMgmtStatOutConformedBytes=_AlBwMgmtStatOutConformedBytes_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,10),_AlBwMgmtStatOutConformedBytes_Type())
alBwMgmtStatOutConformedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatOutConformedBytes.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatOutConformedBytes.setUnits(_E)
_AlBwMgmtStatOutDroppedBytes_Type=Counter32
_AlBwMgmtStatOutDroppedBytes_Object=MibTableColumn
alBwMgmtStatOutDroppedBytes=_AlBwMgmtStatOutDroppedBytes_Object((1,3,6,1,4,1,3076,2,1,2,47,2,1,11),_AlBwMgmtStatOutDroppedBytes_Type())
alBwMgmtStatOutDroppedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:alBwMgmtStatOutDroppedBytes.setStatus(_A)
if mibBuilder.loadTexts:alBwMgmtStatOutDroppedBytes.setUnits(_E)
alBwMgmtStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,47,2))
alBwMgmtStatsGroup.setObjects(*((_B,_H),(_B,_G),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alBwMgmtStatsGroup.setStatus(_A)
altigaBwMgmMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,52,2,1,1,1))
altigaBwMgmMibCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:altigaBwMgmMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaBwMgmMibModule':altigaBwMgmMibModule,'altigaBwMgmMibConformance':altigaBwMgmMibConformance,'altigaBwMgmMibCompliances':altigaBwMgmMibCompliances,'altigaBwMgmMibCompliance':altigaBwMgmMibCompliance,_R:alBwMgmtStatsGroup,'alBwMgmtStatsGlobal':alBwMgmtStatsGlobal,'alBwMgmtStatTable':alBwMgmtStatTable,'alBwMgmtStatEntry':alBwMgmtStatEntry,_H:alBwMgmtStatRowStatus,_G:alBwMgmtStatIntfId,_I:alBwMgmtStatGrpId,_J:alBwMgmtStatInConformedRate,_K:alBwMgmtStatInDroppedRate,_L:alBwMgmtStatInConformedBytes,_M:alBwMgmtStatInDroppedBytes,_N:alBwMgmtStatOutConformedRate,_O:alBwMgmtStatOutDroppedRate,_P:alBwMgmtStatOutConformedBytes,_Q:alBwMgmtStatOutDroppedBytes})