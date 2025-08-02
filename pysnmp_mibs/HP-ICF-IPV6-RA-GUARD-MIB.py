_M='hpicfIpv6RAGuardGroup'
_L='hpicfRAGuardLastErrorCode'
_K='hpicfRAGuardPortLog'
_J='hpicfRAGuardPortBlockedRedirs'
_I='hpicfRAGuardPortBlockedRAs'
_H='hpicfRAGuardPortBlocked'
_G='read-write'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='HP-ICF-IPV6-RA-GUARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpicfIpv6RAGuard=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87))
if mibBuilder.loadTexts:hpicfIpv6RAGuard.setRevisions(('2011-03-16 05:24',))
_HpicfIpv6RAGuardObjects_ObjectIdentity=ObjectIdentity
hpicfIpv6RAGuardObjects=_HpicfIpv6RAGuardObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87,1))
_HpicfIpv6RAGuardConfig_ObjectIdentity=ObjectIdentity
hpicfIpv6RAGuardConfig=_HpicfIpv6RAGuardConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1))
_HpicfRAGuardPortTable_Object=MibTable
hpicfRAGuardPortTable=_HpicfRAGuardPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1))
if mibBuilder.loadTexts:hpicfRAGuardPortTable.setStatus(_A)
_HpicfRAGuardPortEntry_Object=MibTableRow
hpicfRAGuardPortEntry=_HpicfRAGuardPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1))
hpicfRAGuardPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpicfRAGuardPortEntry.setStatus(_A)
_HpicfRAGuardPortBlocked_Type=TruthValue
_HpicfRAGuardPortBlocked_Object=MibTableColumn
hpicfRAGuardPortBlocked=_HpicfRAGuardPortBlocked_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1,1),_HpicfRAGuardPortBlocked_Type())
hpicfRAGuardPortBlocked.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfRAGuardPortBlocked.setStatus(_A)
_HpicfRAGuardPortBlockedRAs_Type=Counter64
_HpicfRAGuardPortBlockedRAs_Object=MibTableColumn
hpicfRAGuardPortBlockedRAs=_HpicfRAGuardPortBlockedRAs_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1,2),_HpicfRAGuardPortBlockedRAs_Type())
hpicfRAGuardPortBlockedRAs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfRAGuardPortBlockedRAs.setStatus(_A)
_HpicfRAGuardPortBlockedRedirs_Type=Counter64
_HpicfRAGuardPortBlockedRedirs_Object=MibTableColumn
hpicfRAGuardPortBlockedRedirs=_HpicfRAGuardPortBlockedRedirs_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1,3),_HpicfRAGuardPortBlockedRedirs_Type())
hpicfRAGuardPortBlockedRedirs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfRAGuardPortBlockedRedirs.setStatus(_A)
_HpicfRAGuardPortLog_Type=TruthValue
_HpicfRAGuardPortLog_Object=MibTableColumn
hpicfRAGuardPortLog=_HpicfRAGuardPortLog_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1,4),_HpicfRAGuardPortLog_Type())
hpicfRAGuardPortLog.setMaxAccess(_G)
if mibBuilder.loadTexts:hpicfRAGuardPortLog.setStatus(_A)
class _HpicfRAGuardLastErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noError',1),('insufficientHardwareResources',2),('genericError',3)))
_HpicfRAGuardLastErrorCode_Type.__name__=_F
_HpicfRAGuardLastErrorCode_Object=MibTableColumn
hpicfRAGuardLastErrorCode=_HpicfRAGuardLastErrorCode_Object((1,3,6,1,4,1,11,2,14,11,5,1,87,1,1,1,1,5),_HpicfRAGuardLastErrorCode_Type())
hpicfRAGuardLastErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfRAGuardLastErrorCode.setStatus(_A)
_HpicfIpv6RAGuardConformance_ObjectIdentity=ObjectIdentity
hpicfIpv6RAGuardConformance=_HpicfIpv6RAGuardConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87,2))
_HpicfIpv6RAGuardCompliances_ObjectIdentity=ObjectIdentity
hpicfIpv6RAGuardCompliances=_HpicfIpv6RAGuardCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87,2,1))
_HpicfIpv6RAGuardGroups_ObjectIdentity=ObjectIdentity
hpicfIpv6RAGuardGroups=_HpicfIpv6RAGuardGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,87,2,2))
hpicfIpv6RAGuardGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,87,2,2,1))
hpicfIpv6RAGuardGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfIpv6RAGuardGroup.setStatus(_A)
hpicfIpv6RAGuardCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,87,2,1,1))
hpicfIpv6RAGuardCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:hpicfIpv6RAGuardCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfIpv6RAGuard':hpicfIpv6RAGuard,'hpicfIpv6RAGuardObjects':hpicfIpv6RAGuardObjects,'hpicfIpv6RAGuardConfig':hpicfIpv6RAGuardConfig,'hpicfRAGuardPortTable':hpicfRAGuardPortTable,'hpicfRAGuardPortEntry':hpicfRAGuardPortEntry,_H:hpicfRAGuardPortBlocked,_I:hpicfRAGuardPortBlockedRAs,_J:hpicfRAGuardPortBlockedRedirs,_K:hpicfRAGuardPortLog,_L:hpicfRAGuardLastErrorCode,'hpicfIpv6RAGuardConformance':hpicfIpv6RAGuardConformance,'hpicfIpv6RAGuardCompliances':hpicfIpv6RAGuardCompliances,'hpicfIpv6RAGuardCompliance':hpicfIpv6RAGuardCompliance,'hpicfIpv6RAGuardGroups':hpicfIpv6RAGuardGroups,_M:hpicfIpv6RAGuardGroup})