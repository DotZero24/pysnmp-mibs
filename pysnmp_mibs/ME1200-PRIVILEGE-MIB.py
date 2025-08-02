_J='me1200PrivilegeConfigWebInfoGroup'
_I='me1200PrivilegeConfigWebStatusRwPriv'
_H='me1200PrivilegeConfigWebStatusRoPriv'
_G='me1200PrivilegeConfigWebConfigRwPriv'
_F='me1200PrivilegeConfigWebConfigRoPriv'
_E='me1200PrivilegeConfigWebModuleName'
_D='ME1200DisplayString'
_C='read-write'
_B='ME1200-PRIVILEGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,=mibBuilder.importSymbols('ME1200-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
me1200PrivilegeMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,59))
if mibBuilder.loadTexts:me1200PrivilegeMib.setRevisions(('2014-04-17 00:00',))
_Me1200PrivilegeMibObjects_ObjectIdentity=ObjectIdentity
me1200PrivilegeMibObjects=_Me1200PrivilegeMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,59,1))
_Me1200PrivilegeConfig_ObjectIdentity=ObjectIdentity
me1200PrivilegeConfig=_Me1200PrivilegeConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,59,1,2))
_Me1200PrivilegeConfigWebTable_Object=MibTable
me1200PrivilegeConfigWebTable=_Me1200PrivilegeConfigWebTable_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1))
if mibBuilder.loadTexts:me1200PrivilegeConfigWebTable.setStatus(_A)
_Me1200PrivilegeConfigWebEntry_Object=MibTableRow
me1200PrivilegeConfigWebEntry=_Me1200PrivilegeConfigWebEntry_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1))
me1200PrivilegeConfigWebEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:me1200PrivilegeConfigWebEntry.setStatus(_A)
class _Me1200PrivilegeConfigWebModuleName_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Me1200PrivilegeConfigWebModuleName_Type.__name__=_D
_Me1200PrivilegeConfigWebModuleName_Object=MibTableColumn
me1200PrivilegeConfigWebModuleName=_Me1200PrivilegeConfigWebModuleName_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1,1),_Me1200PrivilegeConfigWebModuleName_Type())
me1200PrivilegeConfigWebModuleName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:me1200PrivilegeConfigWebModuleName.setStatus(_A)
_Me1200PrivilegeConfigWebConfigRoPriv_Type=Unsigned32
_Me1200PrivilegeConfigWebConfigRoPriv_Object=MibTableColumn
me1200PrivilegeConfigWebConfigRoPriv=_Me1200PrivilegeConfigWebConfigRoPriv_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1,2),_Me1200PrivilegeConfigWebConfigRoPriv_Type())
me1200PrivilegeConfigWebConfigRoPriv.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200PrivilegeConfigWebConfigRoPriv.setStatus(_A)
_Me1200PrivilegeConfigWebConfigRwPriv_Type=Unsigned32
_Me1200PrivilegeConfigWebConfigRwPriv_Object=MibTableColumn
me1200PrivilegeConfigWebConfigRwPriv=_Me1200PrivilegeConfigWebConfigRwPriv_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1,3),_Me1200PrivilegeConfigWebConfigRwPriv_Type())
me1200PrivilegeConfigWebConfigRwPriv.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200PrivilegeConfigWebConfigRwPriv.setStatus(_A)
_Me1200PrivilegeConfigWebStatusRoPriv_Type=Unsigned32
_Me1200PrivilegeConfigWebStatusRoPriv_Object=MibTableColumn
me1200PrivilegeConfigWebStatusRoPriv=_Me1200PrivilegeConfigWebStatusRoPriv_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1,4),_Me1200PrivilegeConfigWebStatusRoPriv_Type())
me1200PrivilegeConfigWebStatusRoPriv.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200PrivilegeConfigWebStatusRoPriv.setStatus(_A)
_Me1200PrivilegeConfigWebStatusRwPriv_Type=Unsigned32
_Me1200PrivilegeConfigWebStatusRwPriv_Object=MibTableColumn
me1200PrivilegeConfigWebStatusRwPriv=_Me1200PrivilegeConfigWebStatusRwPriv_Object((1,3,6,1,4,1,9,9,815,1,59,1,2,1,1,5),_Me1200PrivilegeConfigWebStatusRwPriv_Type())
me1200PrivilegeConfigWebStatusRwPriv.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200PrivilegeConfigWebStatusRwPriv.setStatus(_A)
_Me1200PrivilegeMibConformance_ObjectIdentity=ObjectIdentity
me1200PrivilegeMibConformance=_Me1200PrivilegeMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,59,2))
_Me1200PrivilegeMibCompliances_ObjectIdentity=ObjectIdentity
me1200PrivilegeMibCompliances=_Me1200PrivilegeMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,59,2,1))
_Me1200PrivilegeMibGroups_ObjectIdentity=ObjectIdentity
me1200PrivilegeMibGroups=_Me1200PrivilegeMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,59,2,2))
me1200PrivilegeConfigWebInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,59,2,2,1))
me1200PrivilegeConfigWebInfoGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:me1200PrivilegeConfigWebInfoGroup.setStatus(_A)
me1200PrivilegeMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,59,2,1,1))
me1200PrivilegeMibCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:me1200PrivilegeMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'me1200PrivilegeMib':me1200PrivilegeMib,'me1200PrivilegeMibObjects':me1200PrivilegeMibObjects,'me1200PrivilegeConfig':me1200PrivilegeConfig,'me1200PrivilegeConfigWebTable':me1200PrivilegeConfigWebTable,'me1200PrivilegeConfigWebEntry':me1200PrivilegeConfigWebEntry,_E:me1200PrivilegeConfigWebModuleName,_F:me1200PrivilegeConfigWebConfigRoPriv,_G:me1200PrivilegeConfigWebConfigRwPriv,_H:me1200PrivilegeConfigWebStatusRoPriv,_I:me1200PrivilegeConfigWebStatusRwPriv,'me1200PrivilegeMibConformance':me1200PrivilegeMibConformance,'me1200PrivilegeMibCompliances':me1200PrivilegeMibCompliances,'me1200PrivilegeMibCompliance':me1200PrivilegeMibCompliance,'me1200PrivilegeMibGroups':me1200PrivilegeMibGroups,_J:me1200PrivilegeConfigWebInfoGroup})