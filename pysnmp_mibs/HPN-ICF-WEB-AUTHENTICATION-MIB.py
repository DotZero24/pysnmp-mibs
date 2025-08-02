_J='hpnicfWaActionCode'
_I='hpnicfWaReasonCode'
_H='Integer32'
_G='hpnicfWaVlanID'
_F='hpnicfWaClientMacAddr'
_E='accessible-for-notify'
_D='ifDescr'
_C='IF-MIB'
_B='current'
_A='HPN-ICF-WEB-AUTHENTICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfWebAuthentication=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,93))
if mibBuilder.loadTexts:hpnicfWebAuthentication.setRevisions(('2008-06-25 00:00',))
_HpnicfWaTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfWaTrapObjects=_HpnicfWaTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,93,1))
_HpnicfWaVlanID_Type=Integer32
_HpnicfWaVlanID_Object=MibScalar
hpnicfWaVlanID=_HpnicfWaVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,93,1,1),_HpnicfWaVlanID_Type())
hpnicfWaVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWaVlanID.setStatus(_B)
class _HpnicfWaReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('globalNumberMax',1),('configNumberMax',2),('portNumberMax',3),('invalidUsername',4),('authFail',5),('setACLFail',6),('changeVlanFail',7),('other',8),('onlineOverTime',9),('noTransferData',10),('cutOperation',11),('portDisabled',12),('portDown',13),('userLogout',14),('vlanChanged',15),('vlanDelted',16)))
_HpnicfWaReasonCode_Type.__name__=_H
_HpnicfWaReasonCode_Object=MibScalar
hpnicfWaReasonCode=_HpnicfWaReasonCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,93,1,2),_HpnicfWaReasonCode_Type())
hpnicfWaReasonCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWaReasonCode.setStatus(_B)
class _HpnicfWaActionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfWaActionCode_Type.__name__=_H
_HpnicfWaActionCode_Object=MibScalar
hpnicfWaActionCode=_HpnicfWaActionCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,93,1,3),_HpnicfWaActionCode_Type())
hpnicfWaActionCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWaActionCode.setStatus(_B)
_HpnicfWaClientMacAddr_Type=MacAddress
_HpnicfWaClientMacAddr_Object=MibScalar
hpnicfWaClientMacAddr=_HpnicfWaClientMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,93,1,4),_HpnicfWaClientMacAddr_Type())
hpnicfWaClientMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWaClientMacAddr.setStatus(_B)
_HpnicfWaTrap_ObjectIdentity=ObjectIdentity
hpnicfWaTrap=_HpnicfWaTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,93,2))
_HpnicfWaTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfWaTrapPrefix=_HpnicfWaTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,93,2,0))
hpnicfWaClientLogon=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,93,2,0,1))
hpnicfWaClientLogon.setObjects(*((_A,_F),(_C,_D),(_A,_G)))
if mibBuilder.loadTexts:hpnicfWaClientLogon.setStatus(_B)
hpnicfWaClientLogonFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,93,2,0,2))
hpnicfWaClientLogonFail.setObjects(*((_A,_F),(_C,_D),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:hpnicfWaClientLogonFail.setStatus(_B)
hpnicfWaClientLogout=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,93,2,0,3))
hpnicfWaClientLogout.setObjects(*((_A,_F),(_C,_D),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:hpnicfWaClientLogout.setStatus(_B)
hpnicfWaSysAction=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,93,2,0,4))
hpnicfWaSysAction.setObjects((_A,_J))
if mibBuilder.loadTexts:hpnicfWaSysAction.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpnicfWebAuthentication':hpnicfWebAuthentication,'hpnicfWaTrapObjects':hpnicfWaTrapObjects,_G:hpnicfWaVlanID,_I:hpnicfWaReasonCode,_J:hpnicfWaActionCode,_F:hpnicfWaClientMacAddr,'hpnicfWaTrap':hpnicfWaTrap,'hpnicfWaTrapPrefix':hpnicfWaTrapPrefix,'hpnicfWaClientLogon':hpnicfWaClientLogon,'hpnicfWaClientLogonFail':hpnicfWaClientLogonFail,'hpnicfWaClientLogout':hpnicfWaClientLogout,'hpnicfWaSysAction':hpnicfWaSysAction})