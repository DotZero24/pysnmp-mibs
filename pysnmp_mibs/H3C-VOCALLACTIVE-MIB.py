_F='unknown'
_E='h3cVoCallActiveChannel'
_D='H3C-VOCALLACTIVE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CodecType,=mibBuilder.importSymbols('H3C-VO-TYPE-MIB','CodecType')
h3cVoice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cVoice')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cVoiceCallActive=ModuleIdentity((1,3,6,1,4,1,2011,10,2,39,6))
if mibBuilder.loadTexts:h3cVoiceCallActive.setRevisions(('2005-03-15 00:00',))
_H3cVoCallActiveObjects_ObjectIdentity=ObjectIdentity
h3cVoCallActiveObjects=_H3cVoCallActiveObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,6,1))
_H3cVoCallActiveTable_Object=MibTable
h3cVoCallActiveTable=_H3cVoCallActiveTable_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1))
if mibBuilder.loadTexts:h3cVoCallActiveTable.setStatus(_A)
_H3cVoCallActiveEntry_Object=MibTableRow
h3cVoCallActiveEntry=_H3cVoCallActiveEntry_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1))
h3cVoCallActiveEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cVoCallActiveEntry.setStatus(_A)
_H3cVoCallActiveChannel_Type=Integer32
_H3cVoCallActiveChannel_Object=MibTableColumn
h3cVoCallActiveChannel=_H3cVoCallActiveChannel_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,1),_H3cVoCallActiveChannel_Type())
h3cVoCallActiveChannel.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cVoCallActiveChannel.setStatus(_A)
_H3cVoCallActiveCallerNumber_Type=OctetString
_H3cVoCallActiveCallerNumber_Object=MibTableColumn
h3cVoCallActiveCallerNumber=_H3cVoCallActiveCallerNumber_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,2),_H3cVoCallActiveCallerNumber_Type())
h3cVoCallActiveCallerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveCallerNumber.setStatus(_A)
_H3cVoCallActiveCalledNumber_Type=OctetString
_H3cVoCallActiveCalledNumber_Object=MibTableColumn
h3cVoCallActiveCalledNumber=_H3cVoCallActiveCalledNumber_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,3),_H3cVoCallActiveCalledNumber_Type())
h3cVoCallActiveCalledNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveCalledNumber.setStatus(_A)
_H3cVoCallActiveEncodeType_Type=CodecType
_H3cVoCallActiveEncodeType_Object=MibTableColumn
h3cVoCallActiveEncodeType=_H3cVoCallActiveEncodeType_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,4),_H3cVoCallActiveEncodeType_Type())
h3cVoCallActiveEncodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveEncodeType.setStatus(_A)
_H3cVoCallActiveLocalAddressType_Type=InetAddressType
_H3cVoCallActiveLocalAddressType_Object=MibTableColumn
h3cVoCallActiveLocalAddressType=_H3cVoCallActiveLocalAddressType_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,5),_H3cVoCallActiveLocalAddressType_Type())
h3cVoCallActiveLocalAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveLocalAddressType.setStatus(_A)
_H3cVoCallActiveLocalAddress_Type=InetAddress
_H3cVoCallActiveLocalAddress_Object=MibTableColumn
h3cVoCallActiveLocalAddress=_H3cVoCallActiveLocalAddress_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,6),_H3cVoCallActiveLocalAddress_Type())
h3cVoCallActiveLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveLocalAddress.setStatus(_A)
_H3cVoCallActivePeerAddressType_Type=InetAddressType
_H3cVoCallActivePeerAddressType_Object=MibTableColumn
h3cVoCallActivePeerAddressType=_H3cVoCallActivePeerAddressType_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,7),_H3cVoCallActivePeerAddressType_Type())
h3cVoCallActivePeerAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActivePeerAddressType.setStatus(_A)
_H3cVoCallActivePeerAddress_Type=InetAddress
_H3cVoCallActivePeerAddress_Object=MibTableColumn
h3cVoCallActivePeerAddress=_H3cVoCallActivePeerAddress_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,8),_H3cVoCallActivePeerAddress_Type())
h3cVoCallActivePeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActivePeerAddress.setStatus(_A)
class _H3cVoCallActiveCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('caller',1),('called',2)))
_H3cVoCallActiveCallOrigin_Type.__name__=_C
_H3cVoCallActiveCallOrigin_Object=MibTableColumn
h3cVoCallActiveCallOrigin=_H3cVoCallActiveCallOrigin_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,9),_H3cVoCallActiveCallOrigin_Type())
h3cVoCallActiveCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveCallOrigin.setStatus(_A)
class _H3cVoCallActiveIPSigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('h323',2),('sip',3)))
_H3cVoCallActiveIPSigType_Type.__name__=_C
_H3cVoCallActiveIPSigType_Object=MibTableColumn
h3cVoCallActiveIPSigType=_H3cVoCallActiveIPSigType_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,10),_H3cVoCallActiveIPSigType_Type())
h3cVoCallActiveIPSigType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveIPSigType.setStatus(_A)
class _H3cVoCallActivePSTNSigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('fxs',2),('fxo',3),('em',4),('r2',5),('dss1',6),('dem',7)))
_H3cVoCallActivePSTNSigType_Type.__name__=_C
_H3cVoCallActivePSTNSigType_Object=MibTableColumn
h3cVoCallActivePSTNSigType=_H3cVoCallActivePSTNSigType_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,11),_H3cVoCallActivePSTNSigType_Type())
h3cVoCallActivePSTNSigType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActivePSTNSigType.setStatus(_A)
class _H3cVoCallActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('calling',2),('alerting',3),('talking',4),('release',5)))
_H3cVoCallActiveStatus_Type.__name__=_C
_H3cVoCallActiveStatus_Object=MibTableColumn
h3cVoCallActiveStatus=_H3cVoCallActiveStatus_Object((1,3,6,1,4,1,2011,10,2,39,6,1,1,1,12),_H3cVoCallActiveStatus_Type())
h3cVoCallActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVoCallActiveStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cVoiceCallActive':h3cVoiceCallActive,'h3cVoCallActiveObjects':h3cVoCallActiveObjects,'h3cVoCallActiveTable':h3cVoCallActiveTable,'h3cVoCallActiveEntry':h3cVoCallActiveEntry,_E:h3cVoCallActiveChannel,'h3cVoCallActiveCallerNumber':h3cVoCallActiveCallerNumber,'h3cVoCallActiveCalledNumber':h3cVoCallActiveCalledNumber,'h3cVoCallActiveEncodeType':h3cVoCallActiveEncodeType,'h3cVoCallActiveLocalAddressType':h3cVoCallActiveLocalAddressType,'h3cVoCallActiveLocalAddress':h3cVoCallActiveLocalAddress,'h3cVoCallActivePeerAddressType':h3cVoCallActivePeerAddressType,'h3cVoCallActivePeerAddress':h3cVoCallActivePeerAddress,'h3cVoCallActiveCallOrigin':h3cVoCallActiveCallOrigin,'h3cVoCallActiveIPSigType':h3cVoCallActiveIPSigType,'h3cVoCallActivePSTNSigType':h3cVoCallActivePSTNSigType,'h3cVoCallActiveStatus':h3cVoCallActiveStatus})