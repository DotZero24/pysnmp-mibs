_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pwTcStdMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,11))
if mibBuilder.loadTexts:pwTcStdMIBR.setRevisions(('2007-02-04 12:00',))
class PwGroupID(TextualConvention,Unsigned32):status=_A
class PwIDType(TextualConvention,Unsigned32):status=_A
class PwIndexType(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class PwIndexOrZeroType(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class PwVlanCfg(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4097))
class PwOperStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('dormant',4),('notPresent',5),('lowerLayerDown',6)))
class PwAttachmentIdentifierType(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PwCwStatusTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('waitingForNextMsg',1),('sentWrongBitErrorCode',2),('rxWithdrawWithWrongBitErrorCode',3),('illegalReceivedBit',4),('cwPresent',5),('cwNotPresent',6),('notYetKnown',7)))
class PwStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('pwNotForwarding',0),('servicePwRxFault',1),('servicePwTxFault',2),('psnPwRxFault',3),('psnPwTxFault',4)))
class PwFragSize(TextualConvention,Unsigned32):status=_A
class PwFragStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('noFrag',0),('cfgFragGreaterThanPsnMtu',1),('cfgFragButRemoteIncapable',2),('remoteFragCapable',3),('fragEnabled',4)))
class PwCfgIndexOrzero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
mibBuilder.exportSymbols('PW-TC-STD-R-MIB',**{'PwGroupID':PwGroupID,'PwIDType':PwIDType,'PwIndexType':PwIndexType,'PwIndexOrZeroType':PwIndexOrZeroType,'PwVlanCfg':PwVlanCfg,'PwOperStatusTC':PwOperStatusTC,'PwAttachmentIdentifierType':PwAttachmentIdentifierType,'PwCwStatusTC':PwCwStatusTC,'PwStatus':PwStatus,'PwFragSize':PwFragSize,'PwFragStatus':PwFragStatus,'PwCfgIndexOrzero':PwCfgIndexOrzero,'radExperimental':radExperimental,'pwTcStdMIBR':pwTcStdMIBR})