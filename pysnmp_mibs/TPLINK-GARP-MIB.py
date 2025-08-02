_H='OctetString'
_G='tpGarpInterface'
_F='TPLINK-GARP-MIB'
_E='Enable'
_D='Disable'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkGarpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,61))
if mibBuilder.loadTexts:tplinkGarpMIB.setRevisions(('2014-11-24 14:42',))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_TplinkGarpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkGarpMIBObjects=_TplinkGarpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,61,1))
_TpGarpConfig_ObjectIdentity=ObjectIdentity
tpGarpConfig=_TpGarpConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,61,1,1))
class _TpGarpDupIpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpGarpDupIpEnable_Type.__name__=_B
_TpGarpDupIpEnable_Object=MibScalar
tpGarpDupIpEnable=_TpGarpDupIpEnable_Object((1,3,6,1,4,1,11863,6,61,1,1,1),_TpGarpDupIpEnable_Type())
tpGarpDupIpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGarpDupIpEnable.setStatus(_A)
class _TpGarpIntfUpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpGarpIntfUpEnable_Type.__name__=_B
_TpGarpIntfUpEnable_Object=MibScalar
tpGarpIntfUpEnable=_TpGarpIntfUpEnable_Object((1,3,6,1,4,1,11863,6,61,1,1,2),_TpGarpIntfUpEnable_Type())
tpGarpIntfUpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGarpIntfUpEnable.setStatus(_A)
class _TpGarpLearningEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TpGarpLearningEnable_Type.__name__=_B
_TpGarpLearningEnable_Object=MibScalar
tpGarpLearningEnable=_TpGarpLearningEnable_Object((1,3,6,1,4,1,11863,6,61,1,1,3),_TpGarpLearningEnable_Type())
tpGarpLearningEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGarpLearningEnable.setStatus(_A)
_TpGarpIntfConfig_ObjectIdentity=ObjectIdentity
tpGarpIntfConfig=_TpGarpIntfConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,61,1,2))
_TpGarpIntfConfigTable_Object=MibTable
tpGarpIntfConfigTable=_TpGarpIntfConfigTable_Object((1,3,6,1,4,1,11863,6,61,1,2,1))
if mibBuilder.loadTexts:tpGarpIntfConfigTable.setStatus(_A)
_TpGarpIntfConfigEntry_Object=MibTableRow
tpGarpIntfConfigEntry=_TpGarpIntfConfigEntry_Object((1,3,6,1,4,1,11863,6,61,1,2,1,1))
tpGarpIntfConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tpGarpIntfConfigEntry.setStatus(_A)
class _TpGarpInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TpGarpInterface_Type.__name__=_H
_TpGarpInterface_Object=MibTableColumn
tpGarpInterface=_TpGarpInterface_Object((1,3,6,1,4,1,11863,6,61,1,2,1,1,1),_TpGarpInterface_Type())
tpGarpInterface.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpGarpInterface.setStatus(_A)
class _TpGarpSendInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpGarpSendInterval_Type.__name__=_B
_TpGarpSendInterval_Object=MibTableColumn
tpGarpSendInterval=_TpGarpSendInterval_Object((1,3,6,1,4,1,11863,6,61,1,2,1,1,2),_TpGarpSendInterval_Type())
tpGarpSendInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tpGarpSendInterval.setStatus(_A)
_TplinkGarpNotifications_ObjectIdentity=ObjectIdentity
tplinkGarpNotifications=_TplinkGarpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,61,2))
tpGarpIpDuplicate=NotificationType((1,3,6,1,4,1,11863,6,61,2,1))
tpGarpIpDuplicate.setObjects((_F,_G))
if mibBuilder.loadTexts:tpGarpIpDuplicate.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'MacAddress':MacAddress,'tplinkGarpMIB':tplinkGarpMIB,'tplinkGarpMIBObjects':tplinkGarpMIBObjects,'tpGarpConfig':tpGarpConfig,'tpGarpDupIpEnable':tpGarpDupIpEnable,'tpGarpIntfUpEnable':tpGarpIntfUpEnable,'tpGarpLearningEnable':tpGarpLearningEnable,'tpGarpIntfConfig':tpGarpIntfConfig,'tpGarpIntfConfigTable':tpGarpIntfConfigTable,'tpGarpIntfConfigEntry':tpGarpIntfConfigEntry,_G:tpGarpInterface,'tpGarpSendInterval':tpGarpSendInterval,'tplinkGarpNotifications':tplinkGarpNotifications,'tpGarpIpDuplicate':tpGarpIpDuplicate})