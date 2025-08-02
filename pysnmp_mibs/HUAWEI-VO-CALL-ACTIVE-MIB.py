_G='unknown'
_F='hwVoCallActiveChannel'
_E='HUAWEI-VO-CALL-ACTIVE-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceCallActiveMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,6))
if mibBuilder.loadTexts:hwVoiceCallActiveMIB.setRevisions(('2004-04-08 13:45',))
_HwVoCallActiveObjects_ObjectIdentity=ObjectIdentity
hwVoCallActiveObjects=_HwVoCallActiveObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,6,1))
_HwVoCallActiveTable_Object=MibTable
hwVoCallActiveTable=_HwVoCallActiveTable_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1))
if mibBuilder.loadTexts:hwVoCallActiveTable.setStatus(_A)
_HwVoCallActiveEntry_Object=MibTableRow
hwVoCallActiveEntry=_HwVoCallActiveEntry_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1))
hwVoCallActiveEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hwVoCallActiveEntry.setStatus(_A)
_HwVoCallActiveChannel_Type=Integer32
_HwVoCallActiveChannel_Object=MibTableColumn
hwVoCallActiveChannel=_HwVoCallActiveChannel_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,1),_HwVoCallActiveChannel_Type())
hwVoCallActiveChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveChannel.setStatus(_A)
class _HwVoCallActiveCallerNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoCallActiveCallerNumber_Type.__name__=_D
_HwVoCallActiveCallerNumber_Object=MibTableColumn
hwVoCallActiveCallerNumber=_HwVoCallActiveCallerNumber_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,2),_HwVoCallActiveCallerNumber_Type())
hwVoCallActiveCallerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveCallerNumber.setStatus(_A)
class _HwVoCallActiveCalledNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwVoCallActiveCalledNumber_Type.__name__=_D
_HwVoCallActiveCalledNumber_Object=MibTableColumn
hwVoCallActiveCalledNumber=_HwVoCallActiveCalledNumber_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,3),_HwVoCallActiveCalledNumber_Type())
hwVoCallActiveCalledNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveCalledNumber.setStatus(_A)
class _HwVoCallActiveEncodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_G,0),('g711a',1),('g711u',2),('g723',3),('g729',4),('g729a',5)))
_HwVoCallActiveEncodeType_Type.__name__=_C
_HwVoCallActiveEncodeType_Object=MibTableColumn
hwVoCallActiveEncodeType=_HwVoCallActiveEncodeType_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,4),_HwVoCallActiveEncodeType_Type())
hwVoCallActiveEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveEncodeType.setStatus(_A)
_HwVoCallActiveLocalAddress_Type=IpAddress
_HwVoCallActiveLocalAddress_Object=MibTableColumn
hwVoCallActiveLocalAddress=_HwVoCallActiveLocalAddress_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,5),_HwVoCallActiveLocalAddress_Type())
hwVoCallActiveLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveLocalAddress.setStatus(_A)
_HwVoCallActivePeerAddress_Type=IpAddress
_HwVoCallActivePeerAddress_Object=MibTableColumn
hwVoCallActivePeerAddress=_HwVoCallActivePeerAddress_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,6),_HwVoCallActivePeerAddress_Type())
hwVoCallActivePeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActivePeerAddress.setStatus(_A)
class _HwVoCallActiveCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('caller',1),('called',2)))
_HwVoCallActiveCallOrigin_Type.__name__=_C
_HwVoCallActiveCallOrigin_Object=MibTableColumn
hwVoCallActiveCallOrigin=_HwVoCallActiveCallOrigin_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,7),_HwVoCallActiveCallOrigin_Type())
hwVoCallActiveCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveCallOrigin.setStatus(_A)
class _HwVoCallActiveIPSigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('h323',1))
_HwVoCallActiveIPSigType_Type.__name__=_C
_HwVoCallActiveIPSigType_Object=MibTableColumn
hwVoCallActiveIPSigType=_HwVoCallActiveIPSigType_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,8),_HwVoCallActiveIPSigType_Type())
hwVoCallActiveIPSigType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveIPSigType.setStatus(_A)
class _HwVoCallActivePSTNSigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),('fxs',1),('fxo',2),('em',3),('r2',4),('dss1',5),('dem',6)))
_HwVoCallActivePSTNSigType_Type.__name__=_C
_HwVoCallActivePSTNSigType_Object=MibTableColumn
hwVoCallActivePSTNSigType=_HwVoCallActivePSTNSigType_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,9),_HwVoCallActivePSTNSigType_Type())
hwVoCallActivePSTNSigType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActivePSTNSigType.setStatus(_A)
class _HwVoCallActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('calling',2),('alerting',3),('talking',4),('release',5)))
_HwVoCallActiveStatus_Type.__name__=_C
_HwVoCallActiveStatus_Object=MibTableColumn
hwVoCallActiveStatus=_HwVoCallActiveStatus_Object((1,3,6,1,4,1,2011,5,25,1,6,1,1,1,10),_HwVoCallActiveStatus_Type())
hwVoCallActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoCallActiveStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwVoiceCallActiveMIB':hwVoiceCallActiveMIB,'hwVoCallActiveObjects':hwVoCallActiveObjects,'hwVoCallActiveTable':hwVoCallActiveTable,'hwVoCallActiveEntry':hwVoCallActiveEntry,_F:hwVoCallActiveChannel,'hwVoCallActiveCallerNumber':hwVoCallActiveCallerNumber,'hwVoCallActiveCalledNumber':hwVoCallActiveCalledNumber,'hwVoCallActiveEncodeType':hwVoCallActiveEncodeType,'hwVoCallActiveLocalAddress':hwVoCallActiveLocalAddress,'hwVoCallActivePeerAddress':hwVoCallActivePeerAddress,'hwVoCallActiveCallOrigin':hwVoCallActiveCallOrigin,'hwVoCallActiveIPSigType':hwVoCallActiveIPSigType,'hwVoCallActivePSTNSigType':hwVoCallActivePSTNSigType,'hwVoCallActiveStatus':hwVoCallActiveStatus})