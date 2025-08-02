_H='dpDosPrevBasicGroup'
_G='dpDosPrevCtrlEnabled'
_F='read-write'
_E='dpDosPrevCtrlAttackType'
_D='TruthValue'
_C='Integer32'
_B='DLINKPRIME-DOS-PREVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
dlinkPrimeDosPrevMIB=ModuleIdentity((1,3,6,1,4,1,171,15,4))
if mibBuilder.loadTexts:dlinkPrimeDosPrevMIB.setRevisions(('2014-04-26 00:00',))
class DosAttackType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,99)));namedValues=NamedValues(*(('landAttack',1),('blatAttack',2),('tcpNullScan',3),('tcpXmasScan',4),('tcpSynFin',5),('tcpSynSrcPortLess1024',6),('pingDeathAttack',7),('all',99)))
_DpDosPrevMIBNotifications_ObjectIdentity=ObjectIdentity
dpDosPrevMIBNotifications=_DpDosPrevMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,4,0))
_DpDosPrevMIBObjects_ObjectIdentity=ObjectIdentity
dpDosPrevMIBObjects=_DpDosPrevMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,4,1))
_DpDosPrevCtrlTable_Object=MibTable
dpDosPrevCtrlTable=_DpDosPrevCtrlTable_Object((1,3,6,1,4,1,171,15,4,1,1))
if mibBuilder.loadTexts:dpDosPrevCtrlTable.setStatus(_A)
_DpDosPrevCtrlEntry_Object=MibTableRow
dpDosPrevCtrlEntry=_DpDosPrevCtrlEntry_Object((1,3,6,1,4,1,171,15,4,1,1,1))
dpDosPrevCtrlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dpDosPrevCtrlEntry.setStatus(_A)
_DpDosPrevCtrlAttackType_Type=DosAttackType
_DpDosPrevCtrlAttackType_Object=MibTableColumn
dpDosPrevCtrlAttackType=_DpDosPrevCtrlAttackType_Object((1,3,6,1,4,1,171,15,4,1,1,1,1),_DpDosPrevCtrlAttackType_Type())
dpDosPrevCtrlAttackType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dpDosPrevCtrlAttackType.setStatus(_A)
class _DpDosPrevCtrlEnabled_Type(TruthValue):defaultValue=2
_DpDosPrevCtrlEnabled_Type.__name__=_D
_DpDosPrevCtrlEnabled_Object=MibTableColumn
dpDosPrevCtrlEnabled=_DpDosPrevCtrlEnabled_Object((1,3,6,1,4,1,171,15,4,1,1,1,2),_DpDosPrevCtrlEnabled_Type())
dpDosPrevCtrlEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:dpDosPrevCtrlEnabled.setStatus(_A)
class _DpDosPrevCtrlActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('drop',1))
_DpDosPrevCtrlActionType_Type.__name__=_C
_DpDosPrevCtrlActionType_Object=MibTableColumn
dpDosPrevCtrlActionType=_DpDosPrevCtrlActionType_Object((1,3,6,1,4,1,171,15,4,1,1,1,3),_DpDosPrevCtrlActionType_Type())
dpDosPrevCtrlActionType.setMaxAccess(_F)
if mibBuilder.loadTexts:dpDosPrevCtrlActionType.setStatus(_A)
_DpDosPrevMIBConformance_ObjectIdentity=ObjectIdentity
dpDosPrevMIBConformance=_DpDosPrevMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,4,2))
_DpDosPrevMIBCompliances_ObjectIdentity=ObjectIdentity
dpDosPrevMIBCompliances=_DpDosPrevMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,4,2,1))
_DpDosPrevMIBGroups_ObjectIdentity=ObjectIdentity
dpDosPrevMIBGroups=_DpDosPrevMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,4,2,2))
dpDosPrevBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,4,2,2,1))
dpDosPrevBasicGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:dpDosPrevBasicGroup.setStatus(_A)
dpDosPrevMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,4,2,1,1))
dpDosPrevMIBCompliance.setObjects(*((_B,_H),(_B,'dpDosPrevActionRedirectCtrlGroup')))
if mibBuilder.loadTexts:dpDosPrevMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DosAttackType':DosAttackType,'dlinkPrimeDosPrevMIB':dlinkPrimeDosPrevMIB,'dpDosPrevMIBNotifications':dpDosPrevMIBNotifications,'dpDosPrevMIBObjects':dpDosPrevMIBObjects,'dpDosPrevCtrlTable':dpDosPrevCtrlTable,'dpDosPrevCtrlEntry':dpDosPrevCtrlEntry,_E:dpDosPrevCtrlAttackType,_G:dpDosPrevCtrlEnabled,'dpDosPrevCtrlActionType':dpDosPrevCtrlActionType,'dpDosPrevMIBConformance':dpDosPrevMIBConformance,'dpDosPrevMIBCompliances':dpDosPrevMIBCompliances,'dpDosPrevMIBCompliance':dpDosPrevMIBCompliance,'dpDosPrevMIBGroups':dpDosPrevMIBGroups,_H:dpDosPrevBasicGroup})