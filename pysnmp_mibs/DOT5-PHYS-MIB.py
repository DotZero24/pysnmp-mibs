_c='dot5PhysMgmtBoardAuxRingSpeedAuxRing'
_b='dot5PhysMgmtBoardAuxRingSpeedBoardId'
_a='dot5PhysMgmtDeviceRingSpeedRing'
_Z='dot5PhysMgmtPortRingPortId'
_Y='dot5PhysMgmtPortRingBoardId'
_X='dot5PhysMgmtPortStnPortId'
_W='dot5PhysMgmtPortStnBoardId'
_V='disable'
_U='dot5PhysMgmtPortCommonPortId'
_T='dot5PhysMgmtPortCommonBoardId'
_S='ringOut'
_R='ringIn'
_Q='notSupported'
_P='dot5PhysMgmtBoardId'
_O='faultDetected'
_N='noFaultDetected'
_M='hundredMegaBits'
_L='sixteenMegaBits'
_K='tenMegaBits'
_J='fourMegaBits'
_I='unknown'
_H='DisplayString'
_G='noEnable'
_F='enable'
_E='DOT5-PHYS-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDot5PhysMgmt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDot5PhysMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_Dot5PhysMgmtRev1_ObjectIdentity=ObjectIdentity
dot5PhysMgmtRev1=_Dot5PhysMgmtRev1_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1))
_Dot5PhysMgmtDevice_ObjectIdentity=ObjectIdentity
dot5PhysMgmtDevice=_Dot5PhysMgmtDevice_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,1))
_Dot5PhysMgmtDeviceRingCount_Type=Integer32
_Dot5PhysMgmtDeviceRingCount_Object=MibScalar
dot5PhysMgmtDeviceRingCount=_Dot5PhysMgmtDeviceRingCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,1),_Dot5PhysMgmtDeviceRingCount_Type())
dot5PhysMgmtDeviceRingCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingCount.setStatus(_A)
_Dot5PhysMgmtDevicePortCount_Type=Integer32
_Dot5PhysMgmtDevicePortCount_Object=MibScalar
dot5PhysMgmtDevicePortCount=_Dot5PhysMgmtDevicePortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,2),_Dot5PhysMgmtDevicePortCount_Type())
dot5PhysMgmtDevicePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDevicePortCount.setStatus(_A)
class _Dot5PhysMgmtDevicePortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtDevicePortsEnable_Type.__name__=_C
_Dot5PhysMgmtDevicePortsEnable_Object=MibScalar
dot5PhysMgmtDevicePortsEnable=_Dot5PhysMgmtDevicePortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,3),_Dot5PhysMgmtDevicePortsEnable_Type())
dot5PhysMgmtDevicePortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtDevicePortsEnable.setStatus(_A)
_Dot5PhysMgmtDevicePortsOn_Type=Integer32
_Dot5PhysMgmtDevicePortsOn_Object=MibScalar
dot5PhysMgmtDevicePortsOn=_Dot5PhysMgmtDevicePortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,4),_Dot5PhysMgmtDevicePortsOn_Type())
dot5PhysMgmtDevicePortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDevicePortsOn.setStatus(_A)
_Dot5PhysMgmtDevicePortsOper_Type=Integer32
_Dot5PhysMgmtDevicePortsOper_Object=MibScalar
dot5PhysMgmtDevicePortsOper=_Dot5PhysMgmtDevicePortsOper_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,5),_Dot5PhysMgmtDevicePortsOper_Type())
dot5PhysMgmtDevicePortsOper.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDevicePortsOper.setStatus(_A)
_Dot5PhysMgmtDeviceStnPortCount_Type=Integer32
_Dot5PhysMgmtDeviceStnPortCount_Object=MibScalar
dot5PhysMgmtDeviceStnPortCount=_Dot5PhysMgmtDeviceStnPortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,6),_Dot5PhysMgmtDeviceStnPortCount_Type())
dot5PhysMgmtDeviceStnPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceStnPortCount.setStatus(_A)
class _Dot5PhysMgmtDeviceStnPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtDeviceStnPortsEnable_Type.__name__=_C
_Dot5PhysMgmtDeviceStnPortsEnable_Object=MibScalar
dot5PhysMgmtDeviceStnPortsEnable=_Dot5PhysMgmtDeviceStnPortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,7),_Dot5PhysMgmtDeviceStnPortsEnable_Type())
dot5PhysMgmtDeviceStnPortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceStnPortsEnable.setStatus(_A)
_Dot5PhysMgmtDeviceStnPortsOn_Type=Integer32
_Dot5PhysMgmtDeviceStnPortsOn_Object=MibScalar
dot5PhysMgmtDeviceStnPortsOn=_Dot5PhysMgmtDeviceStnPortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,8),_Dot5PhysMgmtDeviceStnPortsOn_Type())
dot5PhysMgmtDeviceStnPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceStnPortsOn.setStatus(_A)
_Dot5PhysMgmtDeviceRingPortCount_Type=Integer32
_Dot5PhysMgmtDeviceRingPortCount_Object=MibScalar
dot5PhysMgmtDeviceRingPortCount=_Dot5PhysMgmtDeviceRingPortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,9),_Dot5PhysMgmtDeviceRingPortCount_Type())
dot5PhysMgmtDeviceRingPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingPortCount.setStatus(_A)
class _Dot5PhysMgmtDeviceRingPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtDeviceRingPortsEnable_Type.__name__=_C
_Dot5PhysMgmtDeviceRingPortsEnable_Object=MibScalar
dot5PhysMgmtDeviceRingPortsEnable=_Dot5PhysMgmtDeviceRingPortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,10),_Dot5PhysMgmtDeviceRingPortsEnable_Type())
dot5PhysMgmtDeviceRingPortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingPortsEnable.setStatus(_A)
_Dot5PhysMgmtDeviceRingPortsOn_Type=Integer32
_Dot5PhysMgmtDeviceRingPortsOn_Object=MibScalar
dot5PhysMgmtDeviceRingPortsOn=_Dot5PhysMgmtDeviceRingPortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,11),_Dot5PhysMgmtDeviceRingPortsOn_Type())
dot5PhysMgmtDeviceRingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingPortsOn.setStatus(_A)
_Dot5PhysMgmtDevicePortAssociationChanges_Type=Counter32
_Dot5PhysMgmtDevicePortAssociationChanges_Object=MibScalar
dot5PhysMgmtDevicePortAssociationChanges=_Dot5PhysMgmtDevicePortAssociationChanges_Object((1,3,6,1,4,1,52,4,1,1,6,1,1,12),_Dot5PhysMgmtDevicePortAssociationChanges_Type())
dot5PhysMgmtDevicePortAssociationChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDevicePortAssociationChanges.setStatus(_A)
_Dot5PhysMgmtBoard_ObjectIdentity=ObjectIdentity
dot5PhysMgmtBoard=_Dot5PhysMgmtBoard_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,2))
_Dot5PhysMgmtBoardTable_Object=MibTable
dot5PhysMgmtBoardTable=_Dot5PhysMgmtBoardTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1))
if mibBuilder.loadTexts:dot5PhysMgmtBoardTable.setStatus(_A)
_Dot5PhysMgmtBoardEntry_Object=MibTableRow
dot5PhysMgmtBoardEntry=_Dot5PhysMgmtBoardEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1))
dot5PhysMgmtBoardEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:dot5PhysMgmtBoardEntry.setStatus(_A)
_Dot5PhysMgmtBoardId_Type=Integer32
_Dot5PhysMgmtBoardId_Object=MibTableColumn
dot5PhysMgmtBoardId=_Dot5PhysMgmtBoardId_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,1),_Dot5PhysMgmtBoardId_Type())
dot5PhysMgmtBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardId.setStatus(_A)
class _Dot5PhysMgmtBoardDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outsideDomain',1),('withinDomain',2)))
_Dot5PhysMgmtBoardDomain_Type.__name__=_C
_Dot5PhysMgmtBoardDomain_Object=MibTableColumn
dot5PhysMgmtBoardDomain=_Dot5PhysMgmtBoardDomain_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,2),_Dot5PhysMgmtBoardDomain_Type())
dot5PhysMgmtBoardDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDomain.setStatus(_A)
class _Dot5PhysMgmtBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_Dot5PhysMgmtBoardName_Type.__name__=_H
_Dot5PhysMgmtBoardName_Object=MibTableColumn
dot5PhysMgmtBoardName=_Dot5PhysMgmtBoardName_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,3),_Dot5PhysMgmtBoardName_Type())
dot5PhysMgmtBoardName.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardName.setStatus(_A)
class _Dot5PhysMgmtBoardDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Dot5PhysMgmtBoardDesc_Type.__name__=_H
_Dot5PhysMgmtBoardDesc_Object=MibTableColumn
dot5PhysMgmtBoardDesc=_Dot5PhysMgmtBoardDesc_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,4),_Dot5PhysMgmtBoardDesc_Type())
dot5PhysMgmtBoardDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDesc.setStatus(_A)
_Dot5PhysMgmtBoardDot5PortCount_Type=Integer32
_Dot5PhysMgmtBoardDot5PortCount_Object=MibTableColumn
dot5PhysMgmtBoardDot5PortCount=_Dot5PhysMgmtBoardDot5PortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,5),_Dot5PhysMgmtBoardDot5PortCount_Type())
dot5PhysMgmtBoardDot5PortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5PortCount.setStatus(_A)
class _Dot5PhysMgmtBoardDot5PortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtBoardDot5PortsEnable_Type.__name__=_C
_Dot5PhysMgmtBoardDot5PortsEnable_Object=MibTableColumn
dot5PhysMgmtBoardDot5PortsEnable=_Dot5PhysMgmtBoardDot5PortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,6),_Dot5PhysMgmtBoardDot5PortsEnable_Type())
dot5PhysMgmtBoardDot5PortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5PortsEnable.setStatus(_A)
_Dot5PhysMgmtBoardDot5PortsOn_Type=Integer32
_Dot5PhysMgmtBoardDot5PortsOn_Object=MibTableColumn
dot5PhysMgmtBoardDot5PortsOn=_Dot5PhysMgmtBoardDot5PortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,7),_Dot5PhysMgmtBoardDot5PortsOn_Type())
dot5PhysMgmtBoardDot5PortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5PortsOn.setStatus(_A)
_Dot5PhysMgmtBoardDot5PortsOper_Type=Integer32
_Dot5PhysMgmtBoardDot5PortsOper_Object=MibTableColumn
dot5PhysMgmtBoardDot5PortsOper=_Dot5PhysMgmtBoardDot5PortsOper_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,8),_Dot5PhysMgmtBoardDot5PortsOper_Type())
dot5PhysMgmtBoardDot5PortsOper.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5PortsOper.setStatus(_A)
_Dot5PhysMgmtBoardDot5StnPortCount_Type=Integer32
_Dot5PhysMgmtBoardDot5StnPortCount_Object=MibTableColumn
dot5PhysMgmtBoardDot5StnPortCount=_Dot5PhysMgmtBoardDot5StnPortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,9),_Dot5PhysMgmtBoardDot5StnPortCount_Type())
dot5PhysMgmtBoardDot5StnPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5StnPortCount.setStatus(_A)
class _Dot5PhysMgmtBoardDot5StnPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtBoardDot5StnPortsEnable_Type.__name__=_C
_Dot5PhysMgmtBoardDot5StnPortsEnable_Object=MibTableColumn
dot5PhysMgmtBoardDot5StnPortsEnable=_Dot5PhysMgmtBoardDot5StnPortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,10),_Dot5PhysMgmtBoardDot5StnPortsEnable_Type())
dot5PhysMgmtBoardDot5StnPortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5StnPortsEnable.setStatus(_A)
_Dot5PhysMgmtBoardDot5StnPortsOn_Type=Integer32
_Dot5PhysMgmtBoardDot5StnPortsOn_Object=MibTableColumn
dot5PhysMgmtBoardDot5StnPortsOn=_Dot5PhysMgmtBoardDot5StnPortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,11),_Dot5PhysMgmtBoardDot5StnPortsOn_Type())
dot5PhysMgmtBoardDot5StnPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5StnPortsOn.setStatus(_A)
_Dot5PhysMgmtBoardDot5RingPortCount_Type=Integer32
_Dot5PhysMgmtBoardDot5RingPortCount_Object=MibTableColumn
dot5PhysMgmtBoardDot5RingPortCount=_Dot5PhysMgmtBoardDot5RingPortCount_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,12),_Dot5PhysMgmtBoardDot5RingPortCount_Type())
dot5PhysMgmtBoardDot5RingPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5RingPortCount.setStatus(_A)
class _Dot5PhysMgmtBoardDot5RingPortsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_Dot5PhysMgmtBoardDot5RingPortsEnable_Type.__name__=_C
_Dot5PhysMgmtBoardDot5RingPortsEnable_Object=MibTableColumn
dot5PhysMgmtBoardDot5RingPortsEnable=_Dot5PhysMgmtBoardDot5RingPortsEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,13),_Dot5PhysMgmtBoardDot5RingPortsEnable_Type())
dot5PhysMgmtBoardDot5RingPortsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5RingPortsEnable.setStatus(_A)
_Dot5PhysMgmtBoardDot5RingPortsOn_Type=Integer32
_Dot5PhysMgmtBoardDot5RingPortsOn_Object=MibTableColumn
dot5PhysMgmtBoardDot5RingPortsOn=_Dot5PhysMgmtBoardDot5RingPortsOn_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,14),_Dot5PhysMgmtBoardDot5RingPortsOn_Type())
dot5PhysMgmtBoardDot5RingPortsOn.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardDot5RingPortsOn.setStatus(_A)
class _Dot5PhysMgmtBoardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('managementMode',1),('autoMode',2),(_I,3)))
_Dot5PhysMgmtBoardMode_Type.__name__=_C
_Dot5PhysMgmtBoardMode_Object=MibTableColumn
dot5PhysMgmtBoardMode=_Dot5PhysMgmtBoardMode_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,15),_Dot5PhysMgmtBoardMode_Type())
dot5PhysMgmtBoardMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardMode.setStatus(_A)
class _Dot5PhysMgmtBoardSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,10,16,100)));namedValues=NamedValues(*((_I,1),(_J,4),(_K,10),(_L,16),(_M,100)))
_Dot5PhysMgmtBoardSpeed_Type.__name__=_C
_Dot5PhysMgmtBoardSpeed_Object=MibTableColumn
dot5PhysMgmtBoardSpeed=_Dot5PhysMgmtBoardSpeed_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,16),_Dot5PhysMgmtBoardSpeed_Type())
dot5PhysMgmtBoardSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardSpeed.setStatus(_A)
class _Dot5PhysMgmtBoardSpeedFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_Q,3)))
_Dot5PhysMgmtBoardSpeedFault_Type.__name__=_C
_Dot5PhysMgmtBoardSpeedFault_Object=MibTableColumn
dot5PhysMgmtBoardSpeedFault=_Dot5PhysMgmtBoardSpeedFault_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,17),_Dot5PhysMgmtBoardSpeedFault_Type())
dot5PhysMgmtBoardSpeedFault.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardSpeedFault.setStatus(_A)
class _Dot5PhysMgmtBoardSpeedFaultLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('fnb',2),(_R,3),(_S,4)))
_Dot5PhysMgmtBoardSpeedFaultLocation_Type.__name__=_C
_Dot5PhysMgmtBoardSpeedFaultLocation_Object=MibTableColumn
dot5PhysMgmtBoardSpeedFaultLocation=_Dot5PhysMgmtBoardSpeedFaultLocation_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,18),_Dot5PhysMgmtBoardSpeedFaultLocation_Type())
dot5PhysMgmtBoardSpeedFaultLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardSpeedFaultLocation.setStatus(_A)
class _Dot5PhysMgmtBoardPortAssociation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot5PhysMgmtBoardPortAssociation_Type.__name__=_C
_Dot5PhysMgmtBoardPortAssociation_Object=MibTableColumn
dot5PhysMgmtBoardPortAssociation=_Dot5PhysMgmtBoardPortAssociation_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,19),_Dot5PhysMgmtBoardPortAssociation_Type())
dot5PhysMgmtBoardPortAssociation.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardPortAssociation.setStatus(_A)
_Dot5PhysMgmtBoardPortAssociationChanges_Type=Counter32
_Dot5PhysMgmtBoardPortAssociationChanges_Object=MibTableColumn
dot5PhysMgmtBoardPortAssociationChanges=_Dot5PhysMgmtBoardPortAssociationChanges_Object((1,3,6,1,4,1,52,4,1,1,6,1,2,1,1,20),_Dot5PhysMgmtBoardPortAssociationChanges_Type())
dot5PhysMgmtBoardPortAssociationChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardPortAssociationChanges.setStatus(_A)
_Dot5PhysMgmtPort_ObjectIdentity=ObjectIdentity
dot5PhysMgmtPort=_Dot5PhysMgmtPort_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,3))
_Dot5PhysMgmtPortCommon_ObjectIdentity=ObjectIdentity
dot5PhysMgmtPortCommon=_Dot5PhysMgmtPortCommon_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,3,1))
_Dot5PhysMgmtPortCommonTable_Object=MibTable
dot5PhysMgmtPortCommonTable=_Dot5PhysMgmtPortCommonTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1))
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonTable.setStatus(_A)
_Dot5PhysMgmtPortCommonEntry_Object=MibTableRow
dot5PhysMgmtPortCommonEntry=_Dot5PhysMgmtPortCommonEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1))
dot5PhysMgmtPortCommonEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonEntry.setStatus(_A)
_Dot5PhysMgmtPortCommonPortId_Type=Integer32
_Dot5PhysMgmtPortCommonPortId_Object=MibTableColumn
dot5PhysMgmtPortCommonPortId=_Dot5PhysMgmtPortCommonPortId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,1),_Dot5PhysMgmtPortCommonPortId_Type())
dot5PhysMgmtPortCommonPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortId.setStatus(_A)
_Dot5PhysMgmtPortCommonBoardId_Type=Integer32
_Dot5PhysMgmtPortCommonBoardId_Object=MibTableColumn
dot5PhysMgmtPortCommonBoardId=_Dot5PhysMgmtPortCommonBoardId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,2),_Dot5PhysMgmtPortCommonBoardId_Type())
dot5PhysMgmtPortCommonBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonBoardId.setStatus(_A)
class _Dot5PhysMgmtPortCommonPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_Dot5PhysMgmtPortCommonPortName_Type.__name__=_H
_Dot5PhysMgmtPortCommonPortName_Object=MibTableColumn
dot5PhysMgmtPortCommonPortName=_Dot5PhysMgmtPortCommonPortName_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,3),_Dot5PhysMgmtPortCommonPortName_Type())
dot5PhysMgmtPortCommonPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortName.setStatus(_A)
class _Dot5PhysMgmtPortCommonPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_F,2)))
_Dot5PhysMgmtPortCommonPortAdminState_Type.__name__=_C
_Dot5PhysMgmtPortCommonPortAdminState_Object=MibTableColumn
dot5PhysMgmtPortCommonPortAdminState=_Dot5PhysMgmtPortCommonPortAdminState_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,4),_Dot5PhysMgmtPortCommonPortAdminState_Type())
dot5PhysMgmtPortCommonPortAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortAdminState.setStatus(_A)
class _Dot5PhysMgmtPortCommonPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notOperational',1),('operational',2)))
_Dot5PhysMgmtPortCommonPortOperState_Type.__name__=_C
_Dot5PhysMgmtPortCommonPortOperState_Object=MibTableColumn
dot5PhysMgmtPortCommonPortOperState=_Dot5PhysMgmtPortCommonPortOperState_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,5),_Dot5PhysMgmtPortCommonPortOperState_Type())
dot5PhysMgmtPortCommonPortOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortOperState.setStatus(_A)
_Dot5PhysMgmtPortCommonPortType_Type=ObjectIdentifier
_Dot5PhysMgmtPortCommonPortType_Object=MibTableColumn
dot5PhysMgmtPortCommonPortType=_Dot5PhysMgmtPortCommonPortType_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,6),_Dot5PhysMgmtPortCommonPortType_Type())
dot5PhysMgmtPortCommonPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortType.setStatus(_A)
class _Dot5PhysMgmtPortCommonSpeedFaultDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notDetectable',1),(_N,2),(_O,3)))
_Dot5PhysMgmtPortCommonSpeedFaultDetect_Type.__name__=_C
_Dot5PhysMgmtPortCommonSpeedFaultDetect_Object=MibTableColumn
dot5PhysMgmtPortCommonSpeedFaultDetect=_Dot5PhysMgmtPortCommonSpeedFaultDetect_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,7),_Dot5PhysMgmtPortCommonSpeedFaultDetect_Type())
dot5PhysMgmtPortCommonSpeedFaultDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonSpeedFaultDetect.setStatus(_A)
class _Dot5PhysMgmtPortCommonRingOutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notAvailable',1),(_V,2),(_F,3)))
_Dot5PhysMgmtPortCommonRingOutEnable_Type.__name__=_C
_Dot5PhysMgmtPortCommonRingOutEnable_Object=MibTableColumn
dot5PhysMgmtPortCommonRingOutEnable=_Dot5PhysMgmtPortCommonRingOutEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,8),_Dot5PhysMgmtPortCommonRingOutEnable_Type())
dot5PhysMgmtPortCommonRingOutEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonRingOutEnable.setStatus(_A)
class _Dot5PhysMgmtPortCommonPortAssociation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_Dot5PhysMgmtPortCommonPortAssociation_Type.__name__=_C
_Dot5PhysMgmtPortCommonPortAssociation_Object=MibTableColumn
dot5PhysMgmtPortCommonPortAssociation=_Dot5PhysMgmtPortCommonPortAssociation_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,9),_Dot5PhysMgmtPortCommonPortAssociation_Type())
dot5PhysMgmtPortCommonPortAssociation.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonPortAssociation.setStatus(_A)
_Dot5PhysMgmtPortCommonMauCompId_Type=Integer32
_Dot5PhysMgmtPortCommonMauCompId_Object=MibTableColumn
dot5PhysMgmtPortCommonMauCompId=_Dot5PhysMgmtPortCommonMauCompId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,1,1,1,10),_Dot5PhysMgmtPortCommonMauCompId_Type())
dot5PhysMgmtPortCommonMauCompId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortCommonMauCompId.setStatus(_A)
_Dot5PhysMgmtPortStn_ObjectIdentity=ObjectIdentity
dot5PhysMgmtPortStn=_Dot5PhysMgmtPortStn_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,3,2))
_Dot5PhysMgmtPortStnTable_Object=MibTable
dot5PhysMgmtPortStnTable=_Dot5PhysMgmtPortStnTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1))
if mibBuilder.loadTexts:dot5PhysMgmtPortStnTable.setStatus(_A)
_Dot5PhysMgmtPortStnEntry_Object=MibTableRow
dot5PhysMgmtPortStnEntry=_Dot5PhysMgmtPortStnEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1))
dot5PhysMgmtPortStnEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:dot5PhysMgmtPortStnEntry.setStatus(_A)
_Dot5PhysMgmtPortStnPortId_Type=Integer32
_Dot5PhysMgmtPortStnPortId_Object=MibTableColumn
dot5PhysMgmtPortStnPortId=_Dot5PhysMgmtPortStnPortId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1,1),_Dot5PhysMgmtPortStnPortId_Type())
dot5PhysMgmtPortStnPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortStnPortId.setStatus(_A)
_Dot5PhysMgmtPortStnBoardId_Type=Integer32
_Dot5PhysMgmtPortStnBoardId_Object=MibTableColumn
dot5PhysMgmtPortStnBoardId=_Dot5PhysMgmtPortStnBoardId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1,2),_Dot5PhysMgmtPortStnBoardId_Type())
dot5PhysMgmtPortStnBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortStnBoardId.setStatus(_A)
class _Dot5PhysMgmtPortStnPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLink',1),('link',2)))
_Dot5PhysMgmtPortStnPortLinkState_Type.__name__=_C
_Dot5PhysMgmtPortStnPortLinkState_Object=MibTableColumn
dot5PhysMgmtPortStnPortLinkState=_Dot5PhysMgmtPortStnPortLinkState_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1,3),_Dot5PhysMgmtPortStnPortLinkState_Type())
dot5PhysMgmtPortStnPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortStnPortLinkState.setStatus(_A)
_Dot5PhysMgmtPortStnPortLinkStateTime_Type=TimeTicks
_Dot5PhysMgmtPortStnPortLinkStateTime_Object=MibTableColumn
dot5PhysMgmtPortStnPortLinkStateTime=_Dot5PhysMgmtPortStnPortLinkStateTime_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1,4),_Dot5PhysMgmtPortStnPortLinkStateTime_Type())
dot5PhysMgmtPortStnPortLinkStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortStnPortLinkStateTime.setStatus(_A)
class _Dot5PhysMgmtPortStnInsertionTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_Dot5PhysMgmtPortStnInsertionTrapEnable_Type.__name__=_C
_Dot5PhysMgmtPortStnInsertionTrapEnable_Object=MibTableColumn
dot5PhysMgmtPortStnInsertionTrapEnable=_Dot5PhysMgmtPortStnInsertionTrapEnable_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,2,1,1,5),_Dot5PhysMgmtPortStnInsertionTrapEnable_Type())
dot5PhysMgmtPortStnInsertionTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortStnInsertionTrapEnable.setStatus(_A)
_Dot5PhysMgmtPortRing_ObjectIdentity=ObjectIdentity
dot5PhysMgmtPortRing=_Dot5PhysMgmtPortRing_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,3,3))
_Dot5PhysMgmtPortRingTable_Object=MibTable
dot5PhysMgmtPortRingTable=_Dot5PhysMgmtPortRingTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1))
if mibBuilder.loadTexts:dot5PhysMgmtPortRingTable.setStatus(_A)
_Dot5PhysMgmtPortRingEntry_Object=MibTableRow
dot5PhysMgmtPortRingEntry=_Dot5PhysMgmtPortRingEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1))
dot5PhysMgmtPortRingEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:dot5PhysMgmtPortRingEntry.setStatus(_A)
_Dot5PhysMgmtPortRingPortId_Type=Integer32
_Dot5PhysMgmtPortRingPortId_Object=MibTableColumn
dot5PhysMgmtPortRingPortId=_Dot5PhysMgmtPortRingPortId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,1),_Dot5PhysMgmtPortRingPortId_Type())
dot5PhysMgmtPortRingPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingPortId.setStatus(_A)
_Dot5PhysMgmtPortRingBoardId_Type=Integer32
_Dot5PhysMgmtPortRingBoardId_Object=MibTableColumn
dot5PhysMgmtPortRingBoardId=_Dot5PhysMgmtPortRingBoardId_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,2),_Dot5PhysMgmtPortRingBoardId_Type())
dot5PhysMgmtPortRingBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingBoardId.setStatus(_A)
class _Dot5PhysMgmtPortRingPortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAutowrap',1),('autowrap',2),('selectable',3)))
_Dot5PhysMgmtPortRingPortClass_Type.__name__=_C
_Dot5PhysMgmtPortRingPortClass_Object=MibTableColumn
dot5PhysMgmtPortRingPortClass=_Dot5PhysMgmtPortRingPortClass_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,3),_Dot5PhysMgmtPortRingPortClass_Type())
dot5PhysMgmtPortRingPortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingPortClass.setStatus(_A)
class _Dot5PhysMgmtPortRingPortMediaSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noSelection',1),('stp',2),('fiber',3)))
_Dot5PhysMgmtPortRingPortMediaSelect_Type.__name__=_C
_Dot5PhysMgmtPortRingPortMediaSelect_Object=MibTableColumn
dot5PhysMgmtPortRingPortMediaSelect=_Dot5PhysMgmtPortRingPortMediaSelect_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,4),_Dot5PhysMgmtPortRingPortMediaSelect_Type())
dot5PhysMgmtPortRingPortMediaSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingPortMediaSelect.setStatus(_A)
class _Dot5PhysMgmtPortRingFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_N,2),(_O,3)))
_Dot5PhysMgmtPortRingFaultStatus_Type.__name__=_C
_Dot5PhysMgmtPortRingFaultStatus_Object=MibTableColumn
dot5PhysMgmtPortRingFaultStatus=_Dot5PhysMgmtPortRingFaultStatus_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,5),_Dot5PhysMgmtPortRingFaultStatus_Type())
dot5PhysMgmtPortRingFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingFaultStatus.setStatus(_A)
_Dot5PhysMgmtPortRingFaultStateTime_Type=TimeTicks
_Dot5PhysMgmtPortRingFaultStateTime_Object=MibTableColumn
dot5PhysMgmtPortRingFaultStateTime=_Dot5PhysMgmtPortRingFaultStateTime_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,6),_Dot5PhysMgmtPortRingFaultStateTime_Type())
dot5PhysMgmtPortRingFaultStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingFaultStateTime.setStatus(_A)
class _Dot5PhysMgmtPortRingPhantomCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noPhantomAvailable',1),('activatePhantom',2),('deactivatePhantom',3)))
_Dot5PhysMgmtPortRingPhantomCurrent_Type.__name__=_C
_Dot5PhysMgmtPortRingPhantomCurrent_Object=MibTableColumn
dot5PhysMgmtPortRingPhantomCurrent=_Dot5PhysMgmtPortRingPhantomCurrent_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,7),_Dot5PhysMgmtPortRingPhantomCurrent_Type())
dot5PhysMgmtPortRingPhantomCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingPhantomCurrent.setStatus(_A)
class _Dot5PhysMgmtPortRingPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_Dot5PhysMgmtPortRingPortType_Type.__name__=_C
_Dot5PhysMgmtPortRingPortType_Object=MibTableColumn
dot5PhysMgmtPortRingPortType=_Dot5PhysMgmtPortRingPortType_Object((1,3,6,1,4,1,52,4,1,1,6,1,3,3,1,1,8),_Dot5PhysMgmtPortRingPortType_Type())
dot5PhysMgmtPortRingPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtPortRingPortType.setStatus(_A)
_Dot5PhysMgmtPortSwitch_ObjectIdentity=ObjectIdentity
dot5PhysMgmtPortSwitch=_Dot5PhysMgmtPortSwitch_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,3,4))
_Dot5PhysMgmtRingSpeedTables_ObjectIdentity=ObjectIdentity
dot5PhysMgmtRingSpeedTables=_Dot5PhysMgmtRingSpeedTables_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,6,1,4))
_Dot5PhysMgmtDeviceRingSpeedTable_Object=MibTable
dot5PhysMgmtDeviceRingSpeedTable=_Dot5PhysMgmtDeviceRingSpeedTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,1))
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingSpeedTable.setStatus(_A)
_Dot5PhysMgmtDeviceRingSpeedEntry_Object=MibTableRow
dot5PhysMgmtDeviceRingSpeedEntry=_Dot5PhysMgmtDeviceRingSpeedEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,1,1))
dot5PhysMgmtDeviceRingSpeedEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingSpeedEntry.setStatus(_A)
class _Dot5PhysMgmtDeviceRingSpeedRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_Dot5PhysMgmtDeviceRingSpeedRing_Type.__name__=_C
_Dot5PhysMgmtDeviceRingSpeedRing_Object=MibTableColumn
dot5PhysMgmtDeviceRingSpeedRing=_Dot5PhysMgmtDeviceRingSpeedRing_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,1,1,1),_Dot5PhysMgmtDeviceRingSpeedRing_Type())
dot5PhysMgmtDeviceRingSpeedRing.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingSpeedRing.setStatus(_A)
class _Dot5PhysMgmtDeviceRingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,10,16,100)));namedValues=NamedValues(*((_I,1),(_J,4),(_K,10),(_L,16),(_M,100)))
_Dot5PhysMgmtDeviceRingSpeed_Type.__name__=_C
_Dot5PhysMgmtDeviceRingSpeed_Object=MibTableColumn
dot5PhysMgmtDeviceRingSpeed=_Dot5PhysMgmtDeviceRingSpeed_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,1,1,2),_Dot5PhysMgmtDeviceRingSpeed_Type())
dot5PhysMgmtDeviceRingSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtDeviceRingSpeed.setStatus(_A)
_Dot5PhysMgmtBoardAuxRingSpeedTable_Object=MibTable
dot5PhysMgmtBoardAuxRingSpeedTable=_Dot5PhysMgmtBoardAuxRingSpeedTable_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,2))
if mibBuilder.loadTexts:dot5PhysMgmtBoardAuxRingSpeedTable.setStatus(_A)
_Dot5PhysMgmtBoardAuxRingSpeedEntry_Object=MibTableRow
dot5PhysMgmtBoardAuxRingSpeedEntry=_Dot5PhysMgmtBoardAuxRingSpeedEntry_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,2,1))
dot5PhysMgmtBoardAuxRingSpeedEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:dot5PhysMgmtBoardAuxRingSpeedEntry.setStatus(_A)
_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Type=Integer32
_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Object=MibTableColumn
dot5PhysMgmtBoardAuxRingSpeedBoardId=_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,2,1,1),_Dot5PhysMgmtBoardAuxRingSpeedBoardId_Type())
dot5PhysMgmtBoardAuxRingSpeedBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardAuxRingSpeedBoardId.setStatus(_A)
class _Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(201,254))
_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type.__name__=_C
_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Object=MibTableColumn
dot5PhysMgmtBoardAuxRingSpeedAuxRing=_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,2,1,2),_Dot5PhysMgmtBoardAuxRingSpeedAuxRing_Type())
dot5PhysMgmtBoardAuxRingSpeedAuxRing.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5PhysMgmtBoardAuxRingSpeedAuxRing.setStatus(_A)
class _Dot5PhysMgmtBoardAuxRingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,10,16,100)));namedValues=NamedValues(*((_I,1),(_J,4),(_K,10),(_L,16),(_M,100)))
_Dot5PhysMgmtBoardAuxRingSpeed_Type.__name__=_C
_Dot5PhysMgmtBoardAuxRingSpeed_Object=MibTableColumn
dot5PhysMgmtBoardAuxRingSpeed=_Dot5PhysMgmtBoardAuxRingSpeed_Object((1,3,6,1,4,1,52,4,1,1,6,1,4,2,1,3),_Dot5PhysMgmtBoardAuxRingSpeed_Type())
dot5PhysMgmtBoardAuxRingSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:dot5PhysMgmtBoardAuxRingSpeed.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dot5PhysMgmtRev1':dot5PhysMgmtRev1,'dot5PhysMgmtDevice':dot5PhysMgmtDevice,'dot5PhysMgmtDeviceRingCount':dot5PhysMgmtDeviceRingCount,'dot5PhysMgmtDevicePortCount':dot5PhysMgmtDevicePortCount,'dot5PhysMgmtDevicePortsEnable':dot5PhysMgmtDevicePortsEnable,'dot5PhysMgmtDevicePortsOn':dot5PhysMgmtDevicePortsOn,'dot5PhysMgmtDevicePortsOper':dot5PhysMgmtDevicePortsOper,'dot5PhysMgmtDeviceStnPortCount':dot5PhysMgmtDeviceStnPortCount,'dot5PhysMgmtDeviceStnPortsEnable':dot5PhysMgmtDeviceStnPortsEnable,'dot5PhysMgmtDeviceStnPortsOn':dot5PhysMgmtDeviceStnPortsOn,'dot5PhysMgmtDeviceRingPortCount':dot5PhysMgmtDeviceRingPortCount,'dot5PhysMgmtDeviceRingPortsEnable':dot5PhysMgmtDeviceRingPortsEnable,'dot5PhysMgmtDeviceRingPortsOn':dot5PhysMgmtDeviceRingPortsOn,'dot5PhysMgmtDevicePortAssociationChanges':dot5PhysMgmtDevicePortAssociationChanges,'dot5PhysMgmtBoard':dot5PhysMgmtBoard,'dot5PhysMgmtBoardTable':dot5PhysMgmtBoardTable,'dot5PhysMgmtBoardEntry':dot5PhysMgmtBoardEntry,_P:dot5PhysMgmtBoardId,'dot5PhysMgmtBoardDomain':dot5PhysMgmtBoardDomain,'dot5PhysMgmtBoardName':dot5PhysMgmtBoardName,'dot5PhysMgmtBoardDesc':dot5PhysMgmtBoardDesc,'dot5PhysMgmtBoardDot5PortCount':dot5PhysMgmtBoardDot5PortCount,'dot5PhysMgmtBoardDot5PortsEnable':dot5PhysMgmtBoardDot5PortsEnable,'dot5PhysMgmtBoardDot5PortsOn':dot5PhysMgmtBoardDot5PortsOn,'dot5PhysMgmtBoardDot5PortsOper':dot5PhysMgmtBoardDot5PortsOper,'dot5PhysMgmtBoardDot5StnPortCount':dot5PhysMgmtBoardDot5StnPortCount,'dot5PhysMgmtBoardDot5StnPortsEnable':dot5PhysMgmtBoardDot5StnPortsEnable,'dot5PhysMgmtBoardDot5StnPortsOn':dot5PhysMgmtBoardDot5StnPortsOn,'dot5PhysMgmtBoardDot5RingPortCount':dot5PhysMgmtBoardDot5RingPortCount,'dot5PhysMgmtBoardDot5RingPortsEnable':dot5PhysMgmtBoardDot5RingPortsEnable,'dot5PhysMgmtBoardDot5RingPortsOn':dot5PhysMgmtBoardDot5RingPortsOn,'dot5PhysMgmtBoardMode':dot5PhysMgmtBoardMode,'dot5PhysMgmtBoardSpeed':dot5PhysMgmtBoardSpeed,'dot5PhysMgmtBoardSpeedFault':dot5PhysMgmtBoardSpeedFault,'dot5PhysMgmtBoardSpeedFaultLocation':dot5PhysMgmtBoardSpeedFaultLocation,'dot5PhysMgmtBoardPortAssociation':dot5PhysMgmtBoardPortAssociation,'dot5PhysMgmtBoardPortAssociationChanges':dot5PhysMgmtBoardPortAssociationChanges,'dot5PhysMgmtPort':dot5PhysMgmtPort,'dot5PhysMgmtPortCommon':dot5PhysMgmtPortCommon,'dot5PhysMgmtPortCommonTable':dot5PhysMgmtPortCommonTable,'dot5PhysMgmtPortCommonEntry':dot5PhysMgmtPortCommonEntry,_U:dot5PhysMgmtPortCommonPortId,_T:dot5PhysMgmtPortCommonBoardId,'dot5PhysMgmtPortCommonPortName':dot5PhysMgmtPortCommonPortName,'dot5PhysMgmtPortCommonPortAdminState':dot5PhysMgmtPortCommonPortAdminState,'dot5PhysMgmtPortCommonPortOperState':dot5PhysMgmtPortCommonPortOperState,'dot5PhysMgmtPortCommonPortType':dot5PhysMgmtPortCommonPortType,'dot5PhysMgmtPortCommonSpeedFaultDetect':dot5PhysMgmtPortCommonSpeedFaultDetect,'dot5PhysMgmtPortCommonRingOutEnable':dot5PhysMgmtPortCommonRingOutEnable,'dot5PhysMgmtPortCommonPortAssociation':dot5PhysMgmtPortCommonPortAssociation,'dot5PhysMgmtPortCommonMauCompId':dot5PhysMgmtPortCommonMauCompId,'dot5PhysMgmtPortStn':dot5PhysMgmtPortStn,'dot5PhysMgmtPortStnTable':dot5PhysMgmtPortStnTable,'dot5PhysMgmtPortStnEntry':dot5PhysMgmtPortStnEntry,_X:dot5PhysMgmtPortStnPortId,_W:dot5PhysMgmtPortStnBoardId,'dot5PhysMgmtPortStnPortLinkState':dot5PhysMgmtPortStnPortLinkState,'dot5PhysMgmtPortStnPortLinkStateTime':dot5PhysMgmtPortStnPortLinkStateTime,'dot5PhysMgmtPortStnInsertionTrapEnable':dot5PhysMgmtPortStnInsertionTrapEnable,'dot5PhysMgmtPortRing':dot5PhysMgmtPortRing,'dot5PhysMgmtPortRingTable':dot5PhysMgmtPortRingTable,'dot5PhysMgmtPortRingEntry':dot5PhysMgmtPortRingEntry,_Z:dot5PhysMgmtPortRingPortId,_Y:dot5PhysMgmtPortRingBoardId,'dot5PhysMgmtPortRingPortClass':dot5PhysMgmtPortRingPortClass,'dot5PhysMgmtPortRingPortMediaSelect':dot5PhysMgmtPortRingPortMediaSelect,'dot5PhysMgmtPortRingFaultStatus':dot5PhysMgmtPortRingFaultStatus,'dot5PhysMgmtPortRingFaultStateTime':dot5PhysMgmtPortRingFaultStateTime,'dot5PhysMgmtPortRingPhantomCurrent':dot5PhysMgmtPortRingPhantomCurrent,'dot5PhysMgmtPortRingPortType':dot5PhysMgmtPortRingPortType,'dot5PhysMgmtPortSwitch':dot5PhysMgmtPortSwitch,'dot5PhysMgmtRingSpeedTables':dot5PhysMgmtRingSpeedTables,'dot5PhysMgmtDeviceRingSpeedTable':dot5PhysMgmtDeviceRingSpeedTable,'dot5PhysMgmtDeviceRingSpeedEntry':dot5PhysMgmtDeviceRingSpeedEntry,_a:dot5PhysMgmtDeviceRingSpeedRing,'dot5PhysMgmtDeviceRingSpeed':dot5PhysMgmtDeviceRingSpeed,'dot5PhysMgmtBoardAuxRingSpeedTable':dot5PhysMgmtBoardAuxRingSpeedTable,'dot5PhysMgmtBoardAuxRingSpeedEntry':dot5PhysMgmtBoardAuxRingSpeedEntry,_b:dot5PhysMgmtBoardAuxRingSpeedBoardId,_c:dot5PhysMgmtBoardAuxRingSpeedAuxRing,'dot5PhysMgmtBoardAuxRingSpeed':dot5PhysMgmtBoardAuxRingSpeed})