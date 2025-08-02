_K='sysName'
_J='SNMPv2-MIB'
_I='adTrapInformSeqNum'
_H='ADTRAN-GENTRAPINFORM-MIB'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='adGenPseudowireCEMPhysicalPortIfIndex'
_D='ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPseudowireCEMAlarmProv,adGenPseudowireCEMAlarmsID,adGenPseudowireCEMEvents,adGenPseudowireCEMPhysicalPortIfIndex=mibBuilder.importSymbols(_D,'adGenPseudowireCEMAlarmProv','adGenPseudowireCEMAlarmsID','adGenPseudowireCEMEvents',_E)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
adTrapInformSeqNum,=mibBuilder.importSymbols(_H,_I)
ifIndex,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenPseudowireCEMAlarmModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,30,3,1))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmModuleIdentity.setRevisions(('2018-11-20 17:00','2014-07-01 17:00','2012-05-18 11:20'))
_AdGenPseudowireCEMAlarmProvTable_Object=MibTable
adGenPseudowireCEMAlarmProvTable=_AdGenPseudowireCEMAlarmProvTable_Object((1,3,6,1,4,1,664,5,70,30,7,1))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmProvTable.setStatus(_A)
_AdGenPseudowireCEMAlarmProvTableEntry_Object=MibTableRow
adGenPseudowireCEMAlarmProvTableEntry=_AdGenPseudowireCEMAlarmProvTableEntry_Object((1,3,6,1,4,1,664,5,70,30,7,1,1))
adGenPseudowireCEMAlarmProvTableEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmProvTableEntry.setStatus(_A)
_AdGenPseudowireCEMFarEndLOSAlarmEnable_Type=TruthValue
_AdGenPseudowireCEMFarEndLOSAlarmEnable_Object=MibTableColumn
adGenPseudowireCEMFarEndLOSAlarmEnable=_AdGenPseudowireCEMFarEndLOSAlarmEnable_Object((1,3,6,1,4,1,664,5,70,30,7,1,1,1),_AdGenPseudowireCEMFarEndLOSAlarmEnable_Type())
adGenPseudowireCEMFarEndLOSAlarmEnable.setMaxAccess('read-create')
if mibBuilder.loadTexts:adGenPseudowireCEMFarEndLOSAlarmEnable.setStatus(_A)
adGenPseudowireCEMAlarmFarEndLOSClear=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,1))
adGenPseudowireCEMAlarmFarEndLOSClear.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmFarEndLOSClear.setStatus(_A)
adGenPseudowireCEMAlarmFarEndLOSActive=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,2))
adGenPseudowireCEMAlarmFarEndLOSActive.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmFarEndLOSActive.setStatus(_A)
adGenPseudowireCEMAlarmNearEndLPSClear=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,3))
adGenPseudowireCEMAlarmNearEndLPSClear.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmNearEndLPSClear.setStatus(_A)
adGenPseudowireCEMAlarmNearEndLPSActive=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,4))
adGenPseudowireCEMAlarmNearEndLPSActive.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmNearEndLPSActive.setStatus(_A)
adGenPseudowireCEMAlarmFarEndLPSClear=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,5))
adGenPseudowireCEMAlarmFarEndLPSClear.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmFarEndLPSClear.setStatus(_A)
adGenPseudowireCEMAlarmFarEndLPSActive=NotificationType((1,3,6,1,4,1,664,5,70,30,6,0,6))
adGenPseudowireCEMAlarmFarEndLPSActive.setObjects(*((_H,_I),(_J,_K),(_F,_G),(_B,_C),(_D,_E)))
if mibBuilder.loadTexts:adGenPseudowireCEMAlarmFarEndLPSActive.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GENERIC-PSEUDOWIRE-CEM-ALARM-MIB',**{'adGenPseudowireCEMAlarmFarEndLOSClear':adGenPseudowireCEMAlarmFarEndLOSClear,'adGenPseudowireCEMAlarmFarEndLOSActive':adGenPseudowireCEMAlarmFarEndLOSActive,'adGenPseudowireCEMAlarmNearEndLPSClear':adGenPseudowireCEMAlarmNearEndLPSClear,'adGenPseudowireCEMAlarmNearEndLPSActive':adGenPseudowireCEMAlarmNearEndLPSActive,'adGenPseudowireCEMAlarmFarEndLPSClear':adGenPseudowireCEMAlarmFarEndLPSClear,'adGenPseudowireCEMAlarmFarEndLPSActive':adGenPseudowireCEMAlarmFarEndLPSActive,'adGenPseudowireCEMAlarmProvTable':adGenPseudowireCEMAlarmProvTable,'adGenPseudowireCEMAlarmProvTableEntry':adGenPseudowireCEMAlarmProvTableEntry,'adGenPseudowireCEMFarEndLOSAlarmEnable':adGenPseudowireCEMFarEndLOSAlarmEnable,'adGenPseudowireCEMAlarmModuleIdentity':adGenPseudowireCEMAlarmModuleIdentity})