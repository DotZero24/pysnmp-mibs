_K='intSrvGuaranteedIfAttribGroup'
_J='intSrvGuaranteedIfStatus'
_I='intSrvGuaranteedIfSlack'
_H='intSrvGuaranteedIfD'
_G='intSrvGuaranteedIfC'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='Integer32'
_B='INT-SERV-GUARANTEED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
intSrv,=mibBuilder.importSymbols('INT-SERV-MIB','intSrv')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
intSrvGuaranteed=ModuleIdentity((1,3,6,1,2,1,52,4))
_IntSrvGuaranteedObjects_ObjectIdentity=ObjectIdentity
intSrvGuaranteedObjects=_IntSrvGuaranteedObjects_ObjectIdentity((1,3,6,1,2,1,52,4,1))
_IntSrvGuaranteedIfTable_Object=MibTable
intSrvGuaranteedIfTable=_IntSrvGuaranteedIfTable_Object((1,3,6,1,2,1,52,4,1,1))
if mibBuilder.loadTexts:intSrvGuaranteedIfTable.setStatus(_A)
_IntSrvGuaranteedIfEntry_Object=MibTableRow
intSrvGuaranteedIfEntry=_IntSrvGuaranteedIfEntry_Object((1,3,6,1,2,1,52,4,1,1,1))
intSrvGuaranteedIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:intSrvGuaranteedIfEntry.setStatus(_A)
class _IntSrvGuaranteedIfC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_IntSrvGuaranteedIfC_Type.__name__=_C
_IntSrvGuaranteedIfC_Object=MibTableColumn
intSrvGuaranteedIfC=_IntSrvGuaranteedIfC_Object((1,3,6,1,2,1,52,4,1,1,1,1),_IntSrvGuaranteedIfC_Type())
intSrvGuaranteedIfC.setMaxAccess(_D)
if mibBuilder.loadTexts:intSrvGuaranteedIfC.setStatus(_A)
if mibBuilder.loadTexts:intSrvGuaranteedIfC.setUnits('bytes')
class _IntSrvGuaranteedIfD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_IntSrvGuaranteedIfD_Type.__name__=_C
_IntSrvGuaranteedIfD_Object=MibTableColumn
intSrvGuaranteedIfD=_IntSrvGuaranteedIfD_Object((1,3,6,1,2,1,52,4,1,1,1,2),_IntSrvGuaranteedIfD_Type())
intSrvGuaranteedIfD.setMaxAccess(_D)
if mibBuilder.loadTexts:intSrvGuaranteedIfD.setStatus(_A)
if mibBuilder.loadTexts:intSrvGuaranteedIfD.setUnits('microseconds')
class _IntSrvGuaranteedIfSlack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_IntSrvGuaranteedIfSlack_Type.__name__=_C
_IntSrvGuaranteedIfSlack_Object=MibTableColumn
intSrvGuaranteedIfSlack=_IntSrvGuaranteedIfSlack_Object((1,3,6,1,2,1,52,4,1,1,1,3),_IntSrvGuaranteedIfSlack_Type())
intSrvGuaranteedIfSlack.setMaxAccess(_D)
if mibBuilder.loadTexts:intSrvGuaranteedIfSlack.setStatus(_A)
_IntSrvGuaranteedIfStatus_Type=RowStatus
_IntSrvGuaranteedIfStatus_Object=MibTableColumn
intSrvGuaranteedIfStatus=_IntSrvGuaranteedIfStatus_Object((1,3,6,1,2,1,52,4,1,1,1,4),_IntSrvGuaranteedIfStatus_Type())
intSrvGuaranteedIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:intSrvGuaranteedIfStatus.setStatus(_A)
_IntSrvGuaranteedNotifications_ObjectIdentity=ObjectIdentity
intSrvGuaranteedNotifications=_IntSrvGuaranteedNotifications_ObjectIdentity((1,3,6,1,2,1,52,4,2))
_IntSrvGuaranteedConformance_ObjectIdentity=ObjectIdentity
intSrvGuaranteedConformance=_IntSrvGuaranteedConformance_ObjectIdentity((1,3,6,1,2,1,52,4,3))
_IntSrvGuaranteedGroups_ObjectIdentity=ObjectIdentity
intSrvGuaranteedGroups=_IntSrvGuaranteedGroups_ObjectIdentity((1,3,6,1,2,1,52,4,3,1))
_IntSrvGuaranteedCompliances_ObjectIdentity=ObjectIdentity
intSrvGuaranteedCompliances=_IntSrvGuaranteedCompliances_ObjectIdentity((1,3,6,1,2,1,52,4,3,2))
intSrvGuaranteedIfAttribGroup=ObjectGroup((1,3,6,1,2,1,52,4,3,1,2))
intSrvGuaranteedIfAttribGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:intSrvGuaranteedIfAttribGroup.setStatus(_A)
intSrvGuaranteedCompliance=ModuleCompliance((1,3,6,1,2,1,52,4,3,2,1))
intSrvGuaranteedCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:intSrvGuaranteedCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'intSrvGuaranteed':intSrvGuaranteed,'intSrvGuaranteedObjects':intSrvGuaranteedObjects,'intSrvGuaranteedIfTable':intSrvGuaranteedIfTable,'intSrvGuaranteedIfEntry':intSrvGuaranteedIfEntry,_G:intSrvGuaranteedIfC,_H:intSrvGuaranteedIfD,_I:intSrvGuaranteedIfSlack,_J:intSrvGuaranteedIfStatus,'intSrvGuaranteedNotifications':intSrvGuaranteedNotifications,'intSrvGuaranteedConformance':intSrvGuaranteedConformance,'intSrvGuaranteedGroups':intSrvGuaranteedGroups,_K:intSrvGuaranteedIfAttribGroup,'intSrvGuaranteedCompliances':intSrvGuaranteedCompliances,'intSrvGuaranteedCompliance':intSrvGuaranteedCompliance})