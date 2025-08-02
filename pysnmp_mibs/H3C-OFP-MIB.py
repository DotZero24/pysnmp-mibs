_H='not-accessible'
_G='h3cOfpInstanceControllerID'
_F='h3cOfpInstanceID'
_E='H3C-OFP-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cOfp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,167))
if mibBuilder.loadTexts:h3cOfp.setRevisions(('2017-02-28 17:00',))
_H3cOfpInstanceObjects_ObjectIdentity=ObjectIdentity
h3cOfpInstanceObjects=_H3cOfpInstanceObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,167,1))
_H3cOfpInstanceControllerTable_Object=MibTable
h3cOfpInstanceControllerTable=_H3cOfpInstanceControllerTable_Object((1,3,6,1,4,1,2011,10,2,167,1,1))
if mibBuilder.loadTexts:h3cOfpInstanceControllerTable.setStatus(_A)
_H3cOfpInstanceControllerEntry_Object=MibTableRow
h3cOfpInstanceControllerEntry=_H3cOfpInstanceControllerEntry_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1))
h3cOfpInstanceControllerEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:h3cOfpInstanceControllerEntry.setStatus(_A)
class _H3cOfpInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cOfpInstanceID_Type.__name__=_C
_H3cOfpInstanceID_Object=MibTableColumn
h3cOfpInstanceID=_H3cOfpInstanceID_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,1),_H3cOfpInstanceID_Type())
h3cOfpInstanceID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cOfpInstanceID.setStatus(_A)
class _H3cOfpInstanceControllerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cOfpInstanceControllerID_Type.__name__=_C
_H3cOfpInstanceControllerID_Object=MibTableColumn
h3cOfpInstanceControllerID=_H3cOfpInstanceControllerID_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,2),_H3cOfpInstanceControllerID_Type())
h3cOfpInstanceControllerID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cOfpInstanceControllerID.setStatus(_A)
class _H3cOfpInstanceControllerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('equal',1),('master',2),('slave',3)))
_H3cOfpInstanceControllerRole_Type.__name__=_C
_H3cOfpInstanceControllerRole_Object=MibTableColumn
h3cOfpInstanceControllerRole=_H3cOfpInstanceControllerRole_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,3),_H3cOfpInstanceControllerRole_Type())
h3cOfpInstanceControllerRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceControllerRole.setStatus(_A)
class _H3cOfpInstanceCtrConnectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('ssl',2)))
_H3cOfpInstanceCtrConnectType_Type.__name__=_C
_H3cOfpInstanceCtrConnectType_Object=MibTableColumn
h3cOfpInstanceCtrConnectType=_H3cOfpInstanceCtrConnectType_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,4),_H3cOfpInstanceCtrConnectType_Type())
h3cOfpInstanceCtrConnectType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrConnectType.setStatus(_A)
class _H3cOfpInstanceCtrConnectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('established',1)))
_H3cOfpInstanceCtrConnectState_Type.__name__=_C
_H3cOfpInstanceCtrConnectState_Object=MibTableColumn
h3cOfpInstanceCtrConnectState=_H3cOfpInstanceCtrConnectState_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,5),_H3cOfpInstanceCtrConnectState_Type())
h3cOfpInstanceCtrConnectState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrConnectState.setStatus(_A)
class _H3cOfpInstanceCtrSSLPolicy_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cOfpInstanceCtrSSLPolicy_Type.__name__=_D
_H3cOfpInstanceCtrSSLPolicy_Object=MibTableColumn
h3cOfpInstanceCtrSSLPolicy=_H3cOfpInstanceCtrSSLPolicy_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,6),_H3cOfpInstanceCtrSSLPolicy_Type())
h3cOfpInstanceCtrSSLPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrSSLPolicy.setStatus(_A)
class _H3cOfpInstanceCtrVRFName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cOfpInstanceCtrVRFName_Type.__name__=_D
_H3cOfpInstanceCtrVRFName_Object=MibTableColumn
h3cOfpInstanceCtrVRFName=_H3cOfpInstanceCtrVRFName_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,7),_H3cOfpInstanceCtrVRFName_Type())
h3cOfpInstanceCtrVRFName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrVRFName.setStatus(_A)
_H3cOfpInstanceCtrIPType_Type=InetAddressType
_H3cOfpInstanceCtrIPType_Object=MibTableColumn
h3cOfpInstanceCtrIPType=_H3cOfpInstanceCtrIPType_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,8),_H3cOfpInstanceCtrIPType_Type())
h3cOfpInstanceCtrIPType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrIPType.setStatus(_A)
_H3cOfpInstanceCtrIPaddress_Type=InetAddress
_H3cOfpInstanceCtrIPaddress_Object=MibTableColumn
h3cOfpInstanceCtrIPaddress=_H3cOfpInstanceCtrIPaddress_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,9),_H3cOfpInstanceCtrIPaddress_Type())
h3cOfpInstanceCtrIPaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrIPaddress.setStatus(_A)
class _H3cOfpInstanceCtrPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cOfpInstanceCtrPort_Type.__name__=_C
_H3cOfpInstanceCtrPort_Object=MibTableColumn
h3cOfpInstanceCtrPort=_H3cOfpInstanceCtrPort_Object((1,3,6,1,4,1,2011,10,2,167,1,1,1,10),_H3cOfpInstanceCtrPort_Type())
h3cOfpInstanceCtrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cOfpInstanceCtrPort.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cOfp':h3cOfp,'h3cOfpInstanceObjects':h3cOfpInstanceObjects,'h3cOfpInstanceControllerTable':h3cOfpInstanceControllerTable,'h3cOfpInstanceControllerEntry':h3cOfpInstanceControllerEntry,_F:h3cOfpInstanceID,_G:h3cOfpInstanceControllerID,'h3cOfpInstanceControllerRole':h3cOfpInstanceControllerRole,'h3cOfpInstanceCtrConnectType':h3cOfpInstanceCtrConnectType,'h3cOfpInstanceCtrConnectState':h3cOfpInstanceCtrConnectState,'h3cOfpInstanceCtrSSLPolicy':h3cOfpInstanceCtrSSLPolicy,'h3cOfpInstanceCtrVRFName':h3cOfpInstanceCtrVRFName,'h3cOfpInstanceCtrIPType':h3cOfpInstanceCtrIPType,'h3cOfpInstanceCtrIPaddress':h3cOfpInstanceCtrIPaddress,'h3cOfpInstanceCtrPort':h3cOfpInstanceCtrPort})