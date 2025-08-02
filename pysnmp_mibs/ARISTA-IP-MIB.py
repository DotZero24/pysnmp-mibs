_U='aristaIpIfStatsGroup'
_T='aristaIpIfStatsRefreshRate'
_S='aristaIpIfStatsDiscontinuityTime'
_R='aristaIpIfStatsOutMcastOctets'
_Q='aristaIpIfStatsOutMcastPkts'
_P='aristaIpIfStatsInMcastOctets'
_O='aristaIpIfStatsInMcastPkts'
_N='aristaIpIfStatsOutUcastOctets'
_M='aristaIpIfStatsOutUcastPkts'
_L='aristaIpIfStatsInUcastOctets'
_K='aristaIpIfStatsInUcastPkts'
_J='aristaIpIfStatsOutOctets'
_I='aristaIpIfStatsOutPkts'
_H='aristaIpIfStatsInOctets'
_G='aristaIpIfStatsInPkts'
_F='not-accessible'
_E='aristaIpIfStatsIfIndex'
_D='aristaIpIfStatsIPVersion'
_C='read-only'
_B='ARISTA-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
aristaIpMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,27))
if mibBuilder.loadTexts:aristaIpMIB.setRevisions(('2018-12-12 00:00',))
_AristaIpMibObjects_ObjectIdentity=ObjectIdentity
aristaIpMibObjects=_AristaIpMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,27,1))
_AristaIpIfStatsTable_Object=MibTable
aristaIpIfStatsTable=_AristaIpIfStatsTable_Object((1,3,6,1,4,1,30065,3,27,1,1))
if mibBuilder.loadTexts:aristaIpIfStatsTable.setStatus(_A)
_AristaIpIfStatsEntry_Object=MibTableRow
aristaIpIfStatsEntry=_AristaIpIfStatsEntry_Object((1,3,6,1,4,1,30065,3,27,1,1,1))
aristaIpIfStatsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:aristaIpIfStatsEntry.setStatus(_A)
_AristaIpIfStatsIPVersion_Type=InetVersion
_AristaIpIfStatsIPVersion_Object=MibTableColumn
aristaIpIfStatsIPVersion=_AristaIpIfStatsIPVersion_Object((1,3,6,1,4,1,30065,3,27,1,1,1,1),_AristaIpIfStatsIPVersion_Type())
aristaIpIfStatsIPVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaIpIfStatsIPVersion.setStatus(_A)
_AristaIpIfStatsIfIndex_Type=InterfaceIndex
_AristaIpIfStatsIfIndex_Object=MibTableColumn
aristaIpIfStatsIfIndex=_AristaIpIfStatsIfIndex_Object((1,3,6,1,4,1,30065,3,27,1,1,1,2),_AristaIpIfStatsIfIndex_Type())
aristaIpIfStatsIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaIpIfStatsIfIndex.setStatus(_A)
_AristaIpIfStatsInPkts_Type=Counter64
_AristaIpIfStatsInPkts_Object=MibTableColumn
aristaIpIfStatsInPkts=_AristaIpIfStatsInPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,3),_AristaIpIfStatsInPkts_Type())
aristaIpIfStatsInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInPkts.setStatus(_A)
_AristaIpIfStatsInOctets_Type=Counter64
_AristaIpIfStatsInOctets_Object=MibTableColumn
aristaIpIfStatsInOctets=_AristaIpIfStatsInOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,4),_AristaIpIfStatsInOctets_Type())
aristaIpIfStatsInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInOctets.setStatus(_A)
_AristaIpIfStatsOutPkts_Type=Counter64
_AristaIpIfStatsOutPkts_Object=MibTableColumn
aristaIpIfStatsOutPkts=_AristaIpIfStatsOutPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,5),_AristaIpIfStatsOutPkts_Type())
aristaIpIfStatsOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutPkts.setStatus(_A)
_AristaIpIfStatsOutOctets_Type=Counter64
_AristaIpIfStatsOutOctets_Object=MibTableColumn
aristaIpIfStatsOutOctets=_AristaIpIfStatsOutOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,6),_AristaIpIfStatsOutOctets_Type())
aristaIpIfStatsOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutOctets.setStatus(_A)
_AristaIpIfStatsInUcastPkts_Type=Counter64
_AristaIpIfStatsInUcastPkts_Object=MibTableColumn
aristaIpIfStatsInUcastPkts=_AristaIpIfStatsInUcastPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,7),_AristaIpIfStatsInUcastPkts_Type())
aristaIpIfStatsInUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInUcastPkts.setStatus(_A)
_AristaIpIfStatsInUcastOctets_Type=Counter64
_AristaIpIfStatsInUcastOctets_Object=MibTableColumn
aristaIpIfStatsInUcastOctets=_AristaIpIfStatsInUcastOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,8),_AristaIpIfStatsInUcastOctets_Type())
aristaIpIfStatsInUcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInUcastOctets.setStatus(_A)
_AristaIpIfStatsOutUcastPkts_Type=Counter64
_AristaIpIfStatsOutUcastPkts_Object=MibTableColumn
aristaIpIfStatsOutUcastPkts=_AristaIpIfStatsOutUcastPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,9),_AristaIpIfStatsOutUcastPkts_Type())
aristaIpIfStatsOutUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutUcastPkts.setStatus(_A)
_AristaIpIfStatsOutUcastOctets_Type=Counter64
_AristaIpIfStatsOutUcastOctets_Object=MibTableColumn
aristaIpIfStatsOutUcastOctets=_AristaIpIfStatsOutUcastOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,10),_AristaIpIfStatsOutUcastOctets_Type())
aristaIpIfStatsOutUcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutUcastOctets.setStatus(_A)
_AristaIpIfStatsInMcastPkts_Type=Counter64
_AristaIpIfStatsInMcastPkts_Object=MibTableColumn
aristaIpIfStatsInMcastPkts=_AristaIpIfStatsInMcastPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,11),_AristaIpIfStatsInMcastPkts_Type())
aristaIpIfStatsInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInMcastPkts.setStatus(_A)
_AristaIpIfStatsInMcastOctets_Type=Counter64
_AristaIpIfStatsInMcastOctets_Object=MibTableColumn
aristaIpIfStatsInMcastOctets=_AristaIpIfStatsInMcastOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,12),_AristaIpIfStatsInMcastOctets_Type())
aristaIpIfStatsInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsInMcastOctets.setStatus(_A)
_AristaIpIfStatsOutMcastPkts_Type=Counter64
_AristaIpIfStatsOutMcastPkts_Object=MibTableColumn
aristaIpIfStatsOutMcastPkts=_AristaIpIfStatsOutMcastPkts_Object((1,3,6,1,4,1,30065,3,27,1,1,1,13),_AristaIpIfStatsOutMcastPkts_Type())
aristaIpIfStatsOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutMcastPkts.setStatus(_A)
_AristaIpIfStatsOutMcastOctets_Type=Counter64
_AristaIpIfStatsOutMcastOctets_Object=MibTableColumn
aristaIpIfStatsOutMcastOctets=_AristaIpIfStatsOutMcastOctets_Object((1,3,6,1,4,1,30065,3,27,1,1,1,14),_AristaIpIfStatsOutMcastOctets_Type())
aristaIpIfStatsOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsOutMcastOctets.setStatus(_A)
_AristaIpIfStatsDiscontinuityTime_Type=TimeStamp
_AristaIpIfStatsDiscontinuityTime_Object=MibTableColumn
aristaIpIfStatsDiscontinuityTime=_AristaIpIfStatsDiscontinuityTime_Object((1,3,6,1,4,1,30065,3,27,1,1,1,15),_AristaIpIfStatsDiscontinuityTime_Type())
aristaIpIfStatsDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsDiscontinuityTime.setStatus(_A)
_AristaIpIfStatsRefreshRate_Type=Unsigned32
_AristaIpIfStatsRefreshRate_Object=MibTableColumn
aristaIpIfStatsRefreshRate=_AristaIpIfStatsRefreshRate_Object((1,3,6,1,4,1,30065,3,27,1,1,1,16),_AristaIpIfStatsRefreshRate_Type())
aristaIpIfStatsRefreshRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaIpIfStatsRefreshRate.setStatus(_A)
if mibBuilder.loadTexts:aristaIpIfStatsRefreshRate.setUnits('milli-seconds')
_AristaIpMibConformance_ObjectIdentity=ObjectIdentity
aristaIpMibConformance=_AristaIpMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,27,2))
_AristaIpMibCompliances_ObjectIdentity=ObjectIdentity
aristaIpMibCompliances=_AristaIpMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,27,2,1))
_AristaIpMibGroups_ObjectIdentity=ObjectIdentity
aristaIpMibGroups=_AristaIpMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,27,2,2))
aristaIpIfStatsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,27,2,2,1))
aristaIpIfStatsGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:aristaIpIfStatsGroup.setStatus(_A)
aristaIpMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,27,2,1,1))
aristaIpMibCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:aristaIpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aristaIpMIB':aristaIpMIB,'aristaIpMibObjects':aristaIpMibObjects,'aristaIpIfStatsTable':aristaIpIfStatsTable,'aristaIpIfStatsEntry':aristaIpIfStatsEntry,_D:aristaIpIfStatsIPVersion,_E:aristaIpIfStatsIfIndex,_G:aristaIpIfStatsInPkts,_H:aristaIpIfStatsInOctets,_I:aristaIpIfStatsOutPkts,_J:aristaIpIfStatsOutOctets,_K:aristaIpIfStatsInUcastPkts,_L:aristaIpIfStatsInUcastOctets,_M:aristaIpIfStatsOutUcastPkts,_N:aristaIpIfStatsOutUcastOctets,_O:aristaIpIfStatsInMcastPkts,_P:aristaIpIfStatsInMcastOctets,_Q:aristaIpIfStatsOutMcastPkts,_R:aristaIpIfStatsOutMcastOctets,_S:aristaIpIfStatsDiscontinuityTime,_T:aristaIpIfStatsRefreshRate,'aristaIpMibConformance':aristaIpMibConformance,'aristaIpMibCompliances':aristaIpMibCompliances,'aristaIpMibCompliance':aristaIpMibCompliance,'aristaIpMibGroups':aristaIpMibGroups,_U:aristaIpIfStatsGroup})