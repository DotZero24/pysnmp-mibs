if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ekinops,=mibBuilder.importSymbols('EKINOPS-MIB','ekinops')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
modulePmPassive=ModuleIdentity((1,3,6,1,4,1,20044,20))
if mibBuilder.loadTexts:modulePmPassive.setRevisions(('2007-01-05 00:00',))
_Pmpassiveri_ObjectIdentity=ObjectIdentity
pmpassiveri=_Pmpassiveri_ObjectIdentity((1,3,6,1,4,1,20044,20,1))
_PmpassiveRinvHwPlatform_Type=OctetString
_PmpassiveRinvHwPlatform_Object=MibScalar
pmpassiveRinvHwPlatform=_PmpassiveRinvHwPlatform_Object((1,3,6,1,4,1,20044,20,1,1),_PmpassiveRinvHwPlatform_Type())
pmpassiveRinvHwPlatform.setMaxAccess('read-only')
if mibBuilder.loadTexts:pmpassiveRinvHwPlatform.setStatus('current')
mibBuilder.exportSymbols('EKINOPS-PmPassive-MIB',**{'modulePmPassive':modulePmPassive,'pmpassiveri':pmpassiveri,'pmpassiveRinvHwPlatform':pmpassiveRinvHwPlatform})