_I='h3cARPRatelimitTrapMsg'
_H='h3cARPRatelimitTrapCount'
_G='h3cARPRatelimitTrapVer'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='accessible-for-notify'
_B='H3C-ARP-RATELIMIT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cARPRatelimit=ModuleIdentity((1,3,6,1,4,1,2011,10,2,110))
if mibBuilder.loadTexts:h3cARPRatelimit.setRevisions(('2013-10-14 18:00','2009-12-08 19:12'))
_H3cARPRatelimitObjects_ObjectIdentity=ObjectIdentity
h3cARPRatelimitObjects=_H3cARPRatelimitObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,110,1))
_H3cARPRatelimitTrap_ObjectIdentity=ObjectIdentity
h3cARPRatelimitTrap=_H3cARPRatelimitTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,110,1,1))
_H3cARPRatelimitTraps_ObjectIdentity=ObjectIdentity
h3cARPRatelimitTraps=_H3cARPRatelimitTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,110,1,1,0))
_H3cARPRatelimitTrapObjects_ObjectIdentity=ObjectIdentity
h3cARPRatelimitTrapObjects=_H3cARPRatelimitTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,110,1,1,1))
_H3cARPRatelimitTrapVer_Type=Unsigned32
_H3cARPRatelimitTrapVer_Object=MibScalar
h3cARPRatelimitTrapVer=_H3cARPRatelimitTrapVer_Object((1,3,6,1,4,1,2011,10,2,110,1,1,1,1),_H3cARPRatelimitTrapVer_Type())
h3cARPRatelimitTrapVer.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cARPRatelimitTrapVer.setStatus(_A)
_H3cARPRatelimitTrapCount_Type=Unsigned32
_H3cARPRatelimitTrapCount_Object=MibScalar
h3cARPRatelimitTrapCount=_H3cARPRatelimitTrapCount_Object((1,3,6,1,4,1,2011,10,2,110,1,1,1,2),_H3cARPRatelimitTrapCount_Type())
h3cARPRatelimitTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cARPRatelimitTrapCount.setStatus(_A)
class _H3cARPRatelimitTrapMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_H3cARPRatelimitTrapMsg_Type.__name__=_D
_H3cARPRatelimitTrapMsg_Object=MibScalar
h3cARPRatelimitTrapMsg=_H3cARPRatelimitTrapMsg_Object((1,3,6,1,4,1,2011,10,2,110,1,1,1,3),_H3cARPRatelimitTrapMsg_Type())
h3cARPRatelimitTrapMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cARPRatelimitTrapMsg.setStatus(_A)
_H3cARPRatelimitConfig_ObjectIdentity=ObjectIdentity
h3cARPRatelimitConfig=_H3cARPRatelimitConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,110,1,2))
_H3cARPRatelimitConfigTable_Object=MibTable
h3cARPRatelimitConfigTable=_H3cARPRatelimitConfigTable_Object((1,3,6,1,4,1,2011,10,2,110,1,2,1))
if mibBuilder.loadTexts:h3cARPRatelimitConfigTable.setStatus(_A)
_H3cARPRatelimitConfigEntry_Object=MibTableRow
h3cARPRatelimitConfigEntry=_H3cARPRatelimitConfigEntry_Object((1,3,6,1,4,1,2011,10,2,110,1,2,1,1))
h3cARPRatelimitConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cARPRatelimitConfigEntry.setStatus(_A)
_H3cARPRatelimitValue_Type=Unsigned32
_H3cARPRatelimitValue_Object=MibTableColumn
h3cARPRatelimitValue=_H3cARPRatelimitValue_Object((1,3,6,1,4,1,2011,10,2,110,1,2,1,1,1),_H3cARPRatelimitValue_Type())
h3cARPRatelimitValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cARPRatelimitValue.setStatus(_A)
h3cARPRatelimitOverspeedTrap=NotificationType((1,3,6,1,4,1,2011,10,2,110,1,1,0,1))
h3cARPRatelimitOverspeedTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:h3cARPRatelimitOverspeedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cARPRatelimit':h3cARPRatelimit,'h3cARPRatelimitObjects':h3cARPRatelimitObjects,'h3cARPRatelimitTrap':h3cARPRatelimitTrap,'h3cARPRatelimitTraps':h3cARPRatelimitTraps,'h3cARPRatelimitOverspeedTrap':h3cARPRatelimitOverspeedTrap,'h3cARPRatelimitTrapObjects':h3cARPRatelimitTrapObjects,_G:h3cARPRatelimitTrapVer,_H:h3cARPRatelimitTrapCount,_I:h3cARPRatelimitTrapMsg,'h3cARPRatelimitConfig':h3cARPRatelimitConfig,'h3cARPRatelimitConfigTable':h3cARPRatelimitConfigTable,'h3cARPRatelimitConfigEntry':h3cARPRatelimitConfigEntry,'h3cARPRatelimitValue':h3cARPRatelimitValue})