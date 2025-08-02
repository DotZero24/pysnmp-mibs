_F='notAvailable'
_E='mellanoxIfVPIIndex'
_D='MELLANOX-IF-VPI-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mellanoxIfVPI,=mibBuilder.importSymbols('MELLANOX-SMI-MIB','mellanoxIfVPI')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mellanoxIfVPIMib=ModuleIdentity((1,3,6,1,4,1,33049,3,1))
if mibBuilder.loadTexts:mellanoxIfVPIMib.setRevisions(('2017-07-26 00:00',))
_MellanoxIfVPITable_Object=MibTable
mellanoxIfVPITable=_MellanoxIfVPITable_Object((1,3,6,1,4,1,33049,3,1,1))
if mibBuilder.loadTexts:mellanoxIfVPITable.setStatus(_A)
_MellanoxIfVPIEntry_Object=MibTableRow
mellanoxIfVPIEntry=_MellanoxIfVPIEntry_Object((1,3,6,1,4,1,33049,3,1,1,1))
mellanoxIfVPIEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mellanoxIfVPIEntry.setStatus(_A)
_MellanoxIfVPIIndex_Type=Integer32
_MellanoxIfVPIIndex_Object=MibTableColumn
mellanoxIfVPIIndex=_MellanoxIfVPIIndex_Object((1,3,6,1,4,1,33049,3,1,1,1,1),_MellanoxIfVPIIndex_Type())
mellanoxIfVPIIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIIndex.setStatus(_A)
class _MellanoxIfVPIIbPortPhysicalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,100)));namedValues=NamedValues(*(('noStateChange',0),('sleep',1),('polling',2),('disabled',3),('portConfigurationTraining',4),('linkUp',5),('linkErrorRecovery',6),('phyTest',7),(_F,100)))
_MellanoxIfVPIIbPortPhysicalState_Type.__name__=_C
_MellanoxIfVPIIbPortPhysicalState_Object=MibTableColumn
mellanoxIfVPIIbPortPhysicalState=_MellanoxIfVPIIbPortPhysicalState_Object((1,3,6,1,4,1,33049,3,1,1,1,2),_MellanoxIfVPIIbPortPhysicalState_Type())
mellanoxIfVPIIbPortPhysicalState.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIIbPortPhysicalState.setStatus(_A)
class _MellanoxIfVPIIbPortLogicalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,100)));namedValues=NamedValues(*(('noState',0),('down',1),('initialize',2),('armed',3),('active',4),(_F,100)))
_MellanoxIfVPIIbPortLogicalState_Type.__name__=_C
_MellanoxIfVPIIbPortLogicalState_Object=MibTableColumn
mellanoxIfVPIIbPortLogicalState=_MellanoxIfVPIIbPortLogicalState_Object((1,3,6,1,4,1,33049,3,1,1,1,3),_MellanoxIfVPIIbPortLogicalState_Type())
mellanoxIfVPIIbPortLogicalState.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIIbPortLogicalState.setStatus(_A)
_MellanoxIfVPIIbPortGuid_Type=DisplayString
_MellanoxIfVPIIbPortGuid_Object=MibTableColumn
mellanoxIfVPIIbPortGuid=_MellanoxIfVPIIbPortGuid_Object((1,3,6,1,4,1,33049,3,1,1,1,4),_MellanoxIfVPIIbPortGuid_Type())
mellanoxIfVPIIbPortGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIIbPortGuid.setStatus(_A)
_MellanoxIfVPIPortXmitWait_Type=Counter64
_MellanoxIfVPIPortXmitWait_Object=MibTableColumn
mellanoxIfVPIPortXmitWait=_MellanoxIfVPIPortXmitWait_Object((1,3,6,1,4,1,33049,3,1,1,1,5),_MellanoxIfVPIPortXmitWait_Type())
mellanoxIfVPIPortXmitWait.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIPortXmitWait.setStatus(_A)
_MellanoxIfVPISymbolErrorCounter_Type=Counter64
_MellanoxIfVPISymbolErrorCounter_Object=MibTableColumn
mellanoxIfVPISymbolErrorCounter=_MellanoxIfVPISymbolErrorCounter_Object((1,3,6,1,4,1,33049,3,1,1,1,6),_MellanoxIfVPISymbolErrorCounter_Type())
mellanoxIfVPISymbolErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPISymbolErrorCounter.setStatus(_A)
_MellanoxIfVPIPortAdminSpeed_Type=Gauge32
_MellanoxIfVPIPortAdminSpeed_Object=MibTableColumn
mellanoxIfVPIPortAdminSpeed=_MellanoxIfVPIPortAdminSpeed_Object((1,3,6,1,4,1,33049,3,1,1,1,7),_MellanoxIfVPIPortAdminSpeed_Type())
mellanoxIfVPIPortAdminSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIPortAdminSpeed.setStatus(_A)
_MellanoxIfVPISubnetName_Type=DisplayString
_MellanoxIfVPISubnetName_Object=MibTableColumn
mellanoxIfVPISubnetName=_MellanoxIfVPISubnetName_Object((1,3,6,1,4,1,33049,3,1,1,1,8),_MellanoxIfVPISubnetName_Type())
mellanoxIfVPISubnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPISubnetName.setStatus(_A)
_MellanoxIfVPISubnetPrefix_Type=DisplayString
_MellanoxIfVPISubnetPrefix_Object=MibTableColumn
mellanoxIfVPISubnetPrefix=_MellanoxIfVPISubnetPrefix_Object((1,3,6,1,4,1,33049,3,1,1,1,9),_MellanoxIfVPISubnetPrefix_Type())
mellanoxIfVPISubnetPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPISubnetPrefix.setStatus(_A)
_MellanoxIfVPIIbLocalIdentifier_Type=Integer32
_MellanoxIfVPIIbLocalIdentifier_Object=MibTableColumn
mellanoxIfVPIIbLocalIdentifier=_MellanoxIfVPIIbLocalIdentifier_Object((1,3,6,1,4,1,33049,3,1,1,1,10),_MellanoxIfVPIIbLocalIdentifier_Type())
mellanoxIfVPIIbLocalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIIbLocalIdentifier.setStatus(_A)
_MellanoxIfVPI64bytePkts_Type=Counter64
_MellanoxIfVPI64bytePkts_Object=MibTableColumn
mellanoxIfVPI64bytePkts=_MellanoxIfVPI64bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,11),_MellanoxIfVPI64bytePkts_Type())
mellanoxIfVPI64bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI64bytePkts.setStatus(_A)
_MellanoxIfVPI65to127bytePkts_Type=Counter64
_MellanoxIfVPI65to127bytePkts_Object=MibTableColumn
mellanoxIfVPI65to127bytePkts=_MellanoxIfVPI65to127bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,12),_MellanoxIfVPI65to127bytePkts_Type())
mellanoxIfVPI65to127bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI65to127bytePkts.setStatus(_A)
_MellanoxIfVPI128to255bytePkts_Type=Counter64
_MellanoxIfVPI128to255bytePkts_Object=MibTableColumn
mellanoxIfVPI128to255bytePkts=_MellanoxIfVPI128to255bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,13),_MellanoxIfVPI128to255bytePkts_Type())
mellanoxIfVPI128to255bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI128to255bytePkts.setStatus(_A)
_MellanoxIfVPI256to511bytePkts_Type=Counter64
_MellanoxIfVPI256to511bytePkts_Object=MibTableColumn
mellanoxIfVPI256to511bytePkts=_MellanoxIfVPI256to511bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,14),_MellanoxIfVPI256to511bytePkts_Type())
mellanoxIfVPI256to511bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI256to511bytePkts.setStatus(_A)
_MellanoxIfVPI512to1023bytePkts_Type=Counter64
_MellanoxIfVPI512to1023bytePkts_Object=MibTableColumn
mellanoxIfVPI512to1023bytePkts=_MellanoxIfVPI512to1023bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,15),_MellanoxIfVPI512to1023bytePkts_Type())
mellanoxIfVPI512to1023bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI512to1023bytePkts.setStatus(_A)
_MellanoxIfVPI1024to1518bytePkts_Type=Counter64
_MellanoxIfVPI1024to1518bytePkts_Object=MibTableColumn
mellanoxIfVPI1024to1518bytePkts=_MellanoxIfVPI1024to1518bytePkts_Object((1,3,6,1,4,1,33049,3,1,1,1,16),_MellanoxIfVPI1024to1518bytePkts_Type())
mellanoxIfVPI1024to1518bytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPI1024to1518bytePkts.setStatus(_A)
_MellanoxIfVPIJumboPkts_Type=Counter64
_MellanoxIfVPIJumboPkts_Object=MibTableColumn
mellanoxIfVPIJumboPkts=_MellanoxIfVPIJumboPkts_Object((1,3,6,1,4,1,33049,3,1,1,1,17),_MellanoxIfVPIJumboPkts_Type())
mellanoxIfVPIJumboPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIJumboPkts.setStatus(_A)
_MellanoxIfVPIUndersizedPkts_Type=Counter64
_MellanoxIfVPIUndersizedPkts_Object=MibTableColumn
mellanoxIfVPIUndersizedPkts=_MellanoxIfVPIUndersizedPkts_Object((1,3,6,1,4,1,33049,3,1,1,1,18),_MellanoxIfVPIUndersizedPkts_Type())
mellanoxIfVPIUndersizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIUndersizedPkts.setStatus(_A)
_MellanoxIfVPIOversizedPkts_Type=Counter64
_MellanoxIfVPIOversizedPkts_Object=MibTableColumn
mellanoxIfVPIOversizedPkts=_MellanoxIfVPIOversizedPkts_Object((1,3,6,1,4,1,33049,3,1,1,1,19),_MellanoxIfVPIOversizedPkts_Type())
mellanoxIfVPIOversizedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIOversizedPkts.setStatus(_A)
_MellanoxIfVPIUnknownControlOpcode_Type=Counter64
_MellanoxIfVPIUnknownControlOpcode_Object=MibTableColumn
mellanoxIfVPIUnknownControlOpcode=_MellanoxIfVPIUnknownControlOpcode_Object((1,3,6,1,4,1,33049,3,1,1,1,20),_MellanoxIfVPIUnknownControlOpcode_Type())
mellanoxIfVPIUnknownControlOpcode.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIUnknownControlOpcode.setStatus(_A)
_MellanoxIfVPIFCSErrors_Type=Counter64
_MellanoxIfVPIFCSErrors_Object=MibTableColumn
mellanoxIfVPIFCSErrors=_MellanoxIfVPIFCSErrors_Object((1,3,6,1,4,1,33049,3,1,1,1,21),_MellanoxIfVPIFCSErrors_Type())
mellanoxIfVPIFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:mellanoxIfVPIFCSErrors.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mellanoxIfVPIMib':mellanoxIfVPIMib,'mellanoxIfVPITable':mellanoxIfVPITable,'mellanoxIfVPIEntry':mellanoxIfVPIEntry,_E:mellanoxIfVPIIndex,'mellanoxIfVPIIbPortPhysicalState':mellanoxIfVPIIbPortPhysicalState,'mellanoxIfVPIIbPortLogicalState':mellanoxIfVPIIbPortLogicalState,'mellanoxIfVPIIbPortGuid':mellanoxIfVPIIbPortGuid,'mellanoxIfVPIPortXmitWait':mellanoxIfVPIPortXmitWait,'mellanoxIfVPISymbolErrorCounter':mellanoxIfVPISymbolErrorCounter,'mellanoxIfVPIPortAdminSpeed':mellanoxIfVPIPortAdminSpeed,'mellanoxIfVPISubnetName':mellanoxIfVPISubnetName,'mellanoxIfVPISubnetPrefix':mellanoxIfVPISubnetPrefix,'mellanoxIfVPIIbLocalIdentifier':mellanoxIfVPIIbLocalIdentifier,'mellanoxIfVPI64bytePkts':mellanoxIfVPI64bytePkts,'mellanoxIfVPI65to127bytePkts':mellanoxIfVPI65to127bytePkts,'mellanoxIfVPI128to255bytePkts':mellanoxIfVPI128to255bytePkts,'mellanoxIfVPI256to511bytePkts':mellanoxIfVPI256to511bytePkts,'mellanoxIfVPI512to1023bytePkts':mellanoxIfVPI512to1023bytePkts,'mellanoxIfVPI1024to1518bytePkts':mellanoxIfVPI1024to1518bytePkts,'mellanoxIfVPIJumboPkts':mellanoxIfVPIJumboPkts,'mellanoxIfVPIUndersizedPkts':mellanoxIfVPIUndersizedPkts,'mellanoxIfVPIOversizedPkts':mellanoxIfVPIOversizedPkts,'mellanoxIfVPIUnknownControlOpcode':mellanoxIfVPIUnknownControlOpcode,'mellanoxIfVPIFCSErrors':mellanoxIfVPIFCSErrors})