_N='h3cMSRecordConnectionThreshold'
_M='h3cMSCurrentRecordConnection'
_L='h3cMSForwardConnectionThreshold'
_K='h3cMSCurrentForwardConnection'
_J='h3cMSVODConnectionThreshold'
_I='h3cMSCurrentVODConnection'
_H='accessible-for-notify'
_G='h3cMSRecordIndex'
_F='h3cMSVODIndex'
_E='h3cMSForwardIndex'
_D='read-write'
_C='read-only'
_B='H3C-MS-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
h3cSurveillanceMIB,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cSurveillanceMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cMSMan=ModuleIdentity((1,3,6,1,4,1,2011,10,9,3))
_H3cMSManMIBObjects_ObjectIdentity=ObjectIdentity
h3cMSManMIBObjects=_H3cMSManMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,9,3,1))
_H3cMSStatisticalPeriod_Type=Unsigned32
_H3cMSStatisticalPeriod_Object=MibScalar
h3cMSStatisticalPeriod=_H3cMSStatisticalPeriod_Object((1,3,6,1,4,1,2011,10,9,3,1,1),_H3cMSStatisticalPeriod_Type())
h3cMSStatisticalPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMSStatisticalPeriod.setStatus(_A)
_H3cMSManMIBTables_ObjectIdentity=ObjectIdentity
h3cMSManMIBTables=_H3cMSManMIBTables_ObjectIdentity((1,3,6,1,4,1,2011,10,9,3,2))
_H3cMSForwardTable_Object=MibTable
h3cMSForwardTable=_H3cMSForwardTable_Object((1,3,6,1,4,1,2011,10,9,3,2,1))
if mibBuilder.loadTexts:h3cMSForwardTable.setStatus(_A)
_H3cMSForwardEntry_Object=MibTableRow
h3cMSForwardEntry=_H3cMSForwardEntry_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1))
h3cMSForwardEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cMSForwardEntry.setStatus(_A)
_H3cMSForwardIndex_Type=PhysicalIndex
_H3cMSForwardIndex_Object=MibTableColumn
h3cMSForwardIndex=_H3cMSForwardIndex_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,1),_H3cMSForwardIndex_Type())
h3cMSForwardIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMSForwardIndex.setStatus(_A)
_H3cMSForwardMaxConnection_Type=Unsigned32
_H3cMSForwardMaxConnection_Object=MibTableColumn
h3cMSForwardMaxConnection=_H3cMSForwardMaxConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,2),_H3cMSForwardMaxConnection_Type())
h3cMSForwardMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSForwardMaxConnection.setStatus(_A)
_H3cMSForwardConnectionThreshold_Type=Unsigned32
_H3cMSForwardConnectionThreshold_Object=MibTableColumn
h3cMSForwardConnectionThreshold=_H3cMSForwardConnectionThreshold_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,3),_H3cMSForwardConnectionThreshold_Type())
h3cMSForwardConnectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMSForwardConnectionThreshold.setStatus(_A)
_H3cMSCurrentForwardConnection_Type=Unsigned32
_H3cMSCurrentForwardConnection_Object=MibTableColumn
h3cMSCurrentForwardConnection=_H3cMSCurrentForwardConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,4),_H3cMSCurrentForwardConnection_Type())
h3cMSCurrentForwardConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSCurrentForwardConnection.setStatus(_A)
_H3cMSPeriodForwardConnection_Type=Unsigned32
_H3cMSPeriodForwardConnection_Object=MibTableColumn
h3cMSPeriodForwardConnection=_H3cMSPeriodForwardConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,5),_H3cMSPeriodForwardConnection_Type())
h3cMSPeriodForwardConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSPeriodForwardConnection.setStatus(_A)
_H3cMSForwardTotalTime_Type=Unsigned32
_H3cMSForwardTotalTime_Object=MibTableColumn
h3cMSForwardTotalTime=_H3cMSForwardTotalTime_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,6),_H3cMSForwardTotalTime_Type())
h3cMSForwardTotalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSForwardTotalTime.setStatus(_A)
_H3cMSForwardTotalConn_Type=Unsigned32
_H3cMSForwardTotalConn_Object=MibTableColumn
h3cMSForwardTotalConn=_H3cMSForwardTotalConn_Object((1,3,6,1,4,1,2011,10,9,3,2,1,1,7),_H3cMSForwardTotalConn_Type())
h3cMSForwardTotalConn.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSForwardTotalConn.setStatus(_A)
_H3cMSVODTable_Object=MibTable
h3cMSVODTable=_H3cMSVODTable_Object((1,3,6,1,4,1,2011,10,9,3,2,2))
if mibBuilder.loadTexts:h3cMSVODTable.setStatus(_A)
_H3cMSVODEntry_Object=MibTableRow
h3cMSVODEntry=_H3cMSVODEntry_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1))
h3cMSVODEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cMSVODEntry.setStatus(_A)
_H3cMSVODIndex_Type=PhysicalIndex
_H3cMSVODIndex_Object=MibTableColumn
h3cMSVODIndex=_H3cMSVODIndex_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,1),_H3cMSVODIndex_Type())
h3cMSVODIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMSVODIndex.setStatus(_A)
_H3cMSVODMaxConnection_Type=Unsigned32
_H3cMSVODMaxConnection_Object=MibTableColumn
h3cMSVODMaxConnection=_H3cMSVODMaxConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,2),_H3cMSVODMaxConnection_Type())
h3cMSVODMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSVODMaxConnection.setStatus(_A)
_H3cMSVODConnectionThreshold_Type=Unsigned32
_H3cMSVODConnectionThreshold_Object=MibTableColumn
h3cMSVODConnectionThreshold=_H3cMSVODConnectionThreshold_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,3),_H3cMSVODConnectionThreshold_Type())
h3cMSVODConnectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMSVODConnectionThreshold.setStatus(_A)
_H3cMSCurrentVODConnection_Type=Unsigned32
_H3cMSCurrentVODConnection_Object=MibTableColumn
h3cMSCurrentVODConnection=_H3cMSCurrentVODConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,4),_H3cMSCurrentVODConnection_Type())
h3cMSCurrentVODConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSCurrentVODConnection.setStatus(_A)
_H3cMSPeriodVODMaxConnection_Type=Unsigned32
_H3cMSPeriodVODMaxConnection_Object=MibTableColumn
h3cMSPeriodVODMaxConnection=_H3cMSPeriodVODMaxConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,5),_H3cMSPeriodVODMaxConnection_Type())
h3cMSPeriodVODMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSPeriodVODMaxConnection.setStatus(_A)
_H3cMSVODTotalTime_Type=Unsigned32
_H3cMSVODTotalTime_Object=MibTableColumn
h3cMSVODTotalTime=_H3cMSVODTotalTime_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,6),_H3cMSVODTotalTime_Type())
h3cMSVODTotalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSVODTotalTime.setStatus(_A)
_H3cMSVODTotalConn_Type=Unsigned32
_H3cMSVODTotalConn_Object=MibTableColumn
h3cMSVODTotalConn=_H3cMSVODTotalConn_Object((1,3,6,1,4,1,2011,10,9,3,2,2,1,7),_H3cMSVODTotalConn_Type())
h3cMSVODTotalConn.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSVODTotalConn.setStatus(_A)
_H3cMSRecordTable_Object=MibTable
h3cMSRecordTable=_H3cMSRecordTable_Object((1,3,6,1,4,1,2011,10,9,3,2,3))
if mibBuilder.loadTexts:h3cMSRecordTable.setStatus(_A)
_H3cMSRecordEntry_Object=MibTableRow
h3cMSRecordEntry=_H3cMSRecordEntry_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1))
h3cMSRecordEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cMSRecordEntry.setStatus(_A)
_H3cMSRecordIndex_Type=PhysicalIndex
_H3cMSRecordIndex_Object=MibTableColumn
h3cMSRecordIndex=_H3cMSRecordIndex_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,1),_H3cMSRecordIndex_Type())
h3cMSRecordIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cMSRecordIndex.setStatus(_A)
_H3cMSRecordMaxConnection_Type=Unsigned32
_H3cMSRecordMaxConnection_Object=MibTableColumn
h3cMSRecordMaxConnection=_H3cMSRecordMaxConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,2),_H3cMSRecordMaxConnection_Type())
h3cMSRecordMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSRecordMaxConnection.setStatus(_A)
_H3cMSRecordConnectionThreshold_Type=Unsigned32
_H3cMSRecordConnectionThreshold_Object=MibTableColumn
h3cMSRecordConnectionThreshold=_H3cMSRecordConnectionThreshold_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,3),_H3cMSRecordConnectionThreshold_Type())
h3cMSRecordConnectionThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMSRecordConnectionThreshold.setStatus(_A)
_H3cMSCurrentRecordConnection_Type=Unsigned32
_H3cMSCurrentRecordConnection_Object=MibTableColumn
h3cMSCurrentRecordConnection=_H3cMSCurrentRecordConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,4),_H3cMSCurrentRecordConnection_Type())
h3cMSCurrentRecordConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSCurrentRecordConnection.setStatus(_A)
_H3cMSPeriodRecordMaxConnection_Type=Unsigned32
_H3cMSPeriodRecordMaxConnection_Object=MibTableColumn
h3cMSPeriodRecordMaxConnection=_H3cMSPeriodRecordMaxConnection_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,5),_H3cMSPeriodRecordMaxConnection_Type())
h3cMSPeriodRecordMaxConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSPeriodRecordMaxConnection.setStatus(_A)
_H3cMSRecordTotalTime_Type=Unsigned32
_H3cMSRecordTotalTime_Object=MibTableColumn
h3cMSRecordTotalTime=_H3cMSRecordTotalTime_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,6),_H3cMSRecordTotalTime_Type())
h3cMSRecordTotalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSRecordTotalTime.setStatus(_A)
_H3cMSRecordTotalConn_Type=Unsigned32
_H3cMSRecordTotalConn_Object=MibTableColumn
h3cMSRecordTotalConn=_H3cMSRecordTotalConn_Object((1,3,6,1,4,1,2011,10,9,3,2,3,1,7),_H3cMSRecordTotalConn_Type())
h3cMSRecordTotalConn.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMSRecordTotalConn.setStatus(_A)
_H3cMSManMIBTrap_ObjectIdentity=ObjectIdentity
h3cMSManMIBTrap=_H3cMSManMIBTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,9,3,3))
_H3cMSManTrapPrex_ObjectIdentity=ObjectIdentity
h3cMSManTrapPrex=_H3cMSManTrapPrex_ObjectIdentity((1,3,6,1,4,1,2011,10,9,3,3,0))
h3cMSManVODConnectionThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,1))
h3cMSManVODConnectionThresholdTrap.setObjects(*((_B,_F),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:h3cMSManVODConnectionThresholdTrap.setStatus(_A)
h3cMSManVODConnectionRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,2))
h3cMSManVODConnectionRecoverTrap.setObjects(*((_B,_F),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:h3cMSManVODConnectionRecoverTrap.setStatus(_A)
h3cMSManForwardConnectionThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,3))
h3cMSManForwardConnectionThresholdTrap.setObjects(*((_B,_E),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cMSManForwardConnectionThresholdTrap.setStatus(_A)
h3cMSManForwardConnectionRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,4))
h3cMSManForwardConnectionRecoverTrap.setObjects(*((_B,_E),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cMSManForwardConnectionRecoverTrap.setStatus(_A)
h3cMSManRecordConnectionThresholdTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,5))
h3cMSManRecordConnectionThresholdTrap.setObjects(*((_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cMSManRecordConnectionThresholdTrap.setStatus(_A)
h3cMSManRecordConnectionRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,9,3,3,0,6))
h3cMSManRecordConnectionRecoverTrap.setObjects(*((_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cMSManRecordConnectionRecoverTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cMSMan':h3cMSMan,'h3cMSManMIBObjects':h3cMSManMIBObjects,'h3cMSStatisticalPeriod':h3cMSStatisticalPeriod,'h3cMSManMIBTables':h3cMSManMIBTables,'h3cMSForwardTable':h3cMSForwardTable,'h3cMSForwardEntry':h3cMSForwardEntry,_E:h3cMSForwardIndex,'h3cMSForwardMaxConnection':h3cMSForwardMaxConnection,_L:h3cMSForwardConnectionThreshold,_K:h3cMSCurrentForwardConnection,'h3cMSPeriodForwardConnection':h3cMSPeriodForwardConnection,'h3cMSForwardTotalTime':h3cMSForwardTotalTime,'h3cMSForwardTotalConn':h3cMSForwardTotalConn,'h3cMSVODTable':h3cMSVODTable,'h3cMSVODEntry':h3cMSVODEntry,_F:h3cMSVODIndex,'h3cMSVODMaxConnection':h3cMSVODMaxConnection,_J:h3cMSVODConnectionThreshold,_I:h3cMSCurrentVODConnection,'h3cMSPeriodVODMaxConnection':h3cMSPeriodVODMaxConnection,'h3cMSVODTotalTime':h3cMSVODTotalTime,'h3cMSVODTotalConn':h3cMSVODTotalConn,'h3cMSRecordTable':h3cMSRecordTable,'h3cMSRecordEntry':h3cMSRecordEntry,_G:h3cMSRecordIndex,'h3cMSRecordMaxConnection':h3cMSRecordMaxConnection,_N:h3cMSRecordConnectionThreshold,_M:h3cMSCurrentRecordConnection,'h3cMSPeriodRecordMaxConnection':h3cMSPeriodRecordMaxConnection,'h3cMSRecordTotalTime':h3cMSRecordTotalTime,'h3cMSRecordTotalConn':h3cMSRecordTotalConn,'h3cMSManMIBTrap':h3cMSManMIBTrap,'h3cMSManTrapPrex':h3cMSManTrapPrex,'h3cMSManVODConnectionThresholdTrap':h3cMSManVODConnectionThresholdTrap,'h3cMSManVODConnectionRecoverTrap':h3cMSManVODConnectionRecoverTrap,'h3cMSManForwardConnectionThresholdTrap':h3cMSManForwardConnectionThresholdTrap,'h3cMSManForwardConnectionRecoverTrap':h3cMSManForwardConnectionRecoverTrap,'h3cMSManRecordConnectionThresholdTrap':h3cMSManRecordConnectionThresholdTrap,'h3cMSManRecordConnectionRecoverTrap':h3cMSManRecordConnectionRecoverTrap})