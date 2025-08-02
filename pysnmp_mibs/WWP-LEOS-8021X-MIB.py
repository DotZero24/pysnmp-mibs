_H='wwpLeos8021xSuppPort'
_G='read-only'
_F='wwpLeos8021xPort'
_E='WWP-LEOS-8021X-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeos8021xMibModule=ModuleIdentity((1,3,6,1,4,1,6141,2,60,401))
if mibBuilder.loadTexts:wwpLeos8021xMibModule.setRevisions(('2005-08-28 19:35',))
_WwpLeos8021xMIB_ObjectIdentity=ObjectIdentity
wwpLeos8021xMIB=_WwpLeos8021xMIB_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1))
_WwpLeos8021xConf_ObjectIdentity=ObjectIdentity
wwpLeos8021xConf=_WwpLeos8021xConf_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,1))
_WwpLeos8021xGroups_ObjectIdentity=ObjectIdentity
wwpLeos8021xGroups=_WwpLeos8021xGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,1,1))
_WwpLeos8021xCompls_ObjectIdentity=ObjectIdentity
wwpLeos8021xCompls=_WwpLeos8021xCompls_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,1,2))
_WwpLeos8021xObjs_ObjectIdentity=ObjectIdentity
wwpLeos8021xObjs=_WwpLeos8021xObjs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,2))
_WwpLeos8021xPortTable_Object=MibTable
wwpLeos8021xPortTable=_WwpLeos8021xPortTable_Object((1,3,6,1,4,1,6141,2,60,401,1,2,1))
if mibBuilder.loadTexts:wwpLeos8021xPortTable.setStatus(_A)
_WwpLeos8021xPortEntry_Object=MibTableRow
wwpLeos8021xPortEntry=_WwpLeos8021xPortEntry_Object((1,3,6,1,4,1,6141,2,60,401,1,2,1,1))
wwpLeos8021xPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeos8021xPortEntry.setStatus(_A)
class _WwpLeos8021xPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeos8021xPort_Type.__name__=_C
_WwpLeos8021xPort_Object=MibTableColumn
wwpLeos8021xPort=_WwpLeos8021xPort_Object((1,3,6,1,4,1,6141,2,60,401,1,2,1,1,1),_WwpLeos8021xPort_Type())
wwpLeos8021xPort.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeos8021xPort.setStatus(_A)
class _WwpLeos8021xRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('supplicant',2),('authenticator',3),('both',4)))
_WwpLeos8021xRole_Type.__name__=_C
_WwpLeos8021xRole_Object=MibTableColumn
wwpLeos8021xRole=_WwpLeos8021xRole_Object((1,3,6,1,4,1,6141,2,60,401,1,2,1,1,2),_WwpLeos8021xRole_Type())
wwpLeos8021xRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xRole.setStatus(_A)
_WwpLeos8021xAuthPortStatsClear_Type=TruthValue
_WwpLeos8021xAuthPortStatsClear_Object=MibTableColumn
wwpLeos8021xAuthPortStatsClear=_WwpLeos8021xAuthPortStatsClear_Object((1,3,6,1,4,1,6141,2,60,401,1,2,1,1,3),_WwpLeos8021xAuthPortStatsClear_Type())
wwpLeos8021xAuthPortStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xAuthPortStatsClear.setStatus(_A)
_WwpLeos8021xSuppTable_Object=MibTable
wwpLeos8021xSuppTable=_WwpLeos8021xSuppTable_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2))
if mibBuilder.loadTexts:wwpLeos8021xSuppTable.setStatus(_A)
_WwpLeos8021xSuppEntry_Object=MibTableRow
wwpLeos8021xSuppEntry=_WwpLeos8021xSuppEntry_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1))
wwpLeos8021xSuppEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeos8021xSuppEntry.setStatus(_A)
class _WwpLeos8021xSuppPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeos8021xSuppPort_Type.__name__=_C
_WwpLeos8021xSuppPort_Object=MibTableColumn
wwpLeos8021xSuppPort=_WwpLeos8021xSuppPort_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1,1),_WwpLeos8021xSuppPort_Type())
wwpLeos8021xSuppPort.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeos8021xSuppPort.setStatus(_A)
class _WwpLeos8021xSuppUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeos8021xSuppUserName_Type.__name__=_D
_WwpLeos8021xSuppUserName_Object=MibTableColumn
wwpLeos8021xSuppUserName=_WwpLeos8021xSuppUserName_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1,2),_WwpLeos8021xSuppUserName_Type())
wwpLeos8021xSuppUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xSuppUserName.setStatus(_A)
class _WwpLeos8021xSuppPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_WwpLeos8021xSuppPassword_Type.__name__=_D
_WwpLeos8021xSuppPassword_Object=MibTableColumn
wwpLeos8021xSuppPassword=_WwpLeos8021xSuppPassword_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1,3),_WwpLeos8021xSuppPassword_Type())
wwpLeos8021xSuppPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xSuppPassword.setStatus(_A)
_WwpLeos8021xSuppPortStatsClear_Type=TruthValue
_WwpLeos8021xSuppPortStatsClear_Object=MibTableColumn
wwpLeos8021xSuppPortStatsClear=_WwpLeos8021xSuppPortStatsClear_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1,5),_WwpLeos8021xSuppPortStatsClear_Type())
wwpLeos8021xSuppPortStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xSuppPortStatsClear.setStatus(_A)
class _WwpLeos8021xSuppEAPMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('eapMd5',1))
_WwpLeos8021xSuppEAPMethod_Type.__name__=_C
_WwpLeos8021xSuppEAPMethod_Object=MibTableColumn
wwpLeos8021xSuppEAPMethod=_WwpLeos8021xSuppEAPMethod_Object((1,3,6,1,4,1,6141,2,60,401,1,2,2,1,10),_WwpLeos8021xSuppEAPMethod_Type())
wwpLeos8021xSuppEAPMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xSuppEAPMethod.setStatus(_A)
_WwpLeos8021xGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeos8021xGlobalAttrs=_WwpLeos8021xGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,2,3))
_WwpLeos8021xAuthStatsClear_Type=TruthValue
_WwpLeos8021xAuthStatsClear_Object=MibScalar
wwpLeos8021xAuthStatsClear=_WwpLeos8021xAuthStatsClear_Object((1,3,6,1,4,1,6141,2,60,401,1,2,3,1),_WwpLeos8021xAuthStatsClear_Type())
wwpLeos8021xAuthStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xAuthStatsClear.setStatus(_A)
_WwpLeos8021xSuppStatsClear_Type=TruthValue
_WwpLeos8021xSuppStatsClear_Object=MibScalar
wwpLeos8021xSuppStatsClear=_WwpLeos8021xSuppStatsClear_Object((1,3,6,1,4,1,6141,2,60,401,1,2,3,2),_WwpLeos8021xSuppStatsClear_Type())
wwpLeos8021xSuppStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeos8021xSuppStatsClear.setStatus(_A)
_WwpLeos8021xEvents_ObjectIdentity=ObjectIdentity
wwpLeos8021xEvents=_WwpLeos8021xEvents_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,3))
_WwpLeos8021xEventsV2_ObjectIdentity=ObjectIdentity
wwpLeos8021xEventsV2=_WwpLeos8021xEventsV2_ObjectIdentity((1,3,6,1,4,1,6141,2,60,401,1,3,0))
mibBuilder.exportSymbols(_E,**{'wwpLeos8021xMibModule':wwpLeos8021xMibModule,'wwpLeos8021xMIB':wwpLeos8021xMIB,'wwpLeos8021xConf':wwpLeos8021xConf,'wwpLeos8021xGroups':wwpLeos8021xGroups,'wwpLeos8021xCompls':wwpLeos8021xCompls,'wwpLeos8021xObjs':wwpLeos8021xObjs,'wwpLeos8021xPortTable':wwpLeos8021xPortTable,'wwpLeos8021xPortEntry':wwpLeos8021xPortEntry,_F:wwpLeos8021xPort,'wwpLeos8021xRole':wwpLeos8021xRole,'wwpLeos8021xAuthPortStatsClear':wwpLeos8021xAuthPortStatsClear,'wwpLeos8021xSuppTable':wwpLeos8021xSuppTable,'wwpLeos8021xSuppEntry':wwpLeos8021xSuppEntry,_H:wwpLeos8021xSuppPort,'wwpLeos8021xSuppUserName':wwpLeos8021xSuppUserName,'wwpLeos8021xSuppPassword':wwpLeos8021xSuppPassword,'wwpLeos8021xSuppPortStatsClear':wwpLeos8021xSuppPortStatsClear,'wwpLeos8021xSuppEAPMethod':wwpLeos8021xSuppEAPMethod,'wwpLeos8021xGlobalAttrs':wwpLeos8021xGlobalAttrs,'wwpLeos8021xAuthStatsClear':wwpLeos8021xAuthStatsClear,'wwpLeos8021xSuppStatsClear':wwpLeos8021xSuppStatsClear,'wwpLeos8021xEvents':wwpLeos8021xEvents,'wwpLeos8021xEventsV2':wwpLeos8021xEventsV2})