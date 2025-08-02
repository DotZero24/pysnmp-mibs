_F='tnDot1xAuthConfigExtnGroup'
_E='tnDot1xPortEtherTunnel'
_D='tnDot1xAuthConfigExtnEntry'
_C='TruthValue'
_B='TN-SAS-IEEE8021-PAE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1xAuthConfigEntry,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','dot1xAuthConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
tnSASModules,tnSASObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSASModules','tnSASObjs')
tnSASIEEE8021PaeMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,7,2,1,1,17))
if mibBuilder.loadTexts:tnSASIEEE8021PaeMIBModule.setRevisions(('2015-01-09 00:00',))
_TnSASDot1xMIBObjs_ObjectIdentity=ObjectIdentity
tnSASDot1xMIBObjs=_TnSASDot1xMIBObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,16))
_TnSASDot1xAuthenticatorObjs_ObjectIdentity=ObjectIdentity
tnSASDot1xAuthenticatorObjs=_TnSASDot1xAuthenticatorObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,16,1))
_TnDot1xAuthConfigExtnTable_Object=MibTable
tnDot1xAuthConfigExtnTable=_TnDot1xAuthConfigExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,16,1,1))
if mibBuilder.loadTexts:tnDot1xAuthConfigExtnTable.setStatus(_A)
_TnDot1xAuthConfigExtnEntry_Object=MibTableRow
tnDot1xAuthConfigExtnEntry=_TnDot1xAuthConfigExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,16,1,1,1))
if mibBuilder.loadTexts:tnDot1xAuthConfigExtnEntry.setStatus(_A)
class _TnDot1xPortEtherTunnel_Type(TruthValue):defaultValue=2
_TnDot1xPortEtherTunnel_Type.__name__=_C
_TnDot1xPortEtherTunnel_Object=MibTableColumn
tnDot1xPortEtherTunnel=_TnDot1xPortEtherTunnel_Object((1,3,6,1,4,1,7483,7,2,2,2,16,1,1,1,1),_TnDot1xPortEtherTunnel_Type())
tnDot1xPortEtherTunnel.setMaxAccess('read-write')
if mibBuilder.loadTexts:tnDot1xPortEtherTunnel.setStatus(_A)
_TnDot1xSASCompliancs_ObjectIdentity=ObjectIdentity
tnDot1xSASCompliancs=_TnDot1xSASCompliancs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,16,2))
_TnDot1xSASGroups_ObjectIdentity=ObjectIdentity
tnDot1xSASGroups=_TnDot1xSASGroups_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,16,3))
dot1xAuthConfigEntry.registerAugmentions((_B,_D))
tnDot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
tnDot1xAuthConfigExtnGroup=ObjectGroup((1,3,6,1,4,1,7483,7,2,2,2,16,3,1))
tnDot1xAuthConfigExtnGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:tnDot1xAuthConfigExtnGroup.setStatus(_A)
tnDot1xAuthConfigExtnCompliance=ModuleCompliance((1,3,6,1,4,1,7483,7,2,2,2,16,2,1))
tnDot1xAuthConfigExtnCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:tnDot1xAuthConfigExtnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnSASIEEE8021PaeMIBModule':tnSASIEEE8021PaeMIBModule,'tnSASDot1xMIBObjs':tnSASDot1xMIBObjs,'tnSASDot1xAuthenticatorObjs':tnSASDot1xAuthenticatorObjs,'tnDot1xAuthConfigExtnTable':tnDot1xAuthConfigExtnTable,_D:tnDot1xAuthConfigExtnEntry,_E:tnDot1xPortEtherTunnel,'tnDot1xSASCompliancs':tnDot1xSASCompliancs,'tnDot1xAuthConfigExtnCompliance':tnDot1xAuthConfigExtnCompliance,'tnDot1xSASGroups':tnDot1xSASGroups,_F:tnDot1xAuthConfigExtnGroup})