_T='ipmIgnitionThresholdMIBGroup'
_S='ipmIgnitionStatusMIBGroup'
_R='ipmIgnitionOffTimer'
_Q='ipmOvervoltageTimer'
_P='ipmUndervoltageTimer'
_O='ipmSenseOff'
_N='ipmSenseOn'
_M='ipmOvervoltage'
_L='ipmUndervoltage'
_K='ipmConfigBattery'
_J='ipmShutdownTimer'
_I='ipmIgnitionSense'
_H='ipmIgnitionStatus'
_G='ipmInputVoltage'
_F='ipmIgnitionManagement'
_E='ipmIgnitionThresholdIndex'
_D='ipmIgnitionStatusIndex'
_C='read-only'
_B='CISCO-IGNITION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoIgnitionMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1061))
if mibBuilder.loadTexts:ciscoIgnitionMIB.setRevisions(('2023-06-30 00:00',))
class IgnitionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bootloader',0),('powerOn',1),('lowDelay',2),('offDelay',3),('highDelay',4),('onDelay',5),('monitor',6),('sleep',7),('unknown',8)))
_IpmMIBStatus_ObjectIdentity=ObjectIdentity
ipmMIBStatus=_IpmMIBStatus_ObjectIdentity((1,3,6,1,4,1,9,9,1061,0))
_IpmIgnitionStatusTable_Object=MibTable
ipmIgnitionStatusTable=_IpmIgnitionStatusTable_Object((1,3,6,1,4,1,9,9,1061,0,1))
if mibBuilder.loadTexts:ipmIgnitionStatusTable.setStatus(_A)
_IpmIgnitionStatusEntry_Object=MibTableRow
ipmIgnitionStatusEntry=_IpmIgnitionStatusEntry_Object((1,3,6,1,4,1,9,9,1061,0,1,1))
ipmIgnitionStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ipmIgnitionStatusEntry.setStatus(_A)
_IpmIgnitionStatusIndex_Type=Integer32
_IpmIgnitionStatusIndex_Object=MibTableColumn
ipmIgnitionStatusIndex=_IpmIgnitionStatusIndex_Object((1,3,6,1,4,1,9,9,1061,0,1,1,1),_IpmIgnitionStatusIndex_Type())
ipmIgnitionStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionStatusIndex.setStatus(_A)
_IpmIgnitionManagement_Type=TruthValue
_IpmIgnitionManagement_Object=MibTableColumn
ipmIgnitionManagement=_IpmIgnitionManagement_Object((1,3,6,1,4,1,9,9,1061,0,1,1,2),_IpmIgnitionManagement_Type())
ipmIgnitionManagement.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionManagement.setStatus(_A)
_IpmInputVoltage_Type=Unsigned32
_IpmInputVoltage_Object=MibTableColumn
ipmInputVoltage=_IpmInputVoltage_Object((1,3,6,1,4,1,9,9,1061,0,1,1,3),_IpmInputVoltage_Type())
ipmInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmInputVoltage.setStatus(_A)
_IpmIgnitionStatus_Type=IgnitionStatus
_IpmIgnitionStatus_Object=MibTableColumn
ipmIgnitionStatus=_IpmIgnitionStatus_Object((1,3,6,1,4,1,9,9,1061,0,1,1,4),_IpmIgnitionStatus_Type())
ipmIgnitionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionStatus.setStatus(_A)
_IpmIgnitionSense_Type=TruthValue
_IpmIgnitionSense_Object=MibTableColumn
ipmIgnitionSense=_IpmIgnitionSense_Object((1,3,6,1,4,1,9,9,1061,0,1,1,5),_IpmIgnitionSense_Type())
ipmIgnitionSense.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionSense.setStatus(_A)
_IpmShutdownTimer_Type=Unsigned32
_IpmShutdownTimer_Object=MibTableColumn
ipmShutdownTimer=_IpmShutdownTimer_Object((1,3,6,1,4,1,9,9,1061,0,1,1,6),_IpmShutdownTimer_Type())
ipmShutdownTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmShutdownTimer.setStatus(_A)
_IpmConfigBattery_Type=Integer32
_IpmConfigBattery_Object=MibTableColumn
ipmConfigBattery=_IpmConfigBattery_Object((1,3,6,1,4,1,9,9,1061,0,1,1,7),_IpmConfigBattery_Type())
ipmConfigBattery.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmConfigBattery.setStatus(_A)
_IpmMIBThreshold_ObjectIdentity=ObjectIdentity
ipmMIBThreshold=_IpmMIBThreshold_ObjectIdentity((1,3,6,1,4,1,9,9,1061,1))
_IpmIgnitionThresholdTable_Object=MibTable
ipmIgnitionThresholdTable=_IpmIgnitionThresholdTable_Object((1,3,6,1,4,1,9,9,1061,1,1))
if mibBuilder.loadTexts:ipmIgnitionThresholdTable.setStatus(_A)
_IpmIgnitionThresholdEntry_Object=MibTableRow
ipmIgnitionThresholdEntry=_IpmIgnitionThresholdEntry_Object((1,3,6,1,4,1,9,9,1061,1,1,1))
ipmIgnitionThresholdEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ipmIgnitionThresholdEntry.setStatus(_A)
_IpmIgnitionThresholdIndex_Type=Integer32
_IpmIgnitionThresholdIndex_Object=MibTableColumn
ipmIgnitionThresholdIndex=_IpmIgnitionThresholdIndex_Object((1,3,6,1,4,1,9,9,1061,1,1,1,1),_IpmIgnitionThresholdIndex_Type())
ipmIgnitionThresholdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionThresholdIndex.setStatus(_A)
_IpmUndervoltage_Type=Unsigned32
_IpmUndervoltage_Object=MibTableColumn
ipmUndervoltage=_IpmUndervoltage_Object((1,3,6,1,4,1,9,9,1061,1,1,1,2),_IpmUndervoltage_Type())
ipmUndervoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmUndervoltage.setStatus(_A)
_IpmOvervoltage_Type=Unsigned32
_IpmOvervoltage_Object=MibTableColumn
ipmOvervoltage=_IpmOvervoltage_Object((1,3,6,1,4,1,9,9,1061,1,1,1,3),_IpmOvervoltage_Type())
ipmOvervoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmOvervoltage.setStatus(_A)
_IpmSenseOn_Type=Unsigned32
_IpmSenseOn_Object=MibTableColumn
ipmSenseOn=_IpmSenseOn_Object((1,3,6,1,4,1,9,9,1061,1,1,1,4),_IpmSenseOn_Type())
ipmSenseOn.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmSenseOn.setStatus(_A)
_IpmSenseOff_Type=Unsigned32
_IpmSenseOff_Object=MibTableColumn
ipmSenseOff=_IpmSenseOff_Object((1,3,6,1,4,1,9,9,1061,1,1,1,5),_IpmSenseOff_Type())
ipmSenseOff.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmSenseOff.setStatus(_A)
_IpmUndervoltageTimer_Type=Unsigned32
_IpmUndervoltageTimer_Object=MibTableColumn
ipmUndervoltageTimer=_IpmUndervoltageTimer_Object((1,3,6,1,4,1,9,9,1061,1,1,1,6),_IpmUndervoltageTimer_Type())
ipmUndervoltageTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmUndervoltageTimer.setStatus(_A)
_IpmOvervoltageTimer_Type=Unsigned32
_IpmOvervoltageTimer_Object=MibTableColumn
ipmOvervoltageTimer=_IpmOvervoltageTimer_Object((1,3,6,1,4,1,9,9,1061,1,1,1,7),_IpmOvervoltageTimer_Type())
ipmOvervoltageTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmOvervoltageTimer.setStatus(_A)
_IpmIgnitionOffTimer_Type=Unsigned32
_IpmIgnitionOffTimer_Object=MibTableColumn
ipmIgnitionOffTimer=_IpmIgnitionOffTimer_Object((1,3,6,1,4,1,9,9,1061,1,1,1,8),_IpmIgnitionOffTimer_Type())
ipmIgnitionOffTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ipmIgnitionOffTimer.setStatus(_A)
_IpmMIBConform_ObjectIdentity=ObjectIdentity
ipmMIBConform=_IpmMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1061,2))
_IpmMIBCompliance_ObjectIdentity=ObjectIdentity
ipmMIBCompliance=_IpmMIBCompliance_ObjectIdentity((1,3,6,1,4,1,9,9,1061,2,1))
_IpmMIBGroups_ObjectIdentity=ObjectIdentity
ipmMIBGroups=_IpmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1061,2,2))
ipmIgnitionStatusMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,1061,2,2,1))
ipmIgnitionStatusMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ipmIgnitionStatusMIBGroup.setStatus(_A)
ipmIgnitionThresholdMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,1061,2,2,2))
ipmIgnitionThresholdMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ipmIgnitionThresholdMIBGroup.setStatus(_A)
ipmMIBCompliances=ModuleCompliance((1,3,6,1,4,1,9,9,1061,2,1,1))
ipmMIBCompliances.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ipmMIBCompliances.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IgnitionStatus':IgnitionStatus,'ciscoIgnitionMIB':ciscoIgnitionMIB,'ipmMIBStatus':ipmMIBStatus,'ipmIgnitionStatusTable':ipmIgnitionStatusTable,'ipmIgnitionStatusEntry':ipmIgnitionStatusEntry,_D:ipmIgnitionStatusIndex,_F:ipmIgnitionManagement,_G:ipmInputVoltage,_H:ipmIgnitionStatus,_I:ipmIgnitionSense,_J:ipmShutdownTimer,_K:ipmConfigBattery,'ipmMIBThreshold':ipmMIBThreshold,'ipmIgnitionThresholdTable':ipmIgnitionThresholdTable,'ipmIgnitionThresholdEntry':ipmIgnitionThresholdEntry,_E:ipmIgnitionThresholdIndex,_L:ipmUndervoltage,_M:ipmOvervoltage,_N:ipmSenseOn,_O:ipmSenseOff,_P:ipmUndervoltageTimer,_Q:ipmOvervoltageTimer,_R:ipmIgnitionOffTimer,'ipmMIBConform':ipmMIBConform,'ipmMIBCompliance':ipmMIBCompliance,'ipmMIBCompliances':ipmMIBCompliances,'ipmMIBGroups':ipmMIBGroups,_S:ipmIgnitionStatusMIBGroup,_T:ipmIgnitionThresholdMIBGroup})