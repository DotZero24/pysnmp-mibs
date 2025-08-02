_R='dNatRulesPriority'
_Q='dNatRulesStatusPriority'
_P='delete'
_O='insert'
_N='sNatRulesPriority'
_M='sNatRulesStatusPriority'
_L='MxEnableState'
_K='icmp'
_J='udp'
_I='tcp'
_H='all'
_G='MX-NAT-MIB'
_F='noOp'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_L,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
natMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2275))
_NatMIBObjects_ObjectIdentity=ObjectIdentity
natMIBObjects=_NatMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2275,1))
class _ConfigModifiedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('yes',100),('no',200)))
_ConfigModifiedStatus_Type.__name__=_D
_ConfigModifiedStatus_Object=MibScalar
configModifiedStatus=_ConfigModifiedStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,100),_ConfigModifiedStatus_Type())
configModifiedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:configModifiedStatus.setStatus(_A)
_SNatRulesStatusTable_Object=MibTable
sNatRulesStatusTable=_SNatRulesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200))
if mibBuilder.loadTexts:sNatRulesStatusTable.setStatus(_A)
_SNatRulesStatusEntry_Object=MibTableRow
sNatRulesStatusEntry=_SNatRulesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1))
sNatRulesStatusEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:sNatRulesStatusEntry.setStatus(_A)
_SNatRulesStatusPriority_Type=Unsigned32
_SNatRulesStatusPriority_Object=MibTableColumn
sNatRulesStatusPriority=_SNatRulesStatusPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,100),_SNatRulesStatusPriority_Type())
sNatRulesStatusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusPriority.setStatus(_A)
_SNatRulesStatusSourceAddress_Type=OctetString
_SNatRulesStatusSourceAddress_Object=MibTableColumn
sNatRulesStatusSourceAddress=_SNatRulesStatusSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,200),_SNatRulesStatusSourceAddress_Type())
sNatRulesStatusSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusSourceAddress.setStatus(_A)
_SNatRulesStatusSourcePort_Type=OctetString
_SNatRulesStatusSourcePort_Object=MibTableColumn
sNatRulesStatusSourcePort=_SNatRulesStatusSourcePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,300),_SNatRulesStatusSourcePort_Type())
sNatRulesStatusSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusSourcePort.setStatus(_A)
_SNatRulesStatusDestinationAddress_Type=OctetString
_SNatRulesStatusDestinationAddress_Object=MibTableColumn
sNatRulesStatusDestinationAddress=_SNatRulesStatusDestinationAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,400),_SNatRulesStatusDestinationAddress_Type())
sNatRulesStatusDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusDestinationAddress.setStatus(_A)
_SNatRulesStatusDestinationPort_Type=OctetString
_SNatRulesStatusDestinationPort_Object=MibTableColumn
sNatRulesStatusDestinationPort=_SNatRulesStatusDestinationPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,500),_SNatRulesStatusDestinationPort_Type())
sNatRulesStatusDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusDestinationPort.setStatus(_A)
class _SNatRulesStatusProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_H,100),(_I,200),(_J,300),(_K,400)))
_SNatRulesStatusProtocol_Type.__name__=_D
_SNatRulesStatusProtocol_Object=MibTableColumn
sNatRulesStatusProtocol=_SNatRulesStatusProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,600),_SNatRulesStatusProtocol_Type())
sNatRulesStatusProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusProtocol.setStatus(_A)
_SNatRulesStatusNewAddress_Type=OctetString
_SNatRulesStatusNewAddress_Object=MibTableColumn
sNatRulesStatusNewAddress=_SNatRulesStatusNewAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,200,1,700),_SNatRulesStatusNewAddress_Type())
sNatRulesStatusNewAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesStatusNewAddress.setStatus(_A)
_SNatRulesTable_Object=MibTable
sNatRulesTable=_SNatRulesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700))
if mibBuilder.loadTexts:sNatRulesTable.setStatus(_A)
_SNatRulesEntry_Object=MibTableRow
sNatRulesEntry=_SNatRulesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1))
sNatRulesEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:sNatRulesEntry.setStatus(_A)
_SNatRulesPriority_Type=Unsigned32
_SNatRulesPriority_Object=MibTableColumn
sNatRulesPriority=_SNatRulesPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,100),_SNatRulesPriority_Type())
sNatRulesPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sNatRulesPriority.setStatus(_A)
class _SNatRulesActivation_Type(MxEnableState):defaultValue=0
_SNatRulesActivation_Type.__name__=_L
_SNatRulesActivation_Object=MibTableColumn
sNatRulesActivation=_SNatRulesActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,200),_SNatRulesActivation_Type())
sNatRulesActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesActivation.setStatus(_A)
class _SNatRulesSourceAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_SNatRulesSourceAddress_Type.__name__=_E
_SNatRulesSourceAddress_Object=MibTableColumn
sNatRulesSourceAddress=_SNatRulesSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,300),_SNatRulesSourceAddress_Type())
sNatRulesSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesSourceAddress.setStatus(_A)
class _SNatRulesSourcePort_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_SNatRulesSourcePort_Type.__name__=_E
_SNatRulesSourcePort_Object=MibTableColumn
sNatRulesSourcePort=_SNatRulesSourcePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,400),_SNatRulesSourcePort_Type())
sNatRulesSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesSourcePort.setStatus(_A)
class _SNatRulesDestinationAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_SNatRulesDestinationAddress_Type.__name__=_E
_SNatRulesDestinationAddress_Object=MibTableColumn
sNatRulesDestinationAddress=_SNatRulesDestinationAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,500),_SNatRulesDestinationAddress_Type())
sNatRulesDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesDestinationAddress.setStatus(_A)
class _SNatRulesDestinationPort_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_SNatRulesDestinationPort_Type.__name__=_E
_SNatRulesDestinationPort_Object=MibTableColumn
sNatRulesDestinationPort=_SNatRulesDestinationPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,600),_SNatRulesDestinationPort_Type())
sNatRulesDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesDestinationPort.setStatus(_A)
class _SNatRulesProtocol_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_H,100),(_I,200),(_J,300),(_K,400)))
_SNatRulesProtocol_Type.__name__=_D
_SNatRulesProtocol_Object=MibTableColumn
sNatRulesProtocol=_SNatRulesProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,700),_SNatRulesProtocol_Type())
sNatRulesProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesProtocol.setStatus(_A)
class _SNatRulesNewAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_SNatRulesNewAddress_Type.__name__=_E
_SNatRulesNewAddress_Object=MibTableColumn
sNatRulesNewAddress=_SNatRulesNewAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,800),_SNatRulesNewAddress_Type())
sNatRulesNewAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesNewAddress.setStatus(_A)
class _SNatRulesUp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('up',10)))
_SNatRulesUp_Type.__name__=_D
_SNatRulesUp_Object=MibTableColumn
sNatRulesUp=_SNatRulesUp_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,900),_SNatRulesUp_Type())
sNatRulesUp.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesUp.setStatus(_A)
class _SNatRulesDown_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('down',10)))
_SNatRulesDown_Type.__name__=_D
_SNatRulesDown_Object=MibTableColumn
sNatRulesDown=_SNatRulesDown_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,1000),_SNatRulesDown_Type())
sNatRulesDown.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesDown.setStatus(_A)
class _SNatRulesInsert_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),(_O,10)))
_SNatRulesInsert_Type.__name__=_D
_SNatRulesInsert_Object=MibTableColumn
sNatRulesInsert=_SNatRulesInsert_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,1100),_SNatRulesInsert_Type())
sNatRulesInsert.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesInsert.setStatus(_A)
class _SNatRulesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),(_P,10)))
_SNatRulesDelete_Type.__name__=_D
_SNatRulesDelete_Object=MibTableColumn
sNatRulesDelete=_SNatRulesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,700,1,1200),_SNatRulesDelete_Type())
sNatRulesDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:sNatRulesDelete.setStatus(_A)
_DNatRulesStatusTable_Object=MibTable
dNatRulesStatusTable=_DNatRulesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800))
if mibBuilder.loadTexts:dNatRulesStatusTable.setStatus(_A)
_DNatRulesStatusEntry_Object=MibTableRow
dNatRulesStatusEntry=_DNatRulesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1))
dNatRulesStatusEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:dNatRulesStatusEntry.setStatus(_A)
_DNatRulesStatusPriority_Type=Unsigned32
_DNatRulesStatusPriority_Object=MibTableColumn
dNatRulesStatusPriority=_DNatRulesStatusPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,100),_DNatRulesStatusPriority_Type())
dNatRulesStatusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusPriority.setStatus(_A)
_DNatRulesStatusSourceAddress_Type=OctetString
_DNatRulesStatusSourceAddress_Object=MibTableColumn
dNatRulesStatusSourceAddress=_DNatRulesStatusSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,200),_DNatRulesStatusSourceAddress_Type())
dNatRulesStatusSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusSourceAddress.setStatus(_A)
_DNatRulesStatusSourcePort_Type=OctetString
_DNatRulesStatusSourcePort_Object=MibTableColumn
dNatRulesStatusSourcePort=_DNatRulesStatusSourcePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,300),_DNatRulesStatusSourcePort_Type())
dNatRulesStatusSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusSourcePort.setStatus(_A)
_DNatRulesStatusDestinationAddress_Type=OctetString
_DNatRulesStatusDestinationAddress_Object=MibTableColumn
dNatRulesStatusDestinationAddress=_DNatRulesStatusDestinationAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,400),_DNatRulesStatusDestinationAddress_Type())
dNatRulesStatusDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusDestinationAddress.setStatus(_A)
_DNatRulesStatusDestinationPort_Type=OctetString
_DNatRulesStatusDestinationPort_Object=MibTableColumn
dNatRulesStatusDestinationPort=_DNatRulesStatusDestinationPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,500),_DNatRulesStatusDestinationPort_Type())
dNatRulesStatusDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusDestinationPort.setStatus(_A)
class _DNatRulesStatusProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_H,100),(_I,200),(_J,300),(_K,400)))
_DNatRulesStatusProtocol_Type.__name__=_D
_DNatRulesStatusProtocol_Object=MibTableColumn
dNatRulesStatusProtocol=_DNatRulesStatusProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,600),_DNatRulesStatusProtocol_Type())
dNatRulesStatusProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusProtocol.setStatus(_A)
_DNatRulesStatusNewAddress_Type=OctetString
_DNatRulesStatusNewAddress_Object=MibTableColumn
dNatRulesStatusNewAddress=_DNatRulesStatusNewAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,800,1,700),_DNatRulesStatusNewAddress_Type())
dNatRulesStatusNewAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesStatusNewAddress.setStatus(_A)
_DNatRulesTable_Object=MibTable
dNatRulesTable=_DNatRulesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900))
if mibBuilder.loadTexts:dNatRulesTable.setStatus(_A)
_DNatRulesEntry_Object=MibTableRow
dNatRulesEntry=_DNatRulesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1))
dNatRulesEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:dNatRulesEntry.setStatus(_A)
_DNatRulesPriority_Type=Unsigned32
_DNatRulesPriority_Object=MibTableColumn
dNatRulesPriority=_DNatRulesPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,100),_DNatRulesPriority_Type())
dNatRulesPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dNatRulesPriority.setStatus(_A)
class _DNatRulesActivation_Type(MxEnableState):defaultValue=0
_DNatRulesActivation_Type.__name__=_L
_DNatRulesActivation_Object=MibTableColumn
dNatRulesActivation=_DNatRulesActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,200),_DNatRulesActivation_Type())
dNatRulesActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesActivation.setStatus(_A)
class _DNatRulesSourceAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_DNatRulesSourceAddress_Type.__name__=_E
_DNatRulesSourceAddress_Object=MibTableColumn
dNatRulesSourceAddress=_DNatRulesSourceAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,300),_DNatRulesSourceAddress_Type())
dNatRulesSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesSourceAddress.setStatus(_A)
class _DNatRulesSourcePort_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_DNatRulesSourcePort_Type.__name__=_E
_DNatRulesSourcePort_Object=MibTableColumn
dNatRulesSourcePort=_DNatRulesSourcePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,400),_DNatRulesSourcePort_Type())
dNatRulesSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesSourcePort.setStatus(_A)
class _DNatRulesDestinationAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_DNatRulesDestinationAddress_Type.__name__=_E
_DNatRulesDestinationAddress_Object=MibTableColumn
dNatRulesDestinationAddress=_DNatRulesDestinationAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,500),_DNatRulesDestinationAddress_Type())
dNatRulesDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesDestinationAddress.setStatus(_A)
class _DNatRulesDestinationPort_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_DNatRulesDestinationPort_Type.__name__=_E
_DNatRulesDestinationPort_Object=MibTableColumn
dNatRulesDestinationPort=_DNatRulesDestinationPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,600),_DNatRulesDestinationPort_Type())
dNatRulesDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesDestinationPort.setStatus(_A)
class _DNatRulesProtocol_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_H,100),(_I,200),(_J,300),(_K,400)))
_DNatRulesProtocol_Type.__name__=_D
_DNatRulesProtocol_Object=MibTableColumn
dNatRulesProtocol=_DNatRulesProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,700),_DNatRulesProtocol_Type())
dNatRulesProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesProtocol.setStatus(_A)
class _DNatRulesNewAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_DNatRulesNewAddress_Type.__name__=_E
_DNatRulesNewAddress_Object=MibTableColumn
dNatRulesNewAddress=_DNatRulesNewAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,800),_DNatRulesNewAddress_Type())
dNatRulesNewAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesNewAddress.setStatus(_A)
class _DNatRulesUp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('up',10)))
_DNatRulesUp_Type.__name__=_D
_DNatRulesUp_Object=MibTableColumn
dNatRulesUp=_DNatRulesUp_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,900),_DNatRulesUp_Type())
dNatRulesUp.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesUp.setStatus(_A)
class _DNatRulesDown_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('down',10)))
_DNatRulesDown_Type.__name__=_D
_DNatRulesDown_Object=MibTableColumn
dNatRulesDown=_DNatRulesDown_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,1000),_DNatRulesDown_Type())
dNatRulesDown.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesDown.setStatus(_A)
class _DNatRulesInsert_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),(_O,10)))
_DNatRulesInsert_Type.__name__=_D
_DNatRulesInsert_Object=MibTableColumn
dNatRulesInsert=_DNatRulesInsert_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,1100),_DNatRulesInsert_Type())
dNatRulesInsert.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesInsert.setStatus(_A)
class _DNatRulesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),(_P,10)))
_DNatRulesDelete_Type.__name__=_D
_DNatRulesDelete_Object=MibTableColumn
dNatRulesDelete=_DNatRulesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,900,1,1200),_DNatRulesDelete_Type())
dNatRulesDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:dNatRulesDelete.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2275,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'natMIB':natMIB,'natMIBObjects':natMIBObjects,'configModifiedStatus':configModifiedStatus,'sNatRulesStatusTable':sNatRulesStatusTable,'sNatRulesStatusEntry':sNatRulesStatusEntry,_M:sNatRulesStatusPriority,'sNatRulesStatusSourceAddress':sNatRulesStatusSourceAddress,'sNatRulesStatusSourcePort':sNatRulesStatusSourcePort,'sNatRulesStatusDestinationAddress':sNatRulesStatusDestinationAddress,'sNatRulesStatusDestinationPort':sNatRulesStatusDestinationPort,'sNatRulesStatusProtocol':sNatRulesStatusProtocol,'sNatRulesStatusNewAddress':sNatRulesStatusNewAddress,'sNatRulesTable':sNatRulesTable,'sNatRulesEntry':sNatRulesEntry,_N:sNatRulesPriority,'sNatRulesActivation':sNatRulesActivation,'sNatRulesSourceAddress':sNatRulesSourceAddress,'sNatRulesSourcePort':sNatRulesSourcePort,'sNatRulesDestinationAddress':sNatRulesDestinationAddress,'sNatRulesDestinationPort':sNatRulesDestinationPort,'sNatRulesProtocol':sNatRulesProtocol,'sNatRulesNewAddress':sNatRulesNewAddress,'sNatRulesUp':sNatRulesUp,'sNatRulesDown':sNatRulesDown,'sNatRulesInsert':sNatRulesInsert,'sNatRulesDelete':sNatRulesDelete,'dNatRulesStatusTable':dNatRulesStatusTable,'dNatRulesStatusEntry':dNatRulesStatusEntry,_Q:dNatRulesStatusPriority,'dNatRulesStatusSourceAddress':dNatRulesStatusSourceAddress,'dNatRulesStatusSourcePort':dNatRulesStatusSourcePort,'dNatRulesStatusDestinationAddress':dNatRulesStatusDestinationAddress,'dNatRulesStatusDestinationPort':dNatRulesStatusDestinationPort,'dNatRulesStatusProtocol':dNatRulesStatusProtocol,'dNatRulesStatusNewAddress':dNatRulesStatusNewAddress,'dNatRulesTable':dNatRulesTable,'dNatRulesEntry':dNatRulesEntry,_R:dNatRulesPriority,'dNatRulesActivation':dNatRulesActivation,'dNatRulesSourceAddress':dNatRulesSourceAddress,'dNatRulesSourcePort':dNatRulesSourcePort,'dNatRulesDestinationAddress':dNatRulesDestinationAddress,'dNatRulesDestinationPort':dNatRulesDestinationPort,'dNatRulesProtocol':dNatRulesProtocol,'dNatRulesNewAddress':dNatRulesNewAddress,'dNatRulesUp':dNatRulesUp,'dNatRulesDown':dNatRulesDown,'dNatRulesInsert':dNatRulesInsert,'dNatRulesDelete':dNatRulesDelete,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})