_P='hpSwitchAccountingConfigGroup1'
_O='hpSwitchAccountingConfigGroup'
_N='hpSwitchAcctSessIdIncSwitchIdentity'
_M='deprecated'
_L='hpSwitchAcctServiceIndex'
_K='DisplayString'
_J='hpSwitchAcctServiceServerGroupName'
_I='hpSwitchAcctServiceMode'
_H='hpSwitchAcctServiceMethod'
_G='hpSwitchAcctSessionIdentification'
_F='hpSwitchAcctSuppressNullUserName'
_E='hpSwitchAcctUpdateInterval'
_D='read-write'
_C='Integer32'
_B='current'
_A='HP-ACCT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
hpSwitchAccountingMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,17))
if mibBuilder.loadTexts:hpSwitchAccountingMIB.setRevisions(('2019-09-26 00:00','2017-11-22 00:00','2014-08-04 00:00','2011-03-05 00:00','2009-07-14 00:00','2008-07-11 00:00','2001-08-22 02:38'))
_HpSwitchAccountingConfig_ObjectIdentity=ObjectIdentity
hpSwitchAccountingConfig=_HpSwitchAccountingConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,17,1))
class _HpSwitchAcctUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,525600))
_HpSwitchAcctUpdateInterval_Type.__name__=_C
_HpSwitchAcctUpdateInterval_Object=MibScalar
hpSwitchAcctUpdateInterval=_HpSwitchAcctUpdateInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,1,1),_HpSwitchAcctUpdateInterval_Type())
hpSwitchAcctUpdateInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctUpdateInterval.setStatus(_B)
class _HpSwitchAcctSuppressNullUserName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpSwitchAcctSuppressNullUserName_Type.__name__=_C
_HpSwitchAcctSuppressNullUserName_Object=MibScalar
hpSwitchAcctSuppressNullUserName=_HpSwitchAcctSuppressNullUserName_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,1,2),_HpSwitchAcctSuppressNullUserName_Type())
hpSwitchAcctSuppressNullUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctSuppressNullUserName.setStatus(_B)
class _HpSwitchAcctSessionIdentification_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unique',1),('common',2)))
_HpSwitchAcctSessionIdentification_Type.__name__=_C
_HpSwitchAcctSessionIdentification_Object=MibScalar
hpSwitchAcctSessionIdentification=_HpSwitchAcctSessionIdentification_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,1,3),_HpSwitchAcctSessionIdentification_Type())
hpSwitchAcctSessionIdentification.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctSessionIdentification.setStatus(_B)
class _HpSwitchAcctSessIdIncSwitchIdentity_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpSwitchAcctSessIdIncSwitchIdentity_Type.__name__=_C
_HpSwitchAcctSessIdIncSwitchIdentity_Object=MibScalar
hpSwitchAcctSessIdIncSwitchIdentity=_HpSwitchAcctSessIdIncSwitchIdentity_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,1,4),_HpSwitchAcctSessIdIncSwitchIdentity_Type())
hpSwitchAcctSessIdIncSwitchIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctSessIdIncSwitchIdentity.setStatus(_B)
_HpSwitchAcctServiceTable_Object=MibTable
hpSwitchAcctServiceTable=_HpSwitchAcctServiceTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2))
if mibBuilder.loadTexts:hpSwitchAcctServiceTable.setStatus(_B)
_HpSwitchAcctServiceEntry_Object=MibTableRow
hpSwitchAcctServiceEntry=_HpSwitchAcctServiceEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2,1))
hpSwitchAcctServiceEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:hpSwitchAcctServiceEntry.setStatus(_B)
class _HpSwitchAcctServiceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('network',1),('exec',2),('system',3),('commands',4),('restUri',5)))
_HpSwitchAcctServiceIndex_Type.__name__=_C
_HpSwitchAcctServiceIndex_Object=MibTableColumn
hpSwitchAcctServiceIndex=_HpSwitchAcctServiceIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2,1,1),_HpSwitchAcctServiceIndex_Type())
hpSwitchAcctServiceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpSwitchAcctServiceIndex.setStatus(_B)
class _HpSwitchAcctServiceMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('radius',2),('syslog',3),('tacacs',4)))
_HpSwitchAcctServiceMethod_Type.__name__=_C
_HpSwitchAcctServiceMethod_Object=MibTableColumn
hpSwitchAcctServiceMethod=_HpSwitchAcctServiceMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2,1,2),_HpSwitchAcctServiceMethod_Type())
hpSwitchAcctServiceMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctServiceMethod.setStatus(_B)
class _HpSwitchAcctServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('startStop',2),('stopOnly',3),('interimUpdate',4)))
_HpSwitchAcctServiceMode_Type.__name__=_C
_HpSwitchAcctServiceMode_Object=MibTableColumn
hpSwitchAcctServiceMode=_HpSwitchAcctServiceMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2,1,3),_HpSwitchAcctServiceMode_Type())
hpSwitchAcctServiceMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctServiceMode.setStatus(_B)
class _HpSwitchAcctServiceServerGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchAcctServiceServerGroupName_Type.__name__=_K
_HpSwitchAcctServiceServerGroupName_Object=MibTableColumn
hpSwitchAcctServiceServerGroupName=_HpSwitchAcctServiceServerGroupName_Object((1,3,6,1,4,1,11,2,14,11,5,1,17,2,1,4),_HpSwitchAcctServiceServerGroupName_Type())
hpSwitchAcctServiceServerGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchAcctServiceServerGroupName.setStatus(_B)
_HpSwitchAccountingMIBConformance_ObjectIdentity=ObjectIdentity
hpSwitchAccountingMIBConformance=_HpSwitchAccountingMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,17,3))
_HpSwitchAccountingMIBCompliances_ObjectIdentity=ObjectIdentity
hpSwitchAccountingMIBCompliances=_HpSwitchAccountingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,17,3,1))
_HpSwitchAccountingMIBGroups_ObjectIdentity=ObjectIdentity
hpSwitchAccountingMIBGroups=_HpSwitchAccountingMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,17,3,2))
hpSwitchAccountingConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,17,3,2,1))
hpSwitchAccountingConfigGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hpSwitchAccountingConfigGroup.setStatus(_M)
hpSwitchAccountingConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,17,3,2,2))
hpSwitchAccountingConfigGroup1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:hpSwitchAccountingConfigGroup1.setStatus(_B)
hpSwitchAccountingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,17,3,1,1))
hpSwitchAccountingMIBCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:hpSwitchAccountingMIBCompliance.setStatus(_M)
hpSwitchAccountingMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,17,3,1,2))
hpSwitchAccountingMIBCompliance1.setObjects((_A,_P))
if mibBuilder.loadTexts:hpSwitchAccountingMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpSwitchAccountingMIB':hpSwitchAccountingMIB,'hpSwitchAccountingConfig':hpSwitchAccountingConfig,_E:hpSwitchAcctUpdateInterval,_F:hpSwitchAcctSuppressNullUserName,_G:hpSwitchAcctSessionIdentification,_N:hpSwitchAcctSessIdIncSwitchIdentity,'hpSwitchAcctServiceTable':hpSwitchAcctServiceTable,'hpSwitchAcctServiceEntry':hpSwitchAcctServiceEntry,_L:hpSwitchAcctServiceIndex,_H:hpSwitchAcctServiceMethod,_I:hpSwitchAcctServiceMode,_J:hpSwitchAcctServiceServerGroupName,'hpSwitchAccountingMIBConformance':hpSwitchAccountingMIBConformance,'hpSwitchAccountingMIBCompliances':hpSwitchAccountingMIBCompliances,'hpSwitchAccountingMIBCompliance':hpSwitchAccountingMIBCompliance,'hpSwitchAccountingMIBCompliance1':hpSwitchAccountingMIBCompliance1,'hpSwitchAccountingMIBGroups':hpSwitchAccountingMIBGroups,_O:hpSwitchAccountingConfigGroup,_P:hpSwitchAccountingConfigGroup1})