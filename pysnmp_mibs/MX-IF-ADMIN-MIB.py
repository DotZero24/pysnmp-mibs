_Q='ifAdminAnalogPortGroupVer1'
_P='ifAdminInitialAdminState'
_O='ifAdminParent'
_N='ifAdminParentType'
_M='ifAdminUsageState'
_L='ifAdminOpState'
_K='ifAdminAdminState'
_J='ifAdminSetAdmin'
_I='locked'
_H='unlocked'
_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='MX-IF-ADMIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
mediatrixAdmin,=mibBuilder.importSymbols('MX-SMI','mediatrixAdmin')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ifAdminMIB=ModuleIdentity((1,3,6,1,4,1,4935,5,8))
if mibBuilder.loadTexts:ifAdminMIB.setRevisions(('2004-06-10 00:00','1901-11-28 00:00'))
_IfAdminMIBObjects_ObjectIdentity=ObjectIdentity
ifAdminMIBObjects=_IfAdminMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,5,8,1))
_IfAdminTable_Object=MibTable
ifAdminTable=_IfAdminTable_Object((1,3,6,1,4,1,4935,5,8,1,10))
if mibBuilder.loadTexts:ifAdminTable.setStatus(_A)
_IfAdminEntry_Object=MibTableRow
ifAdminEntry=_IfAdminEntry_Object((1,3,6,1,4,1,4935,5,8,1,10,1))
ifAdminEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ifAdminEntry.setStatus(_A)
class _IfAdminSetAdmin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('noOp',0),('permanentUnlock',1),('lock',2),('forcelock',3),('permanentForcelock',4),('unlock',5)))
_IfAdminSetAdmin_Type.__name__=_C
_IfAdminSetAdmin_Object=MibTableColumn
ifAdminSetAdmin=_IfAdminSetAdmin_Object((1,3,6,1,4,1,4935,5,8,1,10,1,2),_IfAdminSetAdmin_Type())
ifAdminSetAdmin.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAdminSetAdmin.setStatus(_A)
class _IfAdminAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('shuttingDown',2),(_I,3),('permanentlock',4)))
_IfAdminAdminState_Type.__name__=_C
_IfAdminAdminState_Object=MibTableColumn
ifAdminAdminState=_IfAdminAdminState_Object((1,3,6,1,4,1,4935,5,8,1,10,1,3),_IfAdminAdminState_Type())
ifAdminAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAdminAdminState.setStatus(_A)
class _IfAdminOpState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IfAdminOpState_Type.__name__=_C
_IfAdminOpState_Object=MibTableColumn
ifAdminOpState=_IfAdminOpState_Object((1,3,6,1,4,1,4935,5,8,1,10,1,4),_IfAdminOpState_Type())
ifAdminOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAdminOpState.setStatus(_A)
class _IfAdminUsageState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('active',2),('busy',3),('idle-unusable',4)))
_IfAdminUsageState_Type.__name__=_C
_IfAdminUsageState_Object=MibTableColumn
ifAdminUsageState=_IfAdminUsageState_Object((1,3,6,1,4,1,4935,5,8,1,10,1,5),_IfAdminUsageState_Type())
ifAdminUsageState.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAdminUsageState.setStatus(_A)
class _IfAdminParentType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('groupAdmin',1),('ifAdmin',2)))
_IfAdminParentType_Type.__name__=_C
_IfAdminParentType_Object=MibTableColumn
ifAdminParentType=_IfAdminParentType_Object((1,3,6,1,4,1,4935,5,8,1,10,1,14),_IfAdminParentType_Type())
ifAdminParentType.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAdminParentType.setStatus(_A)
_IfAdminParent_Type=Integer32
_IfAdminParent_Object=MibTableColumn
ifAdminParent=_IfAdminParent_Object((1,3,6,1,4,1,4935,5,8,1,10,1,15),_IfAdminParent_Type())
ifAdminParent.setMaxAccess(_D)
if mibBuilder.loadTexts:ifAdminParent.setStatus(_A)
class _IfAdminInitialAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IfAdminInitialAdminState_Type.__name__=_C
_IfAdminInitialAdminState_Object=MibTableColumn
ifAdminInitialAdminState=_IfAdminInitialAdminState_Object((1,3,6,1,4,1,4935,5,8,1,10,1,65),_IfAdminInitialAdminState_Type())
ifAdminInitialAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:ifAdminInitialAdminState.setStatus(_A)
_IfAdminConformance_ObjectIdentity=ObjectIdentity
ifAdminConformance=_IfAdminConformance_ObjectIdentity((1,3,6,1,4,1,4935,5,8,2))
_IfAdminCompliances_ObjectIdentity=ObjectIdentity
ifAdminCompliances=_IfAdminCompliances_ObjectIdentity((1,3,6,1,4,1,4935,5,8,2,1))
_IfAdminGroups_ObjectIdentity=ObjectIdentity
ifAdminGroups=_IfAdminGroups_ObjectIdentity((1,3,6,1,4,1,4935,5,8,2,2))
ifAdminAnalogPortGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,5,8,2,2,1))
ifAdminAnalogPortGroupVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ifAdminAnalogPortGroupVer1.setStatus(_A)
ifAdminAnalogPortComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,5,8,2,1,1))
ifAdminAnalogPortComplVer1.setObjects((_B,_Q))
if mibBuilder.loadTexts:ifAdminAnalogPortComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ifAdminMIB':ifAdminMIB,'ifAdminMIBObjects':ifAdminMIBObjects,'ifAdminTable':ifAdminTable,'ifAdminEntry':ifAdminEntry,_J:ifAdminSetAdmin,_K:ifAdminAdminState,_L:ifAdminOpState,_M:ifAdminUsageState,_N:ifAdminParentType,_O:ifAdminParent,_P:ifAdminInitialAdminState,'ifAdminConformance':ifAdminConformance,'ifAdminCompliances':ifAdminCompliances,'ifAdminAnalogPortComplVer1':ifAdminAnalogPortComplVer1,'ifAdminGroups':ifAdminGroups,_Q:ifAdminAnalogPortGroupVer1})