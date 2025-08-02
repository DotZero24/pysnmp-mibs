_J='h3cWaActionCode'
_I='h3cWaReasonCode'
_H='Integer32'
_G='h3cWaVlanID'
_F='h3cWaClientMacAddr'
_E='accessible-for-notify'
_D='ifDescr'
_C='IF-MIB'
_B='current'
_A='H3C-WEB-AUTHENTICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
h3cWebAuthentication=ModuleIdentity((1,3,6,1,4,1,2011,10,2,93))
if mibBuilder.loadTexts:h3cWebAuthentication.setRevisions(('2008-06-25 00:00',))
_H3cWaTrapObjects_ObjectIdentity=ObjectIdentity
h3cWaTrapObjects=_H3cWaTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,93,1))
_H3cWaVlanID_Type=Integer32
_H3cWaVlanID_Object=MibScalar
h3cWaVlanID=_H3cWaVlanID_Object((1,3,6,1,4,1,2011,10,2,93,1,1),_H3cWaVlanID_Type())
h3cWaVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cWaVlanID.setStatus(_B)
class _H3cWaReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('globalNumberMax',1),('configNumberMax',2),('portNumberMax',3),('invalidUsername',4),('authFail',5),('setACLFail',6),('changeVlanFail',7),('other',8),('onlineOverTime',9),('noTransferData',10),('cutOperation',11),('portDisabled',12),('portDown',13),('userLogout',14),('vlanChanged',15),('vlanDelted',16)))
_H3cWaReasonCode_Type.__name__=_H
_H3cWaReasonCode_Object=MibScalar
h3cWaReasonCode=_H3cWaReasonCode_Object((1,3,6,1,4,1,2011,10,2,93,1,2),_H3cWaReasonCode_Type())
h3cWaReasonCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cWaReasonCode.setStatus(_B)
class _H3cWaActionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cWaActionCode_Type.__name__=_H
_H3cWaActionCode_Object=MibScalar
h3cWaActionCode=_H3cWaActionCode_Object((1,3,6,1,4,1,2011,10,2,93,1,3),_H3cWaActionCode_Type())
h3cWaActionCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cWaActionCode.setStatus(_B)
_H3cWaClientMacAddr_Type=MacAddress
_H3cWaClientMacAddr_Object=MibScalar
h3cWaClientMacAddr=_H3cWaClientMacAddr_Object((1,3,6,1,4,1,2011,10,2,93,1,4),_H3cWaClientMacAddr_Type())
h3cWaClientMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cWaClientMacAddr.setStatus(_B)
_H3cWaTrap_ObjectIdentity=ObjectIdentity
h3cWaTrap=_H3cWaTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,93,2))
_H3cWaTrapPrefix_ObjectIdentity=ObjectIdentity
h3cWaTrapPrefix=_H3cWaTrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,93,2,0))
h3cWaClientLogon=NotificationType((1,3,6,1,4,1,2011,10,2,93,2,0,1))
h3cWaClientLogon.setObjects(*((_A,_F),(_C,_D),(_A,_G)))
if mibBuilder.loadTexts:h3cWaClientLogon.setStatus(_B)
h3cWaClientLogonFail=NotificationType((1,3,6,1,4,1,2011,10,2,93,2,0,2))
h3cWaClientLogonFail.setObjects(*((_A,_F),(_C,_D),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:h3cWaClientLogonFail.setStatus(_B)
h3cWaClientLogout=NotificationType((1,3,6,1,4,1,2011,10,2,93,2,0,3))
h3cWaClientLogout.setObjects(*((_A,_F),(_C,_D),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:h3cWaClientLogout.setStatus(_B)
h3cWaSysAction=NotificationType((1,3,6,1,4,1,2011,10,2,93,2,0,4))
h3cWaSysAction.setObjects((_A,_J))
if mibBuilder.loadTexts:h3cWaSysAction.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cWebAuthentication':h3cWebAuthentication,'h3cWaTrapObjects':h3cWaTrapObjects,_G:h3cWaVlanID,_I:h3cWaReasonCode,_J:h3cWaActionCode,_F:h3cWaClientMacAddr,'h3cWaTrap':h3cWaTrap,'h3cWaTrapPrefix':h3cWaTrapPrefix,'h3cWaClientLogon':h3cWaClientLogon,'h3cWaClientLogonFail':h3cWaClientLogonFail,'h3cWaClientLogout':h3cWaClientLogout,'h3cWaSysAction':h3cWaSysAction})