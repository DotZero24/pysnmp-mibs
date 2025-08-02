_F='cie1000HttpsConfigGlobalsInfoGroup'
_E='cie1000HttpsConfigGlobalsRedirectToHttps'
_D='cie1000HttpsConfigGlobalsMode'
_C='read-write'
_B='CIE1000-HTTPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cie1000SwitchMgmt,=mibBuilder.importSymbols('CISCO-IE1000-MIB','cie1000SwitchMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cie1000HttpsMib=ModuleIdentity((1,3,6,1,4,1,9,9,832,1,47))
if mibBuilder.loadTexts:cie1000HttpsMib.setRevisions(('2014-10-10 00:00','2014-07-01 00:00'))
_Cie1000HttpsMibObjects_ObjectIdentity=ObjectIdentity
cie1000HttpsMibObjects=_Cie1000HttpsMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,1))
_Cie1000HttpsConfig_ObjectIdentity=ObjectIdentity
cie1000HttpsConfig=_Cie1000HttpsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,1,2))
_Cie1000HttpsConfigGlobals_ObjectIdentity=ObjectIdentity
cie1000HttpsConfigGlobals=_Cie1000HttpsConfigGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,1,2,1))
_Cie1000HttpsConfigGlobalsMode_Type=TruthValue
_Cie1000HttpsConfigGlobalsMode_Object=MibScalar
cie1000HttpsConfigGlobalsMode=_Cie1000HttpsConfigGlobalsMode_Object((1,3,6,1,4,1,9,9,832,1,47,1,2,1,1),_Cie1000HttpsConfigGlobalsMode_Type())
cie1000HttpsConfigGlobalsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000HttpsConfigGlobalsMode.setStatus(_A)
_Cie1000HttpsConfigGlobalsRedirectToHttps_Type=TruthValue
_Cie1000HttpsConfigGlobalsRedirectToHttps_Object=MibScalar
cie1000HttpsConfigGlobalsRedirectToHttps=_Cie1000HttpsConfigGlobalsRedirectToHttps_Object((1,3,6,1,4,1,9,9,832,1,47,1,2,1,2),_Cie1000HttpsConfigGlobalsRedirectToHttps_Type())
cie1000HttpsConfigGlobalsRedirectToHttps.setMaxAccess(_C)
if mibBuilder.loadTexts:cie1000HttpsConfigGlobalsRedirectToHttps.setStatus(_A)
_Cie1000HttpsMibConformance_ObjectIdentity=ObjectIdentity
cie1000HttpsMibConformance=_Cie1000HttpsMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,2))
_Cie1000HttpsMibCompliances_ObjectIdentity=ObjectIdentity
cie1000HttpsMibCompliances=_Cie1000HttpsMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,2,1))
_Cie1000HttpsMibGroups_ObjectIdentity=ObjectIdentity
cie1000HttpsMibGroups=_Cie1000HttpsMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,832,1,47,2,2))
cie1000HttpsConfigGlobalsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,832,1,47,2,2,1))
cie1000HttpsConfigGlobalsInfoGroup.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:cie1000HttpsConfigGlobalsInfoGroup.setStatus(_A)
cie1000HttpsMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,832,1,47,2,1,1))
cie1000HttpsMibCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:cie1000HttpsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cie1000HttpsMib':cie1000HttpsMib,'cie1000HttpsMibObjects':cie1000HttpsMibObjects,'cie1000HttpsConfig':cie1000HttpsConfig,'cie1000HttpsConfigGlobals':cie1000HttpsConfigGlobals,_D:cie1000HttpsConfigGlobalsMode,_E:cie1000HttpsConfigGlobalsRedirectToHttps,'cie1000HttpsMibConformance':cie1000HttpsMibConformance,'cie1000HttpsMibCompliances':cie1000HttpsMibCompliances,'cie1000HttpsMibCompliance':cie1000HttpsMibCompliance,'cie1000HttpsMibGroups':cie1000HttpsMibGroups,_F:cie1000HttpsConfigGlobalsInfoGroup})