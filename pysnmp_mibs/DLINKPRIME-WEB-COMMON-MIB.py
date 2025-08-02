_I='dpSslServerGroups'
_H='dpWebSessionGroups'
_G='dpSslServerStatus'
_F='dpWebSessionTimeout'
_E='read-write'
_D='TruthValue'
_C='Unsigned32'
_B='DLINKPRIME-WEB-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
dlinkPrimeWebCommonMIB=ModuleIdentity((1,3,6,1,4,1,171,15,28))
if mibBuilder.loadTexts:dlinkPrimeWebCommonMIB.setRevisions(('2014-04-26 00:00',))
_DpWebCommonMIBNotifications_ObjectIdentity=ObjectIdentity
dpWebCommonMIBNotifications=_DpWebCommonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,28,0))
_DpWebMIBObjects_ObjectIdentity=ObjectIdentity
dpWebMIBObjects=_DpWebMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,28,1))
_DpWebSessionObjects_ObjectIdentity=ObjectIdentity
dpWebSessionObjects=_DpWebSessionObjects_ObjectIdentity((1,3,6,1,4,1,171,15,28,1,1))
class _DpWebSessionTimeout_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,36000))
_DpWebSessionTimeout_Type.__name__=_C
_DpWebSessionTimeout_Object=MibScalar
dpWebSessionTimeout=_DpWebSessionTimeout_Object((1,3,6,1,4,1,171,15,28,1,1,1),_DpWebSessionTimeout_Type())
dpWebSessionTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:dpWebSessionTimeout.setStatus(_A)
_DpSslServerObjects_ObjectIdentity=ObjectIdentity
dpSslServerObjects=_DpSslServerObjects_ObjectIdentity((1,3,6,1,4,1,171,15,28,1,2))
class _DpSslServerStatus_Type(TruthValue):defaultValue=2
_DpSslServerStatus_Type.__name__=_D
_DpSslServerStatus_Object=MibScalar
dpSslServerStatus=_DpSslServerStatus_Object((1,3,6,1,4,1,171,15,28,1,2,1),_DpSslServerStatus_Type())
dpSslServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpSslServerStatus.setStatus(_A)
_DpWebCommonMIBConformance_ObjectIdentity=ObjectIdentity
dpWebCommonMIBConformance=_DpWebCommonMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,28,2))
_DpWebCommonMIBCompliances_ObjectIdentity=ObjectIdentity
dpWebCommonMIBCompliances=_DpWebCommonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,28,2,1))
_DpWebCommonGroups_ObjectIdentity=ObjectIdentity
dpWebCommonGroups=_DpWebCommonGroups_ObjectIdentity((1,3,6,1,4,1,171,15,28,2,2))
dpWebSessionGroups=ObjectGroup((1,3,6,1,4,1,171,15,28,2,2,1))
dpWebSessionGroups.setObjects((_B,_F))
if mibBuilder.loadTexts:dpWebSessionGroups.setStatus(_A)
dpSslServerGroups=ObjectGroup((1,3,6,1,4,1,171,15,28,2,2,2))
dpSslServerGroups.setObjects((_B,_G))
if mibBuilder.loadTexts:dpSslServerGroups.setStatus(_A)
dpWebMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,28,2,1,1))
dpWebMIBCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:dpWebMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeWebCommonMIB':dlinkPrimeWebCommonMIB,'dpWebCommonMIBNotifications':dpWebCommonMIBNotifications,'dpWebMIBObjects':dpWebMIBObjects,'dpWebSessionObjects':dpWebSessionObjects,_F:dpWebSessionTimeout,'dpSslServerObjects':dpSslServerObjects,_G:dpSslServerStatus,'dpWebCommonMIBConformance':dpWebCommonMIBConformance,'dpWebCommonMIBCompliances':dpWebCommonMIBCompliances,'dpWebMIBCompliance':dpWebMIBCompliance,'dpWebCommonGroups':dpWebCommonGroups,_H:dpWebSessionGroups,_I:dpSslServerGroups})