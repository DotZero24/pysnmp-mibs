_J='eltMesLbdVlanBasedVlanState'
_I='eltMesLbdVlanBasedVlanStateVlan'
_H='eltMesLbdVlanBasedVlanStatePort'
_G='eltMesLbdVlanBasedPort'
_F='Integer32'
_E='ELTEX-LBD-MIB'
_D='OctetString'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
VlanList1,VlanList2,VlanList3,VlanList4=mibBuilder.importSymbols('RADLAN-BRIDGEMIBOBJECTS-MIB','VlanList1','VlanList2','VlanList3','VlanList4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
_EltMesLbd_ObjectIdentity=ObjectIdentity
eltMesLbd=_EltMesLbd_ObjectIdentity((1,3,6,1,4,1,35265,1,23,127))
_EltMesLbdNotif_ObjectIdentity=ObjectIdentity
eltMesLbdNotif=_EltMesLbdNotif_ObjectIdentity((1,3,6,1,4,1,35265,1,23,127,0))
_EltMesLbdVlanBased_Type=TruthValue
_EltMesLbdVlanBased_Object=MibScalar
eltMesLbdVlanBased=_EltMesLbdVlanBased_Object((1,3,6,1,4,1,35265,1,23,127,1),_EltMesLbdVlanBased_Type())
eltMesLbdVlanBased.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBased.setStatus(_A)
class _EltMesLbdVlanBasedRecoveryTime_Type(Integer32):defaultValue=0
_EltMesLbdVlanBasedRecoveryTime_Type.__name__=_F
_EltMesLbdVlanBasedRecoveryTime_Object=MibScalar
eltMesLbdVlanBasedRecoveryTime=_EltMesLbdVlanBasedRecoveryTime_Object((1,3,6,1,4,1,35265,1,23,127,2),_EltMesLbdVlanBasedRecoveryTime_Type())
eltMesLbdVlanBasedRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBasedRecoveryTime.setStatus(_A)
if mibBuilder.loadTexts:eltMesLbdVlanBasedRecoveryTime.setUnits('seconds')
_EltMesLbdVlanBasedPortTable_Object=MibTable
eltMesLbdVlanBasedPortTable=_EltMesLbdVlanBasedPortTable_Object((1,3,6,1,4,1,35265,1,23,127,3))
if mibBuilder.loadTexts:eltMesLbdVlanBasedPortTable.setStatus(_A)
_EltMesLbdVlanBasedPortEntry_Object=MibTableRow
eltMesLbdVlanBasedPortEntry=_EltMesLbdVlanBasedPortEntry_Object((1,3,6,1,4,1,35265,1,23,127,3,1))
eltMesLbdVlanBasedPortEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:eltMesLbdVlanBasedPortEntry.setStatus(_A)
_EltMesLbdVlanBasedPort_Type=InterfaceIndex
_EltMesLbdVlanBasedPort_Object=MibTableColumn
eltMesLbdVlanBasedPort=_EltMesLbdVlanBasedPort_Object((1,3,6,1,4,1,35265,1,23,127,3,1,1),_EltMesLbdVlanBasedPort_Type())
eltMesLbdVlanBasedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedPort.setStatus(_A)
class _EltMesLbdVlanBasedVlanId1To1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesLbdVlanBasedVlanId1To1024_Type.__name__=_D
_EltMesLbdVlanBasedVlanId1To1024_Object=MibTableColumn
eltMesLbdVlanBasedVlanId1To1024=_EltMesLbdVlanBasedVlanId1To1024_Object((1,3,6,1,4,1,35265,1,23,127,3,1,2),_EltMesLbdVlanBasedVlanId1To1024_Type())
eltMesLbdVlanBasedVlanId1To1024.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanId1To1024.setStatus(_A)
class _EltMesLbdVlanBasedVlanId1025To2048_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesLbdVlanBasedVlanId1025To2048_Type.__name__=_D
_EltMesLbdVlanBasedVlanId1025To2048_Object=MibTableColumn
eltMesLbdVlanBasedVlanId1025To2048=_EltMesLbdVlanBasedVlanId1025To2048_Object((1,3,6,1,4,1,35265,1,23,127,3,1,3),_EltMesLbdVlanBasedVlanId1025To2048_Type())
eltMesLbdVlanBasedVlanId1025To2048.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanId1025To2048.setStatus(_A)
class _EltMesLbdVlanBasedVlanId2049To3072_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesLbdVlanBasedVlanId2049To3072_Type.__name__=_D
_EltMesLbdVlanBasedVlanId2049To3072_Object=MibTableColumn
eltMesLbdVlanBasedVlanId2049To3072=_EltMesLbdVlanBasedVlanId2049To3072_Object((1,3,6,1,4,1,35265,1,23,127,3,1,4),_EltMesLbdVlanBasedVlanId2049To3072_Type())
eltMesLbdVlanBasedVlanId2049To3072.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanId2049To3072.setStatus(_A)
class _EltMesLbdVlanBasedVlanId3073To4094_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesLbdVlanBasedVlanId3073To4094_Type.__name__=_D
_EltMesLbdVlanBasedVlanId3073To4094_Object=MibTableColumn
eltMesLbdVlanBasedVlanId3073To4094=_EltMesLbdVlanBasedVlanId3073To4094_Object((1,3,6,1,4,1,35265,1,23,127,3,1,5),_EltMesLbdVlanBasedVlanId3073To4094_Type())
eltMesLbdVlanBasedVlanId3073To4094.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanId3073To4094.setStatus(_A)
_EltMesLbdVlanBasedVlanStateTable_Object=MibTable
eltMesLbdVlanBasedVlanStateTable=_EltMesLbdVlanBasedVlanStateTable_Object((1,3,6,1,4,1,35265,1,23,127,4))
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanStateTable.setStatus(_A)
_EltMesLbdVlanBasedVlanStateEntry_Object=MibTableRow
eltMesLbdVlanBasedVlanStateEntry=_EltMesLbdVlanBasedVlanStateEntry_Object((1,3,6,1,4,1,35265,1,23,127,4,1))
eltMesLbdVlanBasedVlanStateEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanStateEntry.setStatus(_A)
_EltMesLbdVlanBasedVlanStatePort_Type=InterfaceIndex
_EltMesLbdVlanBasedVlanStatePort_Object=MibTableColumn
eltMesLbdVlanBasedVlanStatePort=_EltMesLbdVlanBasedVlanStatePort_Object((1,3,6,1,4,1,35265,1,23,127,4,1,1),_EltMesLbdVlanBasedVlanStatePort_Type())
eltMesLbdVlanBasedVlanStatePort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanStatePort.setStatus(_A)
_EltMesLbdVlanBasedVlanStateVlan_Type=VlanIndex
_EltMesLbdVlanBasedVlanStateVlan_Object=MibTableColumn
eltMesLbdVlanBasedVlanStateVlan=_EltMesLbdVlanBasedVlanStateVlan_Object((1,3,6,1,4,1,35265,1,23,127,4,1,2),_EltMesLbdVlanBasedVlanStateVlan_Type())
eltMesLbdVlanBasedVlanStateVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanStateVlan.setStatus(_A)
class _EltMesLbdVlanBasedVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('blocked',2)))
_EltMesLbdVlanBasedVlanState_Type.__name__=_F
_EltMesLbdVlanBasedVlanState_Object=MibTableColumn
eltMesLbdVlanBasedVlanState=_EltMesLbdVlanBasedVlanState_Object((1,3,6,1,4,1,35265,1,23,127,4,1,3),_EltMesLbdVlanBasedVlanState_Type())
eltMesLbdVlanBasedVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanState.setStatus(_A)
_EltMesLbdVlanBasedGlobals_ObjectIdentity=ObjectIdentity
eltMesLbdVlanBasedGlobals=_EltMesLbdVlanBasedGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,23,127,5))
_EltMesLbdVlanBasedGlobalsId1To1024_Type=VlanList1
_EltMesLbdVlanBasedGlobalsId1To1024_Object=MibScalar
eltMesLbdVlanBasedGlobalsId1To1024=_EltMesLbdVlanBasedGlobalsId1To1024_Object((1,3,6,1,4,1,35265,1,23,127,5,1),_EltMesLbdVlanBasedGlobalsId1To1024_Type())
eltMesLbdVlanBasedGlobalsId1To1024.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBasedGlobalsId1To1024.setStatus(_A)
_EltMesLbdVlanBasedGlobalsId1025To2048_Type=VlanList2
_EltMesLbdVlanBasedGlobalsId1025To2048_Object=MibScalar
eltMesLbdVlanBasedGlobalsId1025To2048=_EltMesLbdVlanBasedGlobalsId1025To2048_Object((1,3,6,1,4,1,35265,1,23,127,5,2),_EltMesLbdVlanBasedGlobalsId1025To2048_Type())
eltMesLbdVlanBasedGlobalsId1025To2048.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBasedGlobalsId1025To2048.setStatus(_A)
_EltMesLbdVlanBasedGlobalsId2049To3072_Type=VlanList3
_EltMesLbdVlanBasedGlobalsId2049To3072_Object=MibScalar
eltMesLbdVlanBasedGlobalsId2049To3072=_EltMesLbdVlanBasedGlobalsId2049To3072_Object((1,3,6,1,4,1,35265,1,23,127,5,3),_EltMesLbdVlanBasedGlobalsId2049To3072_Type())
eltMesLbdVlanBasedGlobalsId2049To3072.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBasedGlobalsId2049To3072.setStatus(_A)
_EltMesLbdVlanBasedGlobalsId3073To4094_Type=VlanList4
_EltMesLbdVlanBasedGlobalsId3073To4094_Object=MibScalar
eltMesLbdVlanBasedGlobalsId3073To4094=_EltMesLbdVlanBasedGlobalsId3073To4094_Object((1,3,6,1,4,1,35265,1,23,127,5,4),_EltMesLbdVlanBasedGlobalsId3073To4094_Type())
eltMesLbdVlanBasedGlobalsId3073To4094.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesLbdVlanBasedGlobalsId3073To4094.setStatus(_A)
eltMesLbdVlanBasedVlanNotif=NotificationType((1,3,6,1,4,1,35265,1,23,127,0,1))
eltMesLbdVlanBasedVlanNotif.setObjects((_E,_J))
if mibBuilder.loadTexts:eltMesLbdVlanBasedVlanNotif.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'eltMesLbd':eltMesLbd,'eltMesLbdNotif':eltMesLbdNotif,'eltMesLbdVlanBasedVlanNotif':eltMesLbdVlanBasedVlanNotif,'eltMesLbdVlanBased':eltMesLbdVlanBased,'eltMesLbdVlanBasedRecoveryTime':eltMesLbdVlanBasedRecoveryTime,'eltMesLbdVlanBasedPortTable':eltMesLbdVlanBasedPortTable,'eltMesLbdVlanBasedPortEntry':eltMesLbdVlanBasedPortEntry,_G:eltMesLbdVlanBasedPort,'eltMesLbdVlanBasedVlanId1To1024':eltMesLbdVlanBasedVlanId1To1024,'eltMesLbdVlanBasedVlanId1025To2048':eltMesLbdVlanBasedVlanId1025To2048,'eltMesLbdVlanBasedVlanId2049To3072':eltMesLbdVlanBasedVlanId2049To3072,'eltMesLbdVlanBasedVlanId3073To4094':eltMesLbdVlanBasedVlanId3073To4094,'eltMesLbdVlanBasedVlanStateTable':eltMesLbdVlanBasedVlanStateTable,'eltMesLbdVlanBasedVlanStateEntry':eltMesLbdVlanBasedVlanStateEntry,_H:eltMesLbdVlanBasedVlanStatePort,_I:eltMesLbdVlanBasedVlanStateVlan,_J:eltMesLbdVlanBasedVlanState,'eltMesLbdVlanBasedGlobals':eltMesLbdVlanBasedGlobals,'eltMesLbdVlanBasedGlobalsId1To1024':eltMesLbdVlanBasedGlobalsId1To1024,'eltMesLbdVlanBasedGlobalsId1025To2048':eltMesLbdVlanBasedGlobalsId1025To2048,'eltMesLbdVlanBasedGlobalsId2049To3072':eltMesLbdVlanBasedGlobalsId2049To3072,'eltMesLbdVlanBasedGlobalsId3073To4094':eltMesLbdVlanBasedGlobalsId3073To4094})