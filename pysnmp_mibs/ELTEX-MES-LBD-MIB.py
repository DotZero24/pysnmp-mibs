_J='eltLbdVlanBasedVlanState'
_I='eltLbdVlanBasedVlanStateVlan'
_H='eltLbdVlanBasedVlanStatePort'
_G='eltLbdVlanBasedPort'
_F='read-write'
_E='Integer32'
_D='ELTEX-MES-LBD-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
_EltMesLbd_ObjectIdentity=ObjectIdentity
eltMesLbd=_EltMesLbd_ObjectIdentity((1,3,6,1,4,1,35265,1,23,127))
_EltMesLbdNotif_ObjectIdentity=ObjectIdentity
eltMesLbdNotif=_EltMesLbdNotif_ObjectIdentity((1,3,6,1,4,1,35265,1,23,127,0))
_EltLbdVlanBased_Type=TruthValue
_EltLbdVlanBased_Object=MibScalar
eltLbdVlanBased=_EltLbdVlanBased_Object((1,3,6,1,4,1,35265,1,23,127,1),_EltLbdVlanBased_Type())
eltLbdVlanBased.setMaxAccess(_F)
if mibBuilder.loadTexts:eltLbdVlanBased.setStatus(_A)
_EltLbdVlanBasedRecoveryTime_Type=Integer32
_EltLbdVlanBasedRecoveryTime_Object=MibScalar
eltLbdVlanBasedRecoveryTime=_EltLbdVlanBasedRecoveryTime_Object((1,3,6,1,4,1,35265,1,23,127,2),_EltLbdVlanBasedRecoveryTime_Type())
eltLbdVlanBasedRecoveryTime.setMaxAccess(_F)
if mibBuilder.loadTexts:eltLbdVlanBasedRecoveryTime.setStatus(_A)
if mibBuilder.loadTexts:eltLbdVlanBasedRecoveryTime.setUnits('seconds')
_EltLbdVlanBasedPortTable_Object=MibTable
eltLbdVlanBasedPortTable=_EltLbdVlanBasedPortTable_Object((1,3,6,1,4,1,35265,1,23,127,3))
if mibBuilder.loadTexts:eltLbdVlanBasedPortTable.setStatus(_A)
_EltLbdVlanBasedPortEntry_Object=MibTableRow
eltLbdVlanBasedPortEntry=_EltLbdVlanBasedPortEntry_Object((1,3,6,1,4,1,35265,1,23,127,3,1))
eltLbdVlanBasedPortEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:eltLbdVlanBasedPortEntry.setStatus(_A)
_EltLbdVlanBasedPort_Type=InterfaceIndex
_EltLbdVlanBasedPort_Object=MibTableColumn
eltLbdVlanBasedPort=_EltLbdVlanBasedPort_Object((1,3,6,1,4,1,35265,1,23,127,3,1,1),_EltLbdVlanBasedPort_Type())
eltLbdVlanBasedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedPort.setStatus(_A)
class _EltLbdVlanBasedVlanId1To1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltLbdVlanBasedVlanId1To1024_Type.__name__=_C
_EltLbdVlanBasedVlanId1To1024_Object=MibTableColumn
eltLbdVlanBasedVlanId1To1024=_EltLbdVlanBasedVlanId1To1024_Object((1,3,6,1,4,1,35265,1,23,127,3,1,2),_EltLbdVlanBasedVlanId1To1024_Type())
eltLbdVlanBasedVlanId1To1024.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanId1To1024.setStatus(_A)
class _EltLbdVlanBasedVlanId1025To2048_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltLbdVlanBasedVlanId1025To2048_Type.__name__=_C
_EltLbdVlanBasedVlanId1025To2048_Object=MibTableColumn
eltLbdVlanBasedVlanId1025To2048=_EltLbdVlanBasedVlanId1025To2048_Object((1,3,6,1,4,1,35265,1,23,127,3,1,3),_EltLbdVlanBasedVlanId1025To2048_Type())
eltLbdVlanBasedVlanId1025To2048.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanId1025To2048.setStatus(_A)
class _EltLbdVlanBasedVlanId2049To3072_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltLbdVlanBasedVlanId2049To3072_Type.__name__=_C
_EltLbdVlanBasedVlanId2049To3072_Object=MibTableColumn
eltLbdVlanBasedVlanId2049To3072=_EltLbdVlanBasedVlanId2049To3072_Object((1,3,6,1,4,1,35265,1,23,127,3,1,4),_EltLbdVlanBasedVlanId2049To3072_Type())
eltLbdVlanBasedVlanId2049To3072.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanId2049To3072.setStatus(_A)
class _EltLbdVlanBasedVlanId3073To4094_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltLbdVlanBasedVlanId3073To4094_Type.__name__=_C
_EltLbdVlanBasedVlanId3073To4094_Object=MibTableColumn
eltLbdVlanBasedVlanId3073To4094=_EltLbdVlanBasedVlanId3073To4094_Object((1,3,6,1,4,1,35265,1,23,127,3,1,5),_EltLbdVlanBasedVlanId3073To4094_Type())
eltLbdVlanBasedVlanId3073To4094.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanId3073To4094.setStatus(_A)
_EltLbdVlanBasedVlanStateTable_Object=MibTable
eltLbdVlanBasedVlanStateTable=_EltLbdVlanBasedVlanStateTable_Object((1,3,6,1,4,1,35265,1,23,127,4))
if mibBuilder.loadTexts:eltLbdVlanBasedVlanStateTable.setStatus(_A)
_EltLbdVlanBasedVlanStateEntry_Object=MibTableRow
eltLbdVlanBasedVlanStateEntry=_EltLbdVlanBasedVlanStateEntry_Object((1,3,6,1,4,1,35265,1,23,127,4,1))
eltLbdVlanBasedVlanStateEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:eltLbdVlanBasedVlanStateEntry.setStatus(_A)
_EltLbdVlanBasedVlanStatePort_Type=InterfaceIndex
_EltLbdVlanBasedVlanStatePort_Object=MibTableColumn
eltLbdVlanBasedVlanStatePort=_EltLbdVlanBasedVlanStatePort_Object((1,3,6,1,4,1,35265,1,23,127,4,1,1),_EltLbdVlanBasedVlanStatePort_Type())
eltLbdVlanBasedVlanStatePort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanStatePort.setStatus(_A)
_EltLbdVlanBasedVlanStateVlan_Type=VlanIndex
_EltLbdVlanBasedVlanStateVlan_Object=MibTableColumn
eltLbdVlanBasedVlanStateVlan=_EltLbdVlanBasedVlanStateVlan_Object((1,3,6,1,4,1,35265,1,23,127,4,1,2),_EltLbdVlanBasedVlanStateVlan_Type())
eltLbdVlanBasedVlanStateVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanStateVlan.setStatus(_A)
class _EltLbdVlanBasedVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('blocked',2)))
_EltLbdVlanBasedVlanState_Type.__name__=_E
_EltLbdVlanBasedVlanState_Object=MibTableColumn
eltLbdVlanBasedVlanState=_EltLbdVlanBasedVlanState_Object((1,3,6,1,4,1,35265,1,23,127,4,1,3),_EltLbdVlanBasedVlanState_Type())
eltLbdVlanBasedVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltLbdVlanBasedVlanState.setStatus(_A)
eltLbdVlanBasedVlanNotif=NotificationType((1,3,6,1,4,1,35265,1,23,127,0,1))
eltLbdVlanBasedVlanNotif.setObjects((_D,_J))
if mibBuilder.loadTexts:eltLbdVlanBasedVlanNotif.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eltMesLbd':eltMesLbd,'eltMesLbdNotif':eltMesLbdNotif,'eltLbdVlanBasedVlanNotif':eltLbdVlanBasedVlanNotif,'eltLbdVlanBased':eltLbdVlanBased,'eltLbdVlanBasedRecoveryTime':eltLbdVlanBasedRecoveryTime,'eltLbdVlanBasedPortTable':eltLbdVlanBasedPortTable,'eltLbdVlanBasedPortEntry':eltLbdVlanBasedPortEntry,_G:eltLbdVlanBasedPort,'eltLbdVlanBasedVlanId1To1024':eltLbdVlanBasedVlanId1To1024,'eltLbdVlanBasedVlanId1025To2048':eltLbdVlanBasedVlanId1025To2048,'eltLbdVlanBasedVlanId2049To3072':eltLbdVlanBasedVlanId2049To3072,'eltLbdVlanBasedVlanId3073To4094':eltLbdVlanBasedVlanId3073To4094,'eltLbdVlanBasedVlanStateTable':eltLbdVlanBasedVlanStateTable,'eltLbdVlanBasedVlanStateEntry':eltLbdVlanBasedVlanStateEntry,_H:eltLbdVlanBasedVlanStatePort,_I:eltLbdVlanBasedVlanStateVlan,_J:eltLbdVlanBasedVlanState})