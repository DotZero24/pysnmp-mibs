_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxAnCesMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnCesMib')
zxPwTcStdMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,4))
class PwGroupID(TextualConvention,Unsigned32):status=_A
class PwIDType(TextualConvention,Unsigned32):status=_A
class PwIndexType(TextualConvention,Unsigned32):status=_A
class PwVlanCfg(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4097))
class PwOperStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
class PwAttachmentIdentifierType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PwCwStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('waitingForNextMsg',1),('sentWrongBitErrorCode',2),('rxWithdrawWithWrongBitErrorCode',3),('illegalReceivedBit',4),('cwPresent',5),('cwNotPresent',6),('notYetKnown',7)))
class PwCapabilities(TextualConvention,Bits):status=_A;namedValues=NamedValues(('pwStatusIndication',0))
class PwStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('pwNotForwarding',0),('customerFacingPwRxFault',1),('customerFacingPwTxFault',2),('psnFacingPwRxFault',3),('psnFacingPwTxFault',4)))
class PwFragSize(TextualConvention,Unsigned32):status=_A
class PwFragStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('noFrag',0),('cfgFragGreaterThanPsnMtu',1),('cfgFragButRemoteIncapable',2),('remoteFragCapable',3),('fragEnabled',4)))
mibBuilder.exportSymbols('ZXPW-TC-STD-MIB',**{'PwGroupID':PwGroupID,'PwIDType':PwIDType,'PwIndexType':PwIndexType,'PwVlanCfg':PwVlanCfg,'PwOperStatusTC':PwOperStatusTC,'PwAttachmentIdentifierType':PwAttachmentIdentifierType,'PwCwStatusTC':PwCwStatusTC,'PwCapabilities':PwCapabilities,'PwStatus':PwStatus,'PwFragSize':PwFragSize,'PwFragStatus':PwFragStatus,'zxPwTcStdMIB':zxPwTcStdMIB})