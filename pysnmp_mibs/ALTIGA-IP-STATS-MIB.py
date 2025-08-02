_G='altigaIpStatsGroup'
_F='alIpInterfaceStatsCurrentDuplex'
_E='read-only'
_D='alIpInterfaceStatsIndex'
_C='Integer32'
_B='ALTIGA-IP-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alIpMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alIpMibModule')
alIpGroup,alStatsIp=mibBuilder.importSymbols('ALTIGA-MIB','alIpGroup','alStatsIp')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
altigaIpStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,13,2))
if mibBuilder.loadTexts:altigaIpStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaIpStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaIpStatsMibConformance=_AltigaIpStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,13,2,1))
_AltigaIpStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaIpStatsMibCompliances=_AltigaIpStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,13,2,1,1))
_AlStatsIpGlobal_ObjectIdentity=ObjectIdentity
alStatsIpGlobal=_AlStatsIpGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,8,1))
_AlIpInterfaceStatsTable_Object=MibTable
alIpInterfaceStatsTable=_AlIpInterfaceStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,8,1,1))
if mibBuilder.loadTexts:alIpInterfaceStatsTable.setStatus(_A)
_AlIpInterfaceStatsEntry_Object=MibTableRow
alIpInterfaceStatsEntry=_AlIpInterfaceStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,8,1,1,1))
alIpInterfaceStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alIpInterfaceStatsEntry.setStatus(_A)
class _AlIpInterfaceStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlIpInterfaceStatsIndex_Type.__name__=_C
_AlIpInterfaceStatsIndex_Object=MibTableColumn
alIpInterfaceStatsIndex=_AlIpInterfaceStatsIndex_Object((1,3,6,1,4,1,3076,2,1,2,8,1,1,1,1),_AlIpInterfaceStatsIndex_Type())
alIpInterfaceStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alIpInterfaceStatsIndex.setStatus(_A)
class _AlIpInterfaceStatsCurrentDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('full',2),('half',3)))
_AlIpInterfaceStatsCurrentDuplex_Type.__name__=_C
_AlIpInterfaceStatsCurrentDuplex_Object=MibTableColumn
alIpInterfaceStatsCurrentDuplex=_AlIpInterfaceStatsCurrentDuplex_Object((1,3,6,1,4,1,3076,2,1,2,8,1,1,1,2),_AlIpInterfaceStatsCurrentDuplex_Type())
alIpInterfaceStatsCurrentDuplex.setMaxAccess(_E)
if mibBuilder.loadTexts:alIpInterfaceStatsCurrentDuplex.setStatus(_A)
altigaIpStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,8,2))
altigaIpStatsGroup.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:altigaIpStatsGroup.setStatus(_A)
altigaIpStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,13,2,1,1,1))
altigaIpStatsMibCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:altigaIpStatsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'altigaIpStatsMibModule':altigaIpStatsMibModule,'altigaIpStatsMibConformance':altigaIpStatsMibConformance,'altigaIpStatsMibCompliances':altigaIpStatsMibCompliances,'altigaIpStatsMibCompliance':altigaIpStatsMibCompliance,_G:altigaIpStatsGroup,'alStatsIpGlobal':alStatsIpGlobal,'alIpInterfaceStatsTable':alIpInterfaceStatsTable,'alIpInterfaceStatsEntry':alIpInterfaceStatsEntry,_D:alIpInterfaceStatsIndex,_F:alIpInterfaceStatsCurrentDuplex})