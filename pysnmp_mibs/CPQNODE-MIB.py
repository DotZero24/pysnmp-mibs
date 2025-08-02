_Y='cpqNodeErrorMessage'
_X='NotificationType'
_W='Integer32'
_V='cpqHeThermalDegradedAction'
_U='deprecated'
_T='DisplayString'
_S='cpqHeTemperatureLocale'
_R='cpqHeTemperatureChassis'
_Q='mandatory'
_P='cpqNodeMac4'
_O='cpqNodeMac3'
_N='cpqNodeMac2'
_M='cpqNodeMac1'
_L='cpqNodeSerial'
_K='cpqNodeUUID'
_J='cpqNodeType'
_I='cpqNodeNode'
_H='cpqNodeCart'
_G='sysName'
_F='SNMPv2-MIB'
_E='cpqHoTrapFlags'
_D='CPQHOST-MIB'
_C='CPQHLTH-MIB'
_B='read-only'
_A='CPQNODE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cpqHeTemperatureChassis,cpqHeTemperatureLocale,cpqHeThermalDegradedAction=mibBuilder.importSymbols(_C,_R,_S,_V)
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_D,'compaq',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_W,'IpAddress','ModuleIdentity','MibIdentifier',_X,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_X,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','TextualConvention')
_CpqNode_ObjectIdentity=ObjectIdentity
cpqNode=_CpqNode_ObjectIdentity((1,3,6,1,4,1,232,20))
_CpqNodeFix_ObjectIdentity=ObjectIdentity
cpqNodeFix=_CpqNodeFix_ObjectIdentity((1,3,6,1,4,1,232,20,2))
_CpqNodeComponent_ObjectIdentity=ObjectIdentity
cpqNodeComponent=_CpqNodeComponent_ObjectIdentity((1,3,6,1,4,1,232,20,2,1))
_CpqNodeCart_Type=Integer32
_CpqNodeCart_Object=MibScalar
cpqNodeCart=_CpqNodeCart_Object((1,3,6,1,4,1,232,20,2,1,1),_CpqNodeCart_Type())
cpqNodeCart.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeCart.setStatus(_Q)
_CpqNodeNode_Type=Integer32
_CpqNodeNode_Object=MibScalar
cpqNodeNode=_CpqNodeNode_Object((1,3,6,1,4,1,232,20,2,1,2),_CpqNodeNode_Type())
cpqNodeNode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeNode.setStatus(_Q)
class _CpqNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('cartridge',0),('node',1),('switch',2),('unknown',3)))
_CpqNodeType_Type.__name__=_W
_CpqNodeType_Object=MibScalar
cpqNodeType=_CpqNodeType_Object((1,3,6,1,4,1,232,20,2,1,3),_CpqNodeType_Type())
cpqNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeType.setStatus(_Q)
class _CpqNodeUUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CpqNodeUUID_Type.__name__=_T
_CpqNodeUUID_Object=MibScalar
cpqNodeUUID=_CpqNodeUUID_Object((1,3,6,1,4,1,232,20,2,1,4),_CpqNodeUUID_Type())
cpqNodeUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeUUID.setStatus(_Q)
class _CpqNodeSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CpqNodeSerial_Type.__name__=_T
_CpqNodeSerial_Object=MibScalar
cpqNodeSerial=_CpqNodeSerial_Object((1,3,6,1,4,1,232,20,2,1,5),_CpqNodeSerial_Type())
cpqNodeSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeSerial.setStatus(_Q)
_CpqNodeMac1_Type=DisplayString
_CpqNodeMac1_Object=MibScalar
cpqNodeMac1=_CpqNodeMac1_Object((1,3,6,1,4,1,232,20,2,1,6),_CpqNodeMac1_Type())
cpqNodeMac1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeMac1.setStatus(_U)
_CpqNodeMac2_Type=DisplayString
_CpqNodeMac2_Object=MibScalar
cpqNodeMac2=_CpqNodeMac2_Object((1,3,6,1,4,1,232,20,2,1,7),_CpqNodeMac2_Type())
cpqNodeMac2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeMac2.setStatus(_U)
_CpqNodeMac3_Type=DisplayString
_CpqNodeMac3_Object=MibScalar
cpqNodeMac3=_CpqNodeMac3_Object((1,3,6,1,4,1,232,20,2,1,8),_CpqNodeMac3_Type())
cpqNodeMac3.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeMac3.setStatus(_U)
_CpqNodeMac4_Type=DisplayString
_CpqNodeMac4_Object=MibScalar
cpqNodeMac4=_CpqNodeMac4_Object((1,3,6,1,4,1,232,20,2,1,9),_CpqNodeMac4_Type())
cpqNodeMac4.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeMac4.setStatus(_U)
class _CpqNodeErrorMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqNodeErrorMessage_Type.__name__=_T
_CpqNodeErrorMessage_Object=MibScalar
cpqNodeErrorMessage=_CpqNodeErrorMessage_Object((1,3,6,1,4,1,232,20,2,1,10),_CpqNodeErrorMessage_Type())
cpqNodeErrorMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqNodeErrorMessage.setStatus(_Q)
cpqNodeTemperatureDegraded=NotificationType((1,3,6,1,4,1,232,0,23001))
cpqNodeTemperatureDegraded.setObjects(*((_F,_G),(_D,_E),(_C,_V),(_C,_R),(_C,_S),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodeTemperatureDegraded.setStatus('')
cpqNodeTemperatureOk=NotificationType((1,3,6,1,4,1,232,0,23002))
cpqNodeTemperatureOk.setObjects(*((_F,_G),(_D,_E),(_C,_R),(_C,_S),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodeTemperatureOk.setStatus('')
cpqNodeTemperatureFailed=NotificationType((1,3,6,1,4,1,232,0,23003))
cpqNodeTemperatureFailed.setObjects(*((_F,_G),(_D,_E),(_C,_V),(_C,_R),(_C,_S),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodeTemperatureFailed.setStatus('')
cpqNodeErrorEvent=NotificationType((1,3,6,1,4,1,232,0,23004))
cpqNodeErrorEvent.setObjects(*((_F,_G),(_D,_E),(_A,_Y),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodeErrorEvent.setStatus('')
cpqNodePowerOn=NotificationType((1,3,6,1,4,1,232,0,23010))
cpqNodePowerOn.setObjects(*((_F,_G),(_D,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodePowerOn.setStatus('')
cpqNodePowerOff=NotificationType((1,3,6,1,4,1,232,0,23011))
cpqNodePowerOff.setObjects(*((_F,_G),(_D,_E),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cpqNodePowerOff.setStatus('')
mibBuilder.exportSymbols(_A,**{'cpqNodeTemperatureDegraded':cpqNodeTemperatureDegraded,'cpqNodeTemperatureOk':cpqNodeTemperatureOk,'cpqNodeTemperatureFailed':cpqNodeTemperatureFailed,'cpqNodeErrorEvent':cpqNodeErrorEvent,'cpqNodePowerOn':cpqNodePowerOn,'cpqNodePowerOff':cpqNodePowerOff,'cpqNode':cpqNode,'cpqNodeFix':cpqNodeFix,'cpqNodeComponent':cpqNodeComponent,_H:cpqNodeCart,_I:cpqNodeNode,_J:cpqNodeType,_K:cpqNodeUUID,_L:cpqNodeSerial,_M:cpqNodeMac1,_N:cpqNodeMac2,_O:cpqNodeMac3,_P:cpqNodeMac4,_Y:cpqNodeErrorMessage})