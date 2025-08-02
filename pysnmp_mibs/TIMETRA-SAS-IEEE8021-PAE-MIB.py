_F='dot1xAuthConfigExtnGroup'
_E='dot1xPortEtherTunnel'
_D='dot1xAuthConfigExtnEntry'
_C='TruthValue'
_B='TIMETRA-SAS-IEEE8021-PAE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1xAuthConfigEntry,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','dot1xAuthConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
ServiceAdminStatus,TNamedItem,TPolicyStatementNameOrEmpty=mibBuilder.importSymbols('TIMETRA-TC-MIB','ServiceAdminStatus','TNamedItem','TPolicyStatementNameOrEmpty')
timeraSASIEEE8021PaeMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,17))
if mibBuilder.loadTexts:timeraSASIEEE8021PaeMIBModule.setRevisions(('1912-07-01 00:00',))
_TmnxSASDot1xConformance_ObjectIdentity=ObjectIdentity
tmnxSASDot1xConformance=_TmnxSASDot1xConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,12))
_TmnxDot1xSASCompliancs_ObjectIdentity=ObjectIdentity
tmnxDot1xSASCompliancs=_TmnxDot1xSASCompliancs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,12,1))
_TmnxDot1xSASGroups_ObjectIdentity=ObjectIdentity
tmnxDot1xSASGroups=_TmnxDot1xSASGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,12,2))
_TmnxSASDot1xObjs_ObjectIdentity=ObjectIdentity
tmnxSASDot1xObjs=_TmnxSASDot1xObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,16))
_TmnxSASDot1xAuthenticatorObjs_ObjectIdentity=ObjectIdentity
tmnxSASDot1xAuthenticatorObjs=_TmnxSASDot1xAuthenticatorObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,16,1))
_Dot1xAuthConfigExtnTable_Object=MibTable
dot1xAuthConfigExtnTable=_Dot1xAuthConfigExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,16,1,1))
if mibBuilder.loadTexts:dot1xAuthConfigExtnTable.setStatus(_A)
_Dot1xAuthConfigExtnEntry_Object=MibTableRow
dot1xAuthConfigExtnEntry=_Dot1xAuthConfigExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,16,1,1,1))
if mibBuilder.loadTexts:dot1xAuthConfigExtnEntry.setStatus(_A)
class _Dot1xPortEtherTunnel_Type(TruthValue):defaultValue=2
_Dot1xPortEtherTunnel_Type.__name__=_C
_Dot1xPortEtherTunnel_Object=MibTableColumn
dot1xPortEtherTunnel=_Dot1xPortEtherTunnel_Object((1,3,6,1,4,1,6527,6,2,2,2,16,1,1,1,150),_Dot1xPortEtherTunnel_Type())
dot1xPortEtherTunnel.setMaxAccess('read-write')
if mibBuilder.loadTexts:dot1xPortEtherTunnel.setStatus(_A)
dot1xAuthConfigEntry.registerAugmentions((_B,_D))
dot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
dot1xAuthConfigExtnGroup=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,12,2,1))
dot1xAuthConfigExtnGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:dot1xAuthConfigExtnGroup.setStatus(_A)
dot1xAuthConfigExtnCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,12,1,1))
dot1xAuthConfigExtnCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:dot1xAuthConfigExtnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timeraSASIEEE8021PaeMIBModule':timeraSASIEEE8021PaeMIBModule,'tmnxSASDot1xConformance':tmnxSASDot1xConformance,'tmnxDot1xSASCompliancs':tmnxDot1xSASCompliancs,'dot1xAuthConfigExtnCompliance':dot1xAuthConfigExtnCompliance,'tmnxDot1xSASGroups':tmnxDot1xSASGroups,_F:dot1xAuthConfigExtnGroup,'tmnxSASDot1xObjs':tmnxSASDot1xObjs,'tmnxSASDot1xAuthenticatorObjs':tmnxSASDot1xAuthenticatorObjs,'dot1xAuthConfigExtnTable':dot1xAuthConfigExtnTable,_D:dot1xAuthConfigExtnEntry,_E:dot1xPortEtherTunnel})