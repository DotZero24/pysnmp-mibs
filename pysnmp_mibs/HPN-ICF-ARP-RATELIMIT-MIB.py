_I='hpnicfARPRatelimitTrapMsg'
_H='hpnicfARPRatelimitTrapCount'
_G='hpnicfARPRatelimitTrapVer'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='accessible-for-notify'
_B='HPN-ICF-ARP-RATELIMIT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfARPRatelimit=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110))
if mibBuilder.loadTexts:hpnicfARPRatelimit.setRevisions(('2013-10-14 18:00','2009-12-08 19:12'))
_HpnicfARPRatelimitObjects_ObjectIdentity=ObjectIdentity
hpnicfARPRatelimitObjects=_HpnicfARPRatelimitObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110,1))
_HpnicfARPRatelimitTrap_ObjectIdentity=ObjectIdentity
hpnicfARPRatelimitTrap=_HpnicfARPRatelimitTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1))
_HpnicfARPRatelimitTraps_ObjectIdentity=ObjectIdentity
hpnicfARPRatelimitTraps=_HpnicfARPRatelimitTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,0))
_HpnicfARPRatelimitTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfARPRatelimitTrapObjects=_HpnicfARPRatelimitTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,1))
_HpnicfARPRatelimitTrapVer_Type=Unsigned32
_HpnicfARPRatelimitTrapVer_Object=MibScalar
hpnicfARPRatelimitTrapVer=_HpnicfARPRatelimitTrapVer_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,1,1),_HpnicfARPRatelimitTrapVer_Type())
hpnicfARPRatelimitTrapVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfARPRatelimitTrapVer.setStatus(_A)
_HpnicfARPRatelimitTrapCount_Type=Unsigned32
_HpnicfARPRatelimitTrapCount_Object=MibScalar
hpnicfARPRatelimitTrapCount=_HpnicfARPRatelimitTrapCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,1,2),_HpnicfARPRatelimitTrapCount_Type())
hpnicfARPRatelimitTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfARPRatelimitTrapCount.setStatus(_A)
class _HpnicfARPRatelimitTrapMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_HpnicfARPRatelimitTrapMsg_Type.__name__=_D
_HpnicfARPRatelimitTrapMsg_Object=MibScalar
hpnicfARPRatelimitTrapMsg=_HpnicfARPRatelimitTrapMsg_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,1,3),_HpnicfARPRatelimitTrapMsg_Type())
hpnicfARPRatelimitTrapMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfARPRatelimitTrapMsg.setStatus(_A)
_HpnicfARPRatelimitConfig_ObjectIdentity=ObjectIdentity
hpnicfARPRatelimitConfig=_HpnicfARPRatelimitConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,110,1,2))
_HpnicfARPRatelimitConfigTable_Object=MibTable
hpnicfARPRatelimitConfigTable=_HpnicfARPRatelimitConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,2,1))
if mibBuilder.loadTexts:hpnicfARPRatelimitConfigTable.setStatus(_A)
_HpnicfARPRatelimitConfigEntry_Object=MibTableRow
hpnicfARPRatelimitConfigEntry=_HpnicfARPRatelimitConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,2,1,1))
hpnicfARPRatelimitConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfARPRatelimitConfigEntry.setStatus(_A)
_HpnicfARPRatelimitValue_Type=Unsigned32
_HpnicfARPRatelimitValue_Object=MibTableColumn
hpnicfARPRatelimitValue=_HpnicfARPRatelimitValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,110,1,2,1,1,1),_HpnicfARPRatelimitValue_Type())
hpnicfARPRatelimitValue.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfARPRatelimitValue.setStatus(_A)
hpnicfARPRatelimitOverspeedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,110,1,1,0,1))
hpnicfARPRatelimitOverspeedTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:hpnicfARPRatelimitOverspeedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfARPRatelimit':hpnicfARPRatelimit,'hpnicfARPRatelimitObjects':hpnicfARPRatelimitObjects,'hpnicfARPRatelimitTrap':hpnicfARPRatelimitTrap,'hpnicfARPRatelimitTraps':hpnicfARPRatelimitTraps,'hpnicfARPRatelimitOverspeedTrap':hpnicfARPRatelimitOverspeedTrap,'hpnicfARPRatelimitTrapObjects':hpnicfARPRatelimitTrapObjects,_G:hpnicfARPRatelimitTrapVer,_H:hpnicfARPRatelimitTrapCount,_I:hpnicfARPRatelimitTrapMsg,'hpnicfARPRatelimitConfig':hpnicfARPRatelimitConfig,'hpnicfARPRatelimitConfigTable':hpnicfARPRatelimitConfigTable,'hpnicfARPRatelimitConfigEntry':hpnicfARPRatelimitConfigEntry,'hpnicfARPRatelimitValue':hpnicfARPRatelimitValue})