_Q='ciscoTcpMIBGroupRev1'
_P='ciscoTcpMIBGroup'
_O='ciscoTcpConnFastRetransPkts'
_N='ciscoTcpConnRetransPkts'
_M='ciscoTcpConnRto'
_L='deprecated'
_K='ciscoTcpConnEntry'
_J='milliseconds'
_I='ciscoTcpConnSRTT'
_H='ciscoTcpConnElapsed'
_G='ciscoTcpConnOutPkts'
_F='ciscoTcpConnInPkts'
_E='ciscoTcpConnOutBytes'
_D='ciscoTcpConnInBytes'
_C='read-only'
_B='current'
_A='CISCO-TCP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tcpConnEntry,=mibBuilder.importSymbols('TCP-MIB','tcpConnEntry')
ciscoTcpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,6))
if mibBuilder.loadTexts:ciscoTcpMIB.setRevisions(('2001-11-12 00:00','1996-12-03 00:00','1994-07-21 00:00'))
_CiscoTcpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTcpMIBObjects=_CiscoTcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,6,1))
_CiscoTcpConnTable_Object=MibTable
ciscoTcpConnTable=_CiscoTcpConnTable_Object((1,3,6,1,4,1,9,9,6,1,1))
if mibBuilder.loadTexts:ciscoTcpConnTable.setStatus(_B)
_CiscoTcpConnEntry_Object=MibTableRow
ciscoTcpConnEntry=_CiscoTcpConnEntry_Object((1,3,6,1,4,1,9,9,6,1,1,1))
if mibBuilder.loadTexts:ciscoTcpConnEntry.setStatus(_B)
_CiscoTcpConnInBytes_Type=Counter32
_CiscoTcpConnInBytes_Object=MibTableColumn
ciscoTcpConnInBytes=_CiscoTcpConnInBytes_Object((1,3,6,1,4,1,9,9,6,1,1,1,1),_CiscoTcpConnInBytes_Type())
ciscoTcpConnInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnInBytes.setStatus(_B)
_CiscoTcpConnOutBytes_Type=Counter32
_CiscoTcpConnOutBytes_Object=MibTableColumn
ciscoTcpConnOutBytes=_CiscoTcpConnOutBytes_Object((1,3,6,1,4,1,9,9,6,1,1,1,2),_CiscoTcpConnOutBytes_Type())
ciscoTcpConnOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnOutBytes.setStatus(_B)
_CiscoTcpConnInPkts_Type=Counter32
_CiscoTcpConnInPkts_Object=MibTableColumn
ciscoTcpConnInPkts=_CiscoTcpConnInPkts_Object((1,3,6,1,4,1,9,9,6,1,1,1,3),_CiscoTcpConnInPkts_Type())
ciscoTcpConnInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnInPkts.setStatus(_B)
_CiscoTcpConnOutPkts_Type=Counter32
_CiscoTcpConnOutPkts_Object=MibTableColumn
ciscoTcpConnOutPkts=_CiscoTcpConnOutPkts_Object((1,3,6,1,4,1,9,9,6,1,1,1,4),_CiscoTcpConnOutPkts_Type())
ciscoTcpConnOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnOutPkts.setStatus(_B)
_CiscoTcpConnElapsed_Type=TimeTicks
_CiscoTcpConnElapsed_Object=MibTableColumn
ciscoTcpConnElapsed=_CiscoTcpConnElapsed_Object((1,3,6,1,4,1,9,9,6,1,1,1,5),_CiscoTcpConnElapsed_Type())
ciscoTcpConnElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnElapsed.setStatus(_B)
_CiscoTcpConnSRTT_Type=Integer32
_CiscoTcpConnSRTT_Object=MibTableColumn
ciscoTcpConnSRTT=_CiscoTcpConnSRTT_Object((1,3,6,1,4,1,9,9,6,1,1,1,6),_CiscoTcpConnSRTT_Type())
ciscoTcpConnSRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnSRTT.setStatus(_B)
if mibBuilder.loadTexts:ciscoTcpConnSRTT.setUnits(_J)
_CiscoTcpConnRetransPkts_Type=Counter32
_CiscoTcpConnRetransPkts_Object=MibTableColumn
ciscoTcpConnRetransPkts=_CiscoTcpConnRetransPkts_Object((1,3,6,1,4,1,9,9,6,1,1,1,7),_CiscoTcpConnRetransPkts_Type())
ciscoTcpConnRetransPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnRetransPkts.setStatus(_B)
_CiscoTcpConnFastRetransPkts_Type=Counter32
_CiscoTcpConnFastRetransPkts_Object=MibTableColumn
ciscoTcpConnFastRetransPkts=_CiscoTcpConnFastRetransPkts_Object((1,3,6,1,4,1,9,9,6,1,1,1,8),_CiscoTcpConnFastRetransPkts_Type())
ciscoTcpConnFastRetransPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnFastRetransPkts.setStatus(_B)
_CiscoTcpConnRto_Type=Integer32
_CiscoTcpConnRto_Object=MibTableColumn
ciscoTcpConnRto=_CiscoTcpConnRto_Object((1,3,6,1,4,1,9,9,6,1,1,1,9),_CiscoTcpConnRto_Type())
ciscoTcpConnRto.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoTcpConnRto.setStatus(_B)
if mibBuilder.loadTexts:ciscoTcpConnRto.setUnits(_J)
_CiscoTcpMIBTraps_ObjectIdentity=ObjectIdentity
ciscoTcpMIBTraps=_CiscoTcpMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,6,2))
_CiscoTcpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoTcpMIBConformance=_CiscoTcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,6,3))
_CiscoTcpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTcpMIBCompliances=_CiscoTcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,6,3,1))
_CiscoTcpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTcpMIBGroups=_CiscoTcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,6,3,2))
tcpConnEntry.registerAugmentions((_A,_K))
ciscoTcpConnEntry.setIndexNames(*tcpConnEntry.getIndexNames())
ciscoTcpMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,6,3,2,1))
ciscoTcpMIBGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:ciscoTcpMIBGroup.setStatus(_L)
ciscoTcpMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,6,3,2,2))
ciscoTcpMIBGroupRev1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoTcpMIBGroupRev1.setStatus(_B)
ciscoTcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,6,3,1,1))
ciscoTcpMIBCompliance.setObjects((_A,_P))
if mibBuilder.loadTexts:ciscoTcpMIBCompliance.setStatus(_L)
ciscoTcpMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,6,3,1,2))
ciscoTcpMIBComplianceRev1.setObjects((_A,_Q))
if mibBuilder.loadTexts:ciscoTcpMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoTcpMIB':ciscoTcpMIB,'ciscoTcpMIBObjects':ciscoTcpMIBObjects,'ciscoTcpConnTable':ciscoTcpConnTable,_K:ciscoTcpConnEntry,_D:ciscoTcpConnInBytes,_E:ciscoTcpConnOutBytes,_F:ciscoTcpConnInPkts,_G:ciscoTcpConnOutPkts,_H:ciscoTcpConnElapsed,_I:ciscoTcpConnSRTT,_N:ciscoTcpConnRetransPkts,_O:ciscoTcpConnFastRetransPkts,_M:ciscoTcpConnRto,'ciscoTcpMIBTraps':ciscoTcpMIBTraps,'ciscoTcpMIBConformance':ciscoTcpMIBConformance,'ciscoTcpMIBCompliances':ciscoTcpMIBCompliances,'ciscoTcpMIBCompliance':ciscoTcpMIBCompliance,'ciscoTcpMIBComplianceRev1':ciscoTcpMIBComplianceRev1,'ciscoTcpMIBGroups':ciscoTcpMIBGroups,_P:ciscoTcpMIBGroup,_Q:ciscoTcpMIBGroupRev1})