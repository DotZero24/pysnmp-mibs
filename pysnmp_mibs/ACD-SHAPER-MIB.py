_Z='acdShaper1CodePointStatsGroup'
_Y='acdShaper1CodePointStatsQMgmtDropRate'
_X='acdShaper1CodePointStatsQMgmtDropPkts'
_W='acdShaper1CodePointStatsQMgmtDropOctets'
_V='acdShaper1CodePointStatsOverflowRate'
_U='acdShaper1CodePointStatsOverflowPkts'
_T='acdShaper1CodePointStatsOverflowOctets'
_S='acdShaper1CodePointStatsDelayedRate'
_R='acdShaper1CodePointStatsDelayedPkts'
_Q='acdShaper1CodePointStatsDelayedOctets'
_P='acdShaper1CodePointStatsFwdRate'
_O='acdShaper1CodePointStatsFwdPkts'
_N='acdShaper1CodePointStatsFwdOctets'
_M='acdShaper1CodePointStatsPcpID'
_L='acdShaper1CodePointStatsColorID'
_K='acdShaper1CodePointStatsSrcID'
_J='acdShaper1CodePointStatsDstID'
_I='Integer32'
_H='Mbps'
_G='Packets'
_F='Octets'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='ACD-SHAPER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
acdShaper=ModuleIdentity((1,3,6,1,4,1,22420,2,10))
if mibBuilder.loadTexts:acdShaper.setRevisions(('2009-11-01 01:00',))
_AcdShaper1_ObjectIdentity=ObjectIdentity
acdShaper1=_AcdShaper1_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1))
_AcdShaper1MIBObjects_ObjectIdentity=ObjectIdentity
acdShaper1MIBObjects=_AcdShaper1MIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,1))
_AcdShaper1Config_ObjectIdentity=ObjectIdentity
acdShaper1Config=_AcdShaper1Config_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,1,1))
_AcdShaper1Stats_ObjectIdentity=ObjectIdentity
acdShaper1Stats=_AcdShaper1Stats_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,1,2))
_AcdShaper1CodePointStatsTable_Object=MibTable
acdShaper1CodePointStatsTable=_AcdShaper1CodePointStatsTable_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1))
if mibBuilder.loadTexts:acdShaper1CodePointStatsTable.setStatus(_A)
_AcdShaper1CodePointStatsEntry_Object=MibTableRow
acdShaper1CodePointStatsEntry=_AcdShaper1CodePointStatsEntry_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1))
acdShaper1CodePointStatsEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:acdShaper1CodePointStatsEntry.setStatus(_A)
class _AcdShaper1CodePointStatsDstID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AcdShaper1CodePointStatsDstID_Type.__name__=_D
_AcdShaper1CodePointStatsDstID_Object=MibTableColumn
acdShaper1CodePointStatsDstID=_AcdShaper1CodePointStatsDstID_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,1),_AcdShaper1CodePointStatsDstID_Type())
acdShaper1CodePointStatsDstID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDstID.setStatus(_A)
class _AcdShaper1CodePointStatsSrcID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AcdShaper1CodePointStatsSrcID_Type.__name__=_D
_AcdShaper1CodePointStatsSrcID_Object=MibTableColumn
acdShaper1CodePointStatsSrcID=_AcdShaper1CodePointStatsSrcID_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,2),_AcdShaper1CodePointStatsSrcID_Type())
acdShaper1CodePointStatsSrcID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdShaper1CodePointStatsSrcID.setStatus(_A)
class _AcdShaper1CodePointStatsColorID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('green',1),('yellow',2)))
_AcdShaper1CodePointStatsColorID_Type.__name__=_I
_AcdShaper1CodePointStatsColorID_Object=MibTableColumn
acdShaper1CodePointStatsColorID=_AcdShaper1CodePointStatsColorID_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,3),_AcdShaper1CodePointStatsColorID_Type())
acdShaper1CodePointStatsColorID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdShaper1CodePointStatsColorID.setStatus(_A)
class _AcdShaper1CodePointStatsPcpID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcdShaper1CodePointStatsPcpID_Type.__name__=_D
_AcdShaper1CodePointStatsPcpID_Object=MibTableColumn
acdShaper1CodePointStatsPcpID=_AcdShaper1CodePointStatsPcpID_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,4),_AcdShaper1CodePointStatsPcpID_Type())
acdShaper1CodePointStatsPcpID.setMaxAccess(_E)
if mibBuilder.loadTexts:acdShaper1CodePointStatsPcpID.setStatus(_A)
_AcdShaper1CodePointStatsFwdOctets_Type=Counter64
_AcdShaper1CodePointStatsFwdOctets_Object=MibTableColumn
acdShaper1CodePointStatsFwdOctets=_AcdShaper1CodePointStatsFwdOctets_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,5),_AcdShaper1CodePointStatsFwdOctets_Type())
acdShaper1CodePointStatsFwdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdOctets.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdOctets.setUnits(_F)
_AcdShaper1CodePointStatsFwdPkts_Type=Counter64
_AcdShaper1CodePointStatsFwdPkts_Object=MibTableColumn
acdShaper1CodePointStatsFwdPkts=_AcdShaper1CodePointStatsFwdPkts_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,6),_AcdShaper1CodePointStatsFwdPkts_Type())
acdShaper1CodePointStatsFwdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdPkts.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdPkts.setUnits(_G)
_AcdShaper1CodePointStatsFwdRate_Type=Gauge32
_AcdShaper1CodePointStatsFwdRate_Object=MibTableColumn
acdShaper1CodePointStatsFwdRate=_AcdShaper1CodePointStatsFwdRate_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,7),_AcdShaper1CodePointStatsFwdRate_Type())
acdShaper1CodePointStatsFwdRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdRate.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsFwdRate.setUnits(_H)
_AcdShaper1CodePointStatsDelayedOctets_Type=Counter64
_AcdShaper1CodePointStatsDelayedOctets_Object=MibTableColumn
acdShaper1CodePointStatsDelayedOctets=_AcdShaper1CodePointStatsDelayedOctets_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,8),_AcdShaper1CodePointStatsDelayedOctets_Type())
acdShaper1CodePointStatsDelayedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedOctets.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedOctets.setUnits(_F)
_AcdShaper1CodePointStatsDelayedPkts_Type=Counter64
_AcdShaper1CodePointStatsDelayedPkts_Object=MibTableColumn
acdShaper1CodePointStatsDelayedPkts=_AcdShaper1CodePointStatsDelayedPkts_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,9),_AcdShaper1CodePointStatsDelayedPkts_Type())
acdShaper1CodePointStatsDelayedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedPkts.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedPkts.setUnits(_G)
_AcdShaper1CodePointStatsDelayedRate_Type=Gauge32
_AcdShaper1CodePointStatsDelayedRate_Object=MibTableColumn
acdShaper1CodePointStatsDelayedRate=_AcdShaper1CodePointStatsDelayedRate_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,10),_AcdShaper1CodePointStatsDelayedRate_Type())
acdShaper1CodePointStatsDelayedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedRate.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsDelayedRate.setUnits(_H)
_AcdShaper1CodePointStatsOverflowOctets_Type=Counter64
_AcdShaper1CodePointStatsOverflowOctets_Object=MibTableColumn
acdShaper1CodePointStatsOverflowOctets=_AcdShaper1CodePointStatsOverflowOctets_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,11),_AcdShaper1CodePointStatsOverflowOctets_Type())
acdShaper1CodePointStatsOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowOctets.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowOctets.setUnits(_F)
_AcdShaper1CodePointStatsOverflowPkts_Type=Counter64
_AcdShaper1CodePointStatsOverflowPkts_Object=MibTableColumn
acdShaper1CodePointStatsOverflowPkts=_AcdShaper1CodePointStatsOverflowPkts_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,12),_AcdShaper1CodePointStatsOverflowPkts_Type())
acdShaper1CodePointStatsOverflowPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowPkts.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowPkts.setUnits(_G)
_AcdShaper1CodePointStatsOverflowRate_Type=Gauge32
_AcdShaper1CodePointStatsOverflowRate_Object=MibTableColumn
acdShaper1CodePointStatsOverflowRate=_AcdShaper1CodePointStatsOverflowRate_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,13),_AcdShaper1CodePointStatsOverflowRate_Type())
acdShaper1CodePointStatsOverflowRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowRate.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsOverflowRate.setUnits(_H)
_AcdShaper1CodePointStatsQMgmtDropOctets_Type=Counter64
_AcdShaper1CodePointStatsQMgmtDropOctets_Object=MibTableColumn
acdShaper1CodePointStatsQMgmtDropOctets=_AcdShaper1CodePointStatsQMgmtDropOctets_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,14),_AcdShaper1CodePointStatsQMgmtDropOctets_Type())
acdShaper1CodePointStatsQMgmtDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropOctets.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropOctets.setUnits(_F)
_AcdShaper1CodePointStatsQMgmtDropPkts_Type=Counter64
_AcdShaper1CodePointStatsQMgmtDropPkts_Object=MibTableColumn
acdShaper1CodePointStatsQMgmtDropPkts=_AcdShaper1CodePointStatsQMgmtDropPkts_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,15),_AcdShaper1CodePointStatsQMgmtDropPkts_Type())
acdShaper1CodePointStatsQMgmtDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropPkts.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropPkts.setUnits(_G)
_AcdShaper1CodePointStatsQMgmtDropRate_Type=Gauge32
_AcdShaper1CodePointStatsQMgmtDropRate_Object=MibTableColumn
acdShaper1CodePointStatsQMgmtDropRate=_AcdShaper1CodePointStatsQMgmtDropRate_Object((1,3,6,1,4,1,22420,2,10,1,1,2,1,1,16),_AcdShaper1CodePointStatsQMgmtDropRate_Type())
acdShaper1CodePointStatsQMgmtDropRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropRate.setStatus(_A)
if mibBuilder.loadTexts:acdShaper1CodePointStatsQMgmtDropRate.setUnits(_H)
_AcdShaper1Conformance_ObjectIdentity=ObjectIdentity
acdShaper1Conformance=_AcdShaper1Conformance_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,2))
_AcdShaper1Compliances_ObjectIdentity=ObjectIdentity
acdShaper1Compliances=_AcdShaper1Compliances_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,2,1))
_AcdShaper1Groups_ObjectIdentity=ObjectIdentity
acdShaper1Groups=_AcdShaper1Groups_ObjectIdentity((1,3,6,1,4,1,22420,2,10,1,2,2))
acdShaper1CodePointStatsGroup=ObjectGroup((1,3,6,1,4,1,22420,2,10,1,2,2,1))
acdShaper1CodePointStatsGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:acdShaper1CodePointStatsGroup.setStatus(_A)
acdShaper1Compliance=ModuleCompliance((1,3,6,1,4,1,22420,2,10,1,2,1,1))
acdShaper1Compliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:acdShaper1Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'acdShaper':acdShaper,'acdShaper1':acdShaper1,'acdShaper1MIBObjects':acdShaper1MIBObjects,'acdShaper1Config':acdShaper1Config,'acdShaper1Stats':acdShaper1Stats,'acdShaper1CodePointStatsTable':acdShaper1CodePointStatsTable,'acdShaper1CodePointStatsEntry':acdShaper1CodePointStatsEntry,_J:acdShaper1CodePointStatsDstID,_K:acdShaper1CodePointStatsSrcID,_L:acdShaper1CodePointStatsColorID,_M:acdShaper1CodePointStatsPcpID,_N:acdShaper1CodePointStatsFwdOctets,_O:acdShaper1CodePointStatsFwdPkts,_P:acdShaper1CodePointStatsFwdRate,_Q:acdShaper1CodePointStatsDelayedOctets,_R:acdShaper1CodePointStatsDelayedPkts,_S:acdShaper1CodePointStatsDelayedRate,_T:acdShaper1CodePointStatsOverflowOctets,_U:acdShaper1CodePointStatsOverflowPkts,_V:acdShaper1CodePointStatsOverflowRate,_W:acdShaper1CodePointStatsQMgmtDropOctets,_X:acdShaper1CodePointStatsQMgmtDropPkts,_Y:acdShaper1CodePointStatsQMgmtDropRate,'acdShaper1Conformance':acdShaper1Conformance,'acdShaper1Compliances':acdShaper1Compliances,'acdShaper1Compliance':acdShaper1Compliance,'acdShaper1Groups':acdShaper1Groups,_Z:acdShaper1CodePointStatsGroup})